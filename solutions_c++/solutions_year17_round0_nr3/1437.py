#include <stdio.h>
#include <iostream>
#include <string>
#include <assert.h>
#include <map>

using namespace std;
typedef long long ll;

ll min(ll a, ll b) {
	return a<b? a: b;
}
void add(map<ll, ll> &m, ll idx, ll cnt) {
	if (m.find(idx)==m.end()) {
		m[idx] =cnt;
	}
	else {
		m[idx] = m[idx] + cnt;
	}
}
void solve(void) {

	ll N, K; scanf("%lld %lld", &N, &K);
	map<ll, ll> m;
	m.insert({N, 1LL});
	ll cnt = 0;

	ll ans_max= -1LL, ans_min = 1e19;
	while(K>cnt) {
		map<ll, ll> nxt;
		for (map<ll, ll>::reverse_iterator rit = m.rbegin(); rit != m.rend(); rit++) {
			auto e = *rit;
			if (K<=cnt) break;
			if (e.first <= 0) continue;
			ll new_customer = min(e.second, K - cnt);
			add(nxt, e.first/2LL, new_customer);
			add(nxt, (e.first-1LL)/2LL, new_customer);
			cnt += new_customer;
			ans_max = e.first / 2LL;
			ans_min = (e.first -1LL) / 2LL;
		}
		m = nxt;
	}

	/*printf("Map info\n");
	for (const auto &e: m) {
		printf("%lld %lld\n", e.first, e.second);
	}*/

	printf("%lld %lld\n", ans_max, ans_min);
}
int main(void) {
	int T; scanf("%d", &T);
	for (int tc=1; tc<=T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
}
