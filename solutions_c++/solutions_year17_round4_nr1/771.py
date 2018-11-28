/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const int MN = 101;

int dp[MN][MN][MN][3];

void maxi(int &a, int b) {
	if (a < b) a = b;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int n, p, i, j, k, l;
		scanf("%d %d", &n, &p);
		int rem[4] = {};
		for (i = 0; i < n; i++ ) {
			int x;
			scanf("%d", &x);
			rem[p * ((x + p - 1) / p) - x]++;
		}

		memset(dp, 0, sizeof dp);

		for (i = 0; i <= rem[1]; i++) {
			for (j = 0; j <= rem[2]; j++) {
				for (k = 0; k <= rem[3]; k++) {
					if (i == rem[1] && j == rem[2] && k == rem[3]) continue;
					for (l = 0; l < 4; l++) {
						int add = (l == 0);
						if (i < rem[1]) maxi(dp[i + 1][j][k][(l + 1) % p], dp[i][j][k][l] + add);

						if (j < rem[2]) maxi(dp[i][j + 1][k][(l + 2) % p], dp[i][j][k][l] + add);

						if (k < rem[3]) maxi(dp[i][j][k + 1][(l + 3) % p], dp[i][j][k][l] + add);
					}
				}
			}
		}

		int ans = 0;
		for (i = 0; i < 4; i++) ans = max(ans, dp[rem[1]][rem[2]][rem[3]][i]);

		printf("Case #%d: %d\n", K, ans + rem[0]);
		K++;
	}
	return 0;
}
