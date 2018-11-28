#include<map>
#include<algorithm>
#include<cstdio>
#include<utility>
using namespace std;

typedef long long ll;
pair<ll, ll> process(ll N, ll K){
	map<ll, ll> dp;
	dp[N] = 1;

	while (1){
		const auto &kv = prev(dp.end());
		ll n = kv->first, occ = kv->second;
		ll small = (n - 1) / 2;
		ll large = n - 1 - small;
		if (K <= occ) return pair<ll, ll>(large, small);
		dp.erase(prev(dp.end()));
		K -= occ;

		if (small) dp[small] += occ;
		if (large) dp[large] += occ;
	}
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		ll N, K; scanf("%lld%lld", &N, &K);
		auto p = process(N, K);
		printf("%lld %lld\n", p.first, p.second);
	}
}