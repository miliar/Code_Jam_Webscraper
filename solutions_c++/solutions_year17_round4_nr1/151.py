#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <map>

void updmax(int &x, int y) {
	x = std::max(x, y);
}

int solve() {
	static int dp[101][101][101][101][4];
	int n, p;
	std::cin >> n >> p;

	std::fill_n((int *)dp, sizeof(dp) / sizeof(int), -10000);

	std::vector<int> c(4);
	for (int i = 0; i < n; i++) {
		int t;
		std::cin >> t;
		c[t % p]++;
	}

	dp[0][0][0][0][0] = 0;
	for (int i = 0; i <= c[0]; i++) {
		for (int j = 0; j <= c[1]; j++) {
			for (int k = 0; k <= c[2]; k++) {
				for (int l = 0; l <= c[3]; l++) {
					for (int m = 0; m < p; m++) {
						if (dp[i][j][k][l][m] < 0) {
							continue;
						}
						if (i + 1 <= c[0]) updmax(dp[i + 1][j][k][l][(m + p - 0) % p], dp[i][j][k][l][m] + (m == 0));
						if (j + 1 <= c[1]) {
							updmax(dp[i][j + 1][k][l][(m + p - 1) % p], dp[i][j][k][l][m] + (m == 0));
						}
						if (k + 1 <= c[2]) updmax(dp[i][j][k + 1][l][(m + p - 2) % p], dp[i][j][k][l][m] + (m == 0));
						if (l + 1 <= c[3]) updmax(dp[i][j][k][l + 1][(m + p - 3) % p], dp[i][j][k][l][m] + (m == 0));
					}
				}
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < p; i++) {
		updmax(ans, dp[c[0]][c[1]][c[2]][c[3]][i]);
	}
	return ans;
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		int ans = solve();
		printf("Case #%d: %d\n", i + 1, ans);
	}
}
