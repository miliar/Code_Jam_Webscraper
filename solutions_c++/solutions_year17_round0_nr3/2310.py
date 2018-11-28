#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
const ll INF = 2e18;
map<pll, ll> m;

ll f(ll a, ll b) {
	if (b == 0) return INF;
	if (b == 1) return a;
	pll p(a,b);
	map<pll,ll>::iterator it = m.find(p);
	if (it == m.end()) {
		ll ans = min(f(a/2, b/2), f((a-1)/2, (b-1)/2));
		m[p] = ans;
		return ans;
	} else {
		return it->second;
	}
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++) {
		ll n, m;
		scanf("%lld %lld", &n, &m);
		ll ans = f(n, m);
		printf("Case #%d: %lld %lld\n", t, ans/2, (ans-1)/2);
	}
}