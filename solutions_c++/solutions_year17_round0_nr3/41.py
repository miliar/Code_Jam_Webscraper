#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
ll N;
ll calc(ll mngap) {
	map<ll, ll> S;
	S[N + 1] = 1;
	ll ret = 0;
	while (!S.empty()) {
		map<ll, ll> NS;
		for (auto s : S) {
			ll a = s.first, c = s.second;
			if (a >= mngap) {
				NS[a / 2] += c;
				NS[a - a / 2] += c;
				ret += c;
			}
		}
		S = NS;
	}
	return ret;
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		ll K;
		scanf("%lld%lld", &N, &K);
		ll lo = 2, hi = N + 1;
		while (lo < hi) {
			ll m = (lo + hi + 1) / 2;
			if (calc(m) >= K) lo = m;
			else hi = m - 1;
		}
		printf("Case #%d: %lld %lld\n", cn, (lo + 1) / 2 - 1, lo / 2 - 1);
	}
}

