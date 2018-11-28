#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;

#define fi first
#define se second
#define debug(...)
//#define debug(...) fprintf(stderr, __VA_ARGS__)

ll N, K;

pll go() {
	scanf("%lld %lld", &N, &K);

	//largest power of two MINUS 1 before K
	ll lpwr2 = 0;
	while (2 * lpwr2 + 1 < K) {
		lpwr2 = 2 * lpwr2 + 1;
	}

	//after lpwr2 cuts
	N -= lpwr2;
	ll v1 = N / (lpwr2 + 1), v2 = v1 + 1;
	debug("v1 = %lld, v2 = %lld\n", v1, v2);
	debug("N = %lld\n", N);

	ll nbig = N - v1 * (lpwr2 + 1), nsmall = lpwr2 + 1 - nbig;
	debug("nsmall = %lld, nbig = %lld\n", nsmall, nbig);

	K -= lpwr2;
	//how many more there to go?
	ll val = (K <= nbig ? v2 : v1);
	ll bigpiece = val / 2, smallpiece = bigpiece - (val % 2 == 0);
	return pll(bigpiece, smallpiece);
}

int main() {
	freopen("cin.in", "r", stdin);
	freopen("cout.out", "w", stdout);

	int nq;
	scanf("%d", &nq);
	for (int i = 1; i <= nq; i++) {
		pll ans = go();
		printf("Case #%d: %lld %lld\n", i, ans.fi, ans.se);
	}
}
