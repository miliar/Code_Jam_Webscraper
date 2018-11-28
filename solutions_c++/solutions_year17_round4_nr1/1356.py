#include <stdio.h>
#define MX 101
int mods[4];
int dp[MX][MX][MX][4];
int INF = 1000;
int max(int a, int b) {
	return a < b ? b : a;
}
int sol(int one, int two, int three, int offset, int P) {
	if (one < 0 || two < 0 || three < 0) return -INF;
	if (one == 0 && two == 0 && three == 0) return 0;
	int &res = dp[one][two][three][offset];
	if (res >= 0) return res;

	res = max(res, sol(one - 1, two, three, (offset + 1) % P, P) + (offset == 0)?1:0);
	res = max(res, sol(one, two - 1, three, (offset + 2) % P, P) + (offset == 0) ? 1 : 0);
	res = max(res, sol(one, two, three - 1, (offset + 3) % P, P) + (offset == 0) ? 1 : 0);
	printf("[%d][%d][%d][%d] = %d\n", one, two, three, offset, res);
	return res;
}
int solve() {
	int N, P; scanf("%d %d", &N, &P);
	for (int i = 0; i < MX; i++) {
		for (int j = 0; j < MX; j++) {
			for (int k = 0; k < MX; k++) {
				for (int l = 0; l < 4; l++) {
					dp[i][j][k][l] = -INF;
				}
			}
		}
	}
	dp[0][0][0][0] = 0;
	for (int i = 0; i < 4; i++) mods[i] = 0;

	for (int i = 0; i < N; i++) {
		int g; scanf("%d", &g);
		mods[g % P]++;
	}
	for (int i = 0; i <= mods[1]; i++) {
		for (int j = 0; j <= mods[2]; j++) {
			for (int k = 0; k <= mods[3]; k++) {
				for (int l = 0; l < P; l++) {
					if (i>0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i - 1][j][k][(l + P - 1) % P] + (l == 1));
					if (j>0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j-1][k][(l + P - 2) % P] + (l == 2));
					if (k>0) dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k-1][(l + P - 3) % P] + (l == 3));
				}
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < P; i++) {
		int now = mods[0] + dp[mods[1]][mods[2]][mods[3]][i];
		if (ans < now) ans = now;
	}
	
	return ans;
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %d\n", tc, solve());
	}
}