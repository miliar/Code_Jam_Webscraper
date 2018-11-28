#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#define int long long
using namespace std;

signed main() {
	int T; cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		int n, k; cin >> n >> k;
		map<int,int> m;
		m[n] = 1;
		while(k != 1) {
			// printf("k = %lld\n", k);
			int i = m.rbegin()->first;
			int j = min(m[i], k-1);
			// printf("%lld %lld\n", i,j);
			k -= j;
			m[i] -= j;
			if(m[i] == 0) m.erase(i);
			m[(i-1)/2] += j;
			m[i-1-(i-1)/2] += j;

			// cout << m.size() << endl;
		}
		int i = m.rbegin()->first;
		printf("Case #%lld: %lld %lld\n", tc, i-1-(i-1)/2, (i-1)/2);

		/*
		priority_queue<int> pq; pq.push(n);
		while(--k) {
			int i = pq.top(); pq.pop();
			// cout << i << endl;
			pq.push((i-1)/2);
			pq.push(i-1-(i-1)/2);
		}

		int i = pq.top();
		cout << i << endl;
		printf("Case #%lld: %lld %lld\n", tc, i-1-(i-1)/2, (i-1)/2);
		*/
	}
}
