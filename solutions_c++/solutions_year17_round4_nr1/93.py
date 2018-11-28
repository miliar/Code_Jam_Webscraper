#include <bits/stdc++.h>
using namespace std;

int TC, N, P, A[105], sums[4], dp[105][105][105][4];

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; i++) scanf("%d", &A[i]);
		memset(sums, 0, sizeof(sums));
		for (int i = 0; i < N; i++) sums[A[i] % P]++;
		int ans = sums[0];
		memset(dp, -63, sizeof(dp));
		dp[0][0][0][0] = ans;
		for (int i = 0; i <= sums[1]; i++) {
			for (int j = 0; j <= sums[2]; j++) {
				for (int k = 0; k <= sums[3]; k++) {
					for (int l = 0; l < P; l++) {
						if (i > 0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i - 1][j][k][(l + P - 1) % P] + ((l + P - 1) % P == 0));
						if (j > 0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j - 1][k][(l + P - 2) % P] + ((l + P - 2) % P == 0));
						if (k > 0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k - 1][(l + P - 3) % P] + ((l + P - 3) % P == 0));
					}
				}
			}
		}
		int val = sums[1] * 1 + sums[2] * 2 + sums[3] * 3;
		val %= P;
		printf("Case #%d: %d\n", tc, dp[sums[1]][sums[2]][sums[3]][val]);
	}
}
