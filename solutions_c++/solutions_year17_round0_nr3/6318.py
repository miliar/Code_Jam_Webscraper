#include <iostream>
#include <algorithm>
#include <vector>
// #include <pair>
using namespace std;

int main(){
	int T;
	cin >> T;
	for (int z = 0; z < T; ++z){
		long long N, K, mid;
		cin >> N >> K;
		vector <pair<long long, long long>> v;
		v.push_back(make_pair(0, N+1));
		auto foo = [](pair<long long, long long> &a, pair<long long, long long> &b){
			if (a.second-a.first == b.second-b.first)
				return a.first > b.first;
			else
				return a.second-a.first < b.second-b.first;
		};
		pair<long, long> m;
		make_heap(v.begin(), v.end(), foo);
		for (int i = 0; i < K; ++i){
			m = v.front();
			mid = m.first + (m.second - m.first)/2;
			// cout << m.first << " " << mid << " " << m.second <<  endl;
			pop_heap(v.begin(), v.end(), foo);
			v.pop_back();
			v.push_back(make_pair(m.first, mid));
			push_heap(v.begin(), v.end(), foo);
			v.push_back(make_pair(mid, m.second));
			push_heap(v.begin(), v.end(), foo);
		}
		cout << "Case #" << z+1 << ": " << max(mid - m.first, m.second - mid)-1 << " " << min(mid - m.first, m.second - mid)-1 << endl;
	}
}