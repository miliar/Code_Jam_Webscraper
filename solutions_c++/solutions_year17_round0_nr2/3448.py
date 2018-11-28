#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define long long long
int T;
long n, m, dp[21][10], s[21], dig;
int main() {
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase) {
		scanf("%lld", &n);
		m = n;
		memset(dp, 0, sizeof dp);
		for (dig = 1; n; ++dig, n /= 10) s[dig] = n;
		--dig;
		reverse(s + 1, s + dig + 1);
		for (int i = 1; i <= dig; ++i) for (int j = 0; j <= 9; ++j) {
			for (int k = 0; k <= j; ++k) {
				long newv = dp[i - 1][k] * 10 + j;
				if (newv <= s[i]) dp[i][j] = max(dp[i][j], newv);
			}
		}
		long ans = 0;
		for (int j = 0; j <= 9; ++j) ans = max(ans, dp[dig][j]);
		printf("Case #%d: %lld\n", kase, ans);
	}
	return 0;
}
