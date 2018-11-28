#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100;
int test, n, q, u, v;
double e[MAXN+2], s[MAXN+2], d[MAXN+2][MAXN+2], sum[MAXN+2], dp[MAXN+2][MAXN+2];

double dist(int x, int y) {
    return sum[y] - sum[x];
}

int main() {
    scanf("%d", &test);

    for (int tt = 1; tt <= test; ++tt) {
        scanf("%d %d", &n, &q);

        for (int i = 1; i <= n; ++i) {
            scanf("%lf %lf", e+i, s+i);
        }

        for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            scanf("%lf", d[i]+j);

        while (q --> 0) {
            scanf("%d %d", &u, &v);
        }

        for (int i = 2; i <= n; ++i) {
            sum[i] = sum[i-1] + d[i-1][i];
        }

        dp[1][0] = 0;

        for (int i = 2; i <= n; ++i) {
            dp[i][0] = 2e18;
            for (int j = 1; j < i-1; ++j) {
                if (e[j] < dist(j, i)) {
                    dp[i][j] = -1;
                    continue;
                }
                if (dp[i-1][j] < 0) {
                    dp[i][j] = -1;
                } else {
                    dp[i][j] = dp[i-1][j] + d[i-1][i] / s[j];
                    dp[i][0] = min(dp[i][0], dp[i][j]);
                }
            }
            dp[i][i-1] = dp[i-1][0] + d[i-1][i] / s[i-1];
            dp[i][0] = min(dp[i][0], dp[i][i-1]);
        }

        printf("Case #%d: %.8lf\n", tt, dp[n][0]);
    }
    return 0;
}
