#include <bits/stdc++.h>

using namespace std;

// int dp[4][4][111][111];

int main() {
	int t, n, p, x;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%d %d", &n, &p);
		// memset(dp, -1, sizeof dp);

		int cnt[10] = { };
		for (int i = 0; i < n; ++i) {
			scanf("%d", &x);
			cnt[x % p]++;
		}

		int ans = cnt[0];// + calc(0, 1, p);
		if (p == 2) {
			ans += (cnt[1] + 1) >> 1;
		} else {
			int x = min(cnt[1], cnt[2]);
			ans += x;
			cnt[1] -= x;
			cnt[2] -= x;
			ans += (cnt[1] + 2) / 3;
			ans += (cnt[2] + 2) / 3;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}