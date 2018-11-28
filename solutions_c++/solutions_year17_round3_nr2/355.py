#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int K = 1000;
int dp[2][2][2000][2000];
int vis[2000];

void update(int &a, int k) {
	if (a == -1) {
		a = k;
	}
	a = min(a, k);
}

int main() {
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ca++);
		int ac, aj;
		scanf("%d%d", &ac, &aj);
		memset(vis, 0, sizeof(vis));
		for (int i = 0; i < ac; i++) {
			int p, q;
			scanf("%d%d", &p, &q);
			for (int j = p + 1; j <= q; j++) vis[j] = 2;
		}
		for (int i = 0; i < aj; i++) {
			int p, q;
			scanf("%d%d", &p, &q);
			for (int j = p + 1; j <= q; j++) vis[j] = 1;
		}
		memset(dp, -1, sizeof(dp));
		if (vis[1] == 2) {
			dp[1][1][1][K - 1] = 0;
		} else if (vis[1] == 1) {
			dp[0][0][1][K + 1] = 0;
		} else {
			dp[0][0][1][K + 1] = dp[1][1][1][K - 1] = 0;
		}
		int ans = 10000;
		for (int i = 2; i <= 1440; i++) {
			for (int k = K - 720; k <= K + 720; k++) {
				if (vis[i] != 2) {
					for (int p = 0; p < 2; p++) {
						if (dp[p][0][i - 1][k - 1] != -1) update(dp[p][0][i][k], dp[p][0][i - 1][k - 1]);
						if (dp[p][1][i - 1][k - 1] != -1) update(dp[p][0][i][k], dp[p][1][i - 1][k - 1] + 1);
						if (i == 1440 && k == K && dp[p][0][i][k] != -1) {
							if (0 == p) {
								update(ans, dp[p][0][i][k]);
							} else {
								update(ans, dp[p][0][i][k] + 1);
							}
						}
					}
				}
				if (vis[i] != 1) {
					for (int p = 0; p < 2; p++) {
						if (dp[p][0][i - 1][k + 1] != -1) update(dp[p][1][i][k], dp[p][0][i - 1][k + 1] + 1);
						if (dp[p][1][i - 1][k + 1] != -1) update(dp[p][1][i][k], dp[p][1][i - 1][k + 1]);
						if (i == 1440 && k == K && dp[p][1][i][k] != -1) {
							if (1 == p) {
								update(ans, dp[p][1][i][k]);
							} else {
								update(ans, dp[p][1][i][k] + 1);
							}
						}
					}
				}
			}
		}
		printf("%d\n", ans);
	}
}
