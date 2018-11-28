#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define mp make_pair

priority_queue <pair<ll, ll> > pq;

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("respc2", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		ll n, k;
		while(!pq.empty())
			pq.pop();
		scanf("%lld %lld", &n, &k);
		if (k >= n) {
			printf("Case #%d: 0 0\n", i + 1);
			continue;
		}
		pq.push(mp(n, 1));
		ll index = 0;
		ll d, q;
		while(1) {
			d = pq.top().first;
			q = pq.top().second;
			index += q;
			if (index >= k)
				break;
			pq.pop();
			if (d & 1) {
				//Impar
				d >>= 1;
				pq.push(mp(d, (q << 1)));
			} else {
				//Par
				d >>= 1;
				pq.push(mp(d, q));
				pq.push(mp(d - 1, q));
			}
		}
		ll resp1, resp2;
		resp1 = d >> 1;
		resp2 = resp1;
		if (!(d & 1)) resp2--;
		printf("Case #%d: %lld %lld\n", i + 1, resp1, resp2);

	}
	return 0;
}
