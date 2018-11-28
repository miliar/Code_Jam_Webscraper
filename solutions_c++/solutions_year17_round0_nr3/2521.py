#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef long long ll;
ll n, k, len;
map<ll, ll> dp[64];
ll calc(int d, ll n) {
	if (!d)
		return n >= len;
	if (dp[d].find(n) != dp[d].end())
		return dp[d][n];
	ll &ret = dp[d][n];
	--n;
	ret += calc(d - 1, (n + 1) / 2);
	ret += calc(d - 1, n / 2);
	return ret;
}
int main() {
	freopen("C:/Users/ASUS/Downloads/C-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		scanf("%lld%lld", &n, &k);
		int d = 0;
		ll count = 0;
		while (true) {
			count += 1ll << d;
			if (k <= count)
				break;
			++d;
		}
		count -= 1ll << d;
		k -= count;
		ll l = 1, r = n, m, res = 0;
		while (l <= r) {
			m = (l + r) / 2;
			for (int i = 0; i <= d; ++i)
				dp[i].clear();
			len = m;
			if (calc(d, n) >= k) {
				res = m;
				l = m + 1;
			}else
				r = m - 1;
		}
		--res;
		printf(" %lld %lld\n", (res + 1) / 2, res / 2);
	}
	return 0;
}