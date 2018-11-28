#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAXN = 105;

#define debug(...) fprintf(stderr, __VA_ARGS__)
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()

void setmax (char &a, char b) {
	if (a < b) {
		a = b;
	}
}

int N, P, cnt[4];
char dp[MAXN][MAXN][MAXN][MAXN][4];

int go() {
	scanf("%d %d", &N, &P);
	memset(cnt, 0, sizeof(cnt));
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int x;
		scanf("%d", &x);
		cnt[x % P]++;
		sum += x;
	}
	sum %= P;

	for (int i = 0; i <= cnt[0]; i++) {
		for (int j = 0; j <= cnt[1]; j++) {
			for (int k = 0; k <= cnt[2]; k++) {
				for (int m = 0; m <= cnt[3]; m++) {
					for (int n = 0; n < 4; n++) {
						dp[i][j][k][m][n] = -1;
					}
				}
			}
		}
	}

	dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]][0] = 1;
	for (int i = cnt[0]; i >= 0; i--) {
		for (int j = cnt[1]; j >= 0; j--) {
			for (int k = cnt[2]; k >= 0; k--) {
				for (int m = cnt[3]; m >= 0; m--) {
					for (int n = 0; n < 4; n++) {
						char pdp = dp[i][j][k][m][n];
						if (pdp == -1) {
							continue;
						}

						if (i) {
							setmax(dp[i - 1][j][k][m][n], pdp + (n % P == 0));
						}
						if (j) {
							setmax(dp[i][j - 1][k][m][(n + 1) % P], pdp + ((n + 1) % P == 0));
						}
						if (k) {
							setmax(dp[i][j][k - 1][m][(n + 2) % P], pdp + ((n + 2) % P == 0));
						}
						if (m) {
							setmax(dp[i][j][k][m - 1][(n + 3) % P], pdp + ((n + 3) % P == 0));
						}
					}
				}
			}
		}
	}

	char ans = 0;
	for (int i = 0; i < 4; i++) {
		setmax(ans, dp[0][0][0][0][i]);
	}
	ans -= (sum == 0);
	return ans;
}

int main() {
	int ncas;
	scanf("%d", &ncas);
	for (int cas = 1; cas <= ncas; cas++) {
		printf("Case #%d: %d\n", cas, go());
	}
}
