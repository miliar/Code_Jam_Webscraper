#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
pair<ll, ll> solve(ll n, ll k) {
	ll cnt = 1, sum = 0;
	while (true) {
		if (k - sum <= cnt) {
			k -= sum;	
			ll ave = (n - sum) / cnt;
			ll l = ave + (k <= (n - sum) % cnt);
			ll m = (l - 1) >> 1;	
			return make_pair(max(m, l - 1 - m), min(m, l - 1 - m));
		} else {
			sum += cnt;	
			cnt <<= 1;
		}
	}
	return make_pair(-1, -1);
}
int main() {
	freopen("C2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		ll n, k;
		scanf("%lld%lld", &n, &k);
		pair<ll, ll> ans = solve(n, k);
		printf("Case #%d: %lld %lld\n", cas + 1, ans.first, ans.second);
	}
	return 0;
}
