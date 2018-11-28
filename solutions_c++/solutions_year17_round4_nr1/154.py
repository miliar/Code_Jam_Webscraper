#include<cstdio>
int n, m;
int a[110];
int d[10];
int dp[110][110][110];
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d%d", &n, &m);
		int ans = 0;
		for (int i = 0; i < 5; i++) {
			d[i] = 0;
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			d[a[i] % m]++;
		}
		for (int i = 0; i <= d[1]; i++) {
			for (int j = 0; j <= d[2]; j++) {
				for (int k = 0; k <= d[3]; k++) {
					dp[i][j][k] = 0;
				}
			}
		}
		for (int i = 0; i <= d[1]; i++) {
			for (int j = 0; j <= d[2]; j++) {
				for (int k = 0; k <= d[3]; k++) {
					int t = dp[i][j][k];
					if ((i * 1 + j * 2 + k * 3) % m == 0) {
						t++;
					}
					if (dp[i + 1][j][k] < t)dp[i + 1][j][k] = t;
					if (dp[i][j + 1][k] < t)dp[i][j + 1][k] = t;
					if (dp[i][j][k + 1] < t)dp[i][j][k + 1] = t;
				}
			}
		}
		ans = d[0] + dp[d[1]][d[2]][d[3]];
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
