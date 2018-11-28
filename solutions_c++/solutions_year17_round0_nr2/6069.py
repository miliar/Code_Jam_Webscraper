#include <cstdio>
#include <iostream>
#include <vector>
#define MAX 1000000000000000000
using namespace std;
vector<long long> v;
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	for (int i = 1; i <= 9; i++){
		v.push_back(i);
	}
	int idx = 0;
	while (true){
		if (idx >= v.size()) break;
		long long curr = v[idx];
		long long last = curr%10;
		for (int i = last; i <= 9; i++){
			long long res = curr*10ll+(long long)i;
			if (res < MAX && res > 0) v.push_back(res);
		}
		idx++;
	}
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		long long N;
		cin >> N;
		int l = 0;
		int r = v.size()-1;
		while (l < r){
			int m = (l+r+1)/2;
			if (v[m] > N){
				r = m-1;
			}
			else{
				l = m;
			}
		}
		cout << "Case #" << t+1 << ": " << v[l] << endl;
	}
}