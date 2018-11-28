#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <functional>

using namespace std;

typedef pair<long long int, long long int> P;
typedef pair<long long int, P> Q;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		long long int n, k;
		cin >> n >> k;

		priority_queue<Q, vector<Q>, greater<Q> > pq;
		
		pq.push(Q(-(n+1), P(0, n+1)));

		printf("Case #%d: ", i+1);
		for (long long int i = 0; i < k; i++) {
			Q q = pq.top();
			pq.pop();
			P p = q.second;
			//cout << p.first << ' ' << p.second << endl;
			long long int mid = p.second + p.first;
			mid /= 2;
			//cout << mid << endl;
			if (i == k - 1) {
				cout << max(mid - p.first, p.second - mid)-1 << ' ' << min(mid - p.first, p.second - mid)-1 << endl;
			}
			pq.push(Q(p.first-mid, P(p.first, mid)));
			pq.push(Q(mid-p.second, P(mid, p.second)));
		}
		
	}
	return 0;
}