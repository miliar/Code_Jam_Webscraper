#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 24*60 + 5;

int n, m;
int a[MAXN][2];
int dp[MAXN][MAXN][2][2];

void read() {
    int q, w;
    memset(a, 0, sizeof a);

    scanf ("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &q, &w);
        while (q < w) {
            a[q][0] = 1;
            ++q;
        }
    }
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &q, &w);
        while (q < w) {
            a[q][1] = 1;
            ++q;
        }
    }
}

void solve() {
    for (int i = 0; i < MAXN; i++) {
        for (int j = 0; j < MAXN; j++) {
            for (int k = 0; k < 2; k++) {
                for (int d = 0; d < 2; d++) {
                    dp[i][j][k][d] = 100000;
                }
            }
        }
    }


    if (!a[0][0]) dp[0][1][0][0] = 0;
    if (!a[0][1]) dp[0][0][1][1] = 0;

    for (int i = 1; i < 24 * 60; i++) {
        for (int j = 0; j <= i + 1; j++) {
            for (int k = 0; k < 2; k++) {
                if (a[i][k]) {
                    continue;
                }

                for (int d = 0; d < 2; d++) {
                    if (j == 0 && k == 0) continue;

                    int p = j;
                    if (k == 0) --p;

                    int val1 = dp[i - 1][p][k][d];
                    int val2 = dp[i - 1][p][k ^ 1][d];

                    dp[i][j][k][d] = min(dp[i][j][k][d], val1);
                    dp[i][j][k][d] = min(dp[i][j][k][d], val2 + 1);

                    //if (dp[i][j][k][d] < 50)printf ("%d %d %d %d   %d  %d %d\n", i ,j , k, d, dp[i][j][k][d], val1, val2);
                }
            }
        }
    }
    int ans = 1000000;
    //printf("%d\n", dp[24*60/2+100][1+100][0][1]);

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            int val = dp[24*60 - 1][24*60/2][i][j];
            //printf ("%d %d   %d\n", i, j, val);
            ans = min(ans, val + (i != j));
        }
    }
    printf ("%d\n", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

