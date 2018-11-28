#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll msb(ll k){
	ll i;

	for (i = 62ll; i >= 0ll; i--){
		if (k & (1ll << i)){
			break;
		}
	}

	return i;
}

int main(){
	ll n, k, g, b, l, r, x;
	int t, i;

	assert(scanf("%d", &t) == 1);

	for (i = 1; i <= t; i++){
		assert(scanf("%lld%lld", &n, &k) == 2);

		k--;
		b = msb(k + 1ll);
		g = 1ll << b;
		k -= (g - 1ll);
		x = (n - g + 1ll) / g;

		if ((n - g + 1ll) % g > k){
			l = x / 2ll;
			r = (x + 1ll) / 2ll;
		}
		else{
			l = (x - 1ll) / 2ll;
			r = x / 2ll;
		}

		printf("Case #%d: %lld %lld\n", i, max(l, r), min(l, r));
	}

	return 0;
}