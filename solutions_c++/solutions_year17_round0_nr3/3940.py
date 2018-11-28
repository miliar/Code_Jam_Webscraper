#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;

int T, C=1;
ll N, K;

pll getMaxMin(ll n) {
	ll m = n/2;
	if (n%2 == 1) {
		return pll(m, m);
	} else {
		return pll(m, m-1);
	}
}

pll main2() {
	ll nlevel = floor(log2(N)) + 1;
	ll klevel = floor(log2(K)) + 1;

	if (klevel == nlevel) {
		return pll(0,0);
	}
	if (klevel == 1) {
		return getMaxMin(N);
	}

	ll items = exp2(klevel) / 2;
	ll maxCount = (N % items) + 1;

	ll levelMaxLR = N / exp2(klevel-1);
	ll levelMinLR = levelMaxLR;
	if (maxCount == items) {
		return getMaxMin(levelMaxLR);
	} else {
		levelMinLR--;
	}

	if ((K - items) < maxCount) {
		return getMaxMin(levelMaxLR);
	} else {
		return getMaxMin(levelMinLR);
	}
}

int main(void) {
	cin >> T;
	while (T--) {
		cin >> N >> K;
		pll res = main2();
		printf("Case #%d: %lld %lld\n", C++, res.first, res.second);
	}
	return 0;
}