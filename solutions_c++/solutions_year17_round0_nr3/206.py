#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
typedef long long ll;

int tc;
ll k, n;
map<ll,ll> cnt;
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%lld %lld", &n, &k);
		cnt[-n] = 1;
		while (k > 0) {
			ll sz, cc;
			tie(sz,cc) = *cnt.begin();
			sz = -sz;
			cnt.erase(cnt.begin());
			cnt[-(sz-1)/2] += cc;
			cnt[-sz/2] += cc;
			k -= cc;
			if (k <= 0) printf("%lld %lld\n", sz/2, (sz-1)/2);
		}
		cnt.clear();
	}

	return 0;
}