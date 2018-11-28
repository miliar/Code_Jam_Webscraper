#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> ii;

ii solve (ll n, ll k) {
	ll pot = 1;
	ll left = 1, right = 0;
	for (; k > pot; n >>= 1LL, k -= pot, pot <<= 1LL) {
		if (n & 1)
			left = (pot << 1LL) - right;
		else
			right = (pot << 1LL) - left;
	}
	if (k > left)
		--n;
	return make_pair(n >> 1LL, (n-1) >> 1LL);
}

int main () {
	int test; scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		ll n, k; scanf("%lld %lld", &n, &k);
		printf("Case #%d: ", t);
		ii ans = solve(n, k);
		printf("%lld %lld\n", ans.first, ans.second);
	}
	return 0;
}