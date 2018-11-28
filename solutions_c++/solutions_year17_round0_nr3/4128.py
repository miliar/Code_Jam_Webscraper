#include <iostream>
#include <queue>
#include <algorithm>

using in = long long int;
using namespace std;

#define forn(i, n) for(in i = 0; i<(n); ++i)
#define forv(i, v) forn(i, v.size())

pair<int,int> half(int n) {
	return {n/2,(n-1)/2};
}

void testcase() {
	int N, K; 
	cin >> N >> K;
	priority_queue<pair<int,int>> pq;
	pq.push(half(N));
	for(int k = 1; k<K; k++) {
		auto p = pq.top(); pq.pop();
		// cout << "split " << p.first << " " << p.second << endl; 
		pq.push(half(p.first));
		pq.push(half(p.second));
	}
	cout << pq.top().first << " " << pq.top().second;
}

int main() {
	int T; cin >> T;
	for(int t = 1; t<=T; t++) {
		cout << "Case #" << t << ": "; testcase(); cout << endl;
	}
}