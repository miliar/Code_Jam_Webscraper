#define _USE_MATH_DEFINES
#include<bits/stdc++.h>
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3f
#define EPS (1e-10)
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef long long ll;
typedef pair<int, int>P;

int a[100], b[100], c[100], d[100];
int dp[1441][721][2];
bool A[1441], B[1441];
int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		int n, m; scanf("%d%d", &n, &m);
		rep(i, n) {
			scanf("%d%d", &a[i], &b[i]);
			for (int j = a[i]; j < b[i]; j++)A[j] = 1;
		}
		rep(i, m) {
			scanf("%d%d", &c[i], &d[i]);
			for (int j = c[i]; j < d[i]; j++)B[j] = 1;
		}
		memset(dp, 0x3f, sizeof(dp));
		dp[0][0][0] = 0;
		rep(i, 1440)rep(j, i + 1)rep(k, 2) {
			if (dp[i][j][k] == INF)continue;
			if (j < 720 && !A[i]) {
				if (k == 0)
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][k]);
				else
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][k] + 1);
			}
			if (i - j < 720 && !B[i]) {
				if (k == 1)
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][k]);
				else
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][k] + 1);
			}
		}
		int ans = dp[1440][720][0];
		memset(dp, 0x3f, sizeof(dp));
		dp[0][0][1] = 0;
		rep(i, 1440)rep(j, i + 1)rep(k, 2) {
			if (dp[i][j][k] == INF)continue;
			if (j < 720 && !A[i]) {
				if (k == 0)
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][k]);
				else
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][k] + 1);
			}
			if (i - j < 720 && !B[i]) {
				if (k == 1)
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][k]);
				else
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][k] + 1);
			}
		}
		ans = min(ans, dp[1440][720][1]);
		printf("Case #%d: %d\n", cnt, ans);
	}
}