#include <cstdio>
#include <queue>
using namespace std;
typedef long long ll;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		ll n, k;
		scanf("%lld%lld", &n, &k);
		priority_queue<pair<ll, ll>> pq;
		ll cnt = 0;
		pq.emplace(n, 1ll);
		while (true) {
			ll space = pq.top().first;
			ll num = pq.top().second;
			cnt += num;
			if (cnt >= k) break;
			pq.pop();
			priority_queue<pair<ll, ll>> tmp;
			if (space&1) {
				num += num;
				while (!pq.empty()) {
					if (pq.top().first != space/2) {
						tmp.push(pq.top());
					} else {
						num += pq.top().second;
					}
					pq.pop();
				}
				tmp.emplace(space/2, num);
			} else {
				ll num1 = num, num2 = num;
				while (!pq.empty()) {
					if (pq.top().first == space/2) {
						num1 += pq.top().second;
					} else if (pq.top().first == space/2 - 1) {
						num2 += pq.top().second;
					} else {
						tmp.push(pq.top());
					}
					pq.pop();
				}
				tmp.emplace(space/2, num1);
				tmp.emplace(space/2-1, num2);
			}
			pq = tmp;
		}
		ll ans = pq.top().first;
		printf("Case #%d: ", TN);
		if (ans&1) printf("%lld %lld\n", ans/2, ans/2);
		else printf("%lld %lld\n", ans/2, ans/2-1);
	}
	return 0;
}