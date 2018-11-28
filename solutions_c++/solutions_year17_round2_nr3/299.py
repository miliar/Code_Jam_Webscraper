#include <cstdio>

using namespace std;

typedef long long ll;

const int MAXN = 104;
const ll  INF  = 1000LL * 1000LL * 1000LL * 1000LL;
const double DINF = 1e200;

int N;
ll dp[MAXN][MAXN];
double dp2[MAXN][MAXN];
int Dl[MAXN], Dv[MAXN];

int main() {
	int tc;
	scanf("%d", &tc);

	for (int t = 1; t <= tc; ++t) {
		int q;
		scanf("%d %d", &N, &q);
		for (int i = 1; i <= N; ++i) {
			scanf("%d %d", &Dl[i], &Dv[i]);
		}

		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				int x;
				scanf("%d", &x);
				if (i == j) dp[i][j] = 0;
				else if (x == -1) dp[i][j] = INF;
				else dp[i][j] = x;
			}
		}

		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				if (dp[j][i] == INF) continue;
				for (int k = 1; k <= N; ++k) {
					if (dp[j][i] + dp[i][k] < dp[j][k]) {
						dp[j][k] = dp[j][i] + dp[i][k];
					}
				}
			}
		}

		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				if (i == j) dp2[i][j] = 0;
				else if (dp[i][j] == INF) dp2[i][j] = DINF;
				else if (dp[i][j] > Dl[i]) dp2[i][j] = DINF;
				else dp2[i][j] = dp[i][j] / (double)Dv[i];
			}
		}

		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				if (dp2[j][i] == DINF) continue;
				for (int k = 1; k <= N; ++k) {
					if (dp2[j][i] + dp2[i][k] < dp2[j][k]) {
						dp2[j][k] = dp2[j][i] + dp2[i][k];
					}
				}
			}
		}

		printf("Case #%d:", t);
		for (int i = 1; i <= q; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			printf(" %.9f", dp2[x][y]);
		}
		puts("");
	}

	return 0;
}