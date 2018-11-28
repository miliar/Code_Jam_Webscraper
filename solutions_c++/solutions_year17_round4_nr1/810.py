#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int n, p;
int g[111];
int dp[111][111][111];
int c0, c1, c2, c3;

inline void update(int &des, int src) {
	if (des == -1) {
		des = src;
	} else {
		des = max(des, src);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &p);
		c0 = 0;
		c1 = 0;
		c2 = 0;
		c3 = 0;
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &g[i]);
			g[i] %= p;
			c0 += (g[i] == 0);
			c1 += (g[i] == 1);
			c2 += (g[i] == 2);
			c3 += (g[i] == 3);
		}
		memset(dp, -1, sizeof(dp));
		dp[0][0][0] = 0;
		for (int i = 0; i <= c1; ++ i) {
			for (int j = 0; j <= c2; ++ j) {
				for (int k = 0; k <= c3; ++ k) {
					if (dp[i][j][k] != -1) {
						int t = (i * 1 + j * 2 + k * 3) % p;
						int a = (t == 0);
						if (i < c1) {
							update(dp[i + 1][j][k], dp[i][j][k] + a);
						}
						if (j < c2) {
							update(dp[i][j + 1][k], dp[i][j][k] + a);
						}
						if (k < c3) {
							update(dp[i][j][k + 1], dp[i][j][k] + a);
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", kase, c0 + dp[c1][c2][c3]);
	}
	return 0;
}
