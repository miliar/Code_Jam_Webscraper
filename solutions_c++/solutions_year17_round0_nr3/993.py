#include <bits/stdc++.h>
using namespace std;
typedef pair<long long, long long> pi;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int tc;
	cin >> tc;
	for (int q = 1; q <= tc; q++) {
		priority_queue<pi, vector<pi>, less<pi> > pq;
		long long n,k;
		cin >> n >> k;
		long long count = 0;
		pq.push(make_pair(n, 1));
		while (true) {
			long long a,b = 0;
			do {
				pi x = pq.top();
				a = x.first;
				b += x.second;
				pq.pop();
			} while (pq.top().first == a && pq.size() > 0);
			a -= 1;
			if (a % 2 == 0) {
				pq.push(make_pair(a/2, b*2));
				count += b;
				if (count >= k ) {
					printf("Case #%d: %lld %lld\n", q, a/2, a/2);
					break;
				}
			}
			else {
				pq.push(make_pair(a/2, b));
				pq.push(make_pair(a/2 + 1, b));
				count += b;
				if (count >= k ) {
					printf("Case #%d: %lld %lld\n", q, a/2+1, a/2);
					break;
				}
			}
		}
	}
}
