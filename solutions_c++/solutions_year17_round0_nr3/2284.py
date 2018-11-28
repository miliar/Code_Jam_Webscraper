#include <stdio.h>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;
map<ll, pair< ll, ll > > dp;
ll num[2];
ll N, K;

pair<ll,ll> cal(ll n, int lev) {
	if (lev == 0) {
		num[n & 1] = n;
		if (n & 1) return make_pair(0, 1);
		return make_pair(1, 0);
	}
	map<ll, pair<ll, ll> >::iterator it = dp.find(n);
	if (it == dp.end()) {
		pair<ll, ll> pr1 = cal((n - 1) / 2, lev - 1);
		pair<ll, ll> pr2 = cal((n - 1) - (n - 1) / 2, lev - 1);
		dp[n] = make_pair(pr1.first + pr2.first, pr1.second + pr2.second);
	}
	return dp[n];
}

int main() {
	//freopen("input.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	setbuf(stdout, NULL);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%lld %lld", &N, &K);
		num[0] = num[1] = -1LL;
		dp.clear();
		int lev = 0;
		ll k = 1, kSum = 1;
		for (; kSum < K; k = 2 * k, kSum += k, lev += 1);
		kSum -= k;
		K -= kSum;
		pair<ll, ll> pr = cal(N, lev);
		ll sp;
		if (num[0] > num[1]) sp = (pr.first >= K ? num[0] : num[1]);
		else sp = (pr.second >= K ? num[1] : num[0]);
		sp--;
		//printf("%lld: %lld, %lld: %lld, %lld\n", num[0], pr.first, num[1], pr.second, K);
		printf("Case #%d: %lld %lld\n", t, sp - sp / 2, sp / 2);
	}
	return 0;
}