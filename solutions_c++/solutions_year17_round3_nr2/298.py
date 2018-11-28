#include <bits/stdc++.h>
#define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
using namespace std;

typedef long long ll;

const int dd = 24 * 60 + 7;

int U[3][2 * dd];

int dp1[dd][2], dp2[dd][2];

int main() {
    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        int n, m;
        scanf("%d %d", &n, &m);

        memset(U[0], 0, sizeof(U[0]));
        memset(U[1], 0, sizeof(U[1]));

        for (int i = 0; i < n; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            fill(U[0] + a, U[0] + b, 1);
        }

        for (int i = 0; i < m; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            fill(U[1] + a, U[1] + b, 1);
        }

        int ans = (int)1e9;

        for (int w = 0; w < 2; w++) {

            for (int i = 0; i <= 24 * 60; i++) {
                dp1[i][0] = dp1[i][1] = dp2[i][0] = dp2[i][1] = (int)1e9;
            }
            dp1[0][w] = 0;

            for (int t = 0; t < 24 * 60; t++) {
                for (int i = 0; i <= t; i++) {

                    for (int who = 0; who < 2; who++) {
                        if (!U[who][t]) {
                            //if (t < 5)err("go to (%d, %d, %d) = %d\n", t + 1, i + who, who, dp1[i][who]);
                            dp2[i + who][who] = min(dp2[i + who][who], dp1[i][who]);
                        }

                        if (!U[who ^ 1][t]) {
                            dp2[i + (who ^ 1)][who ^ 1] = min(dp2[i + (who ^ 1)][who ^ 1], dp1[i][who] + 1);
                        }
                    }

                }

                for (int i = 0; i <= t + 1; i++) {
                    //err("dp[%d][%d] = (%d, %d)\n", t, i, dp1[i][0], dp1[i][1]);
                    dp1[i][0] = dp2[i][0];
                    dp1[i][1] = dp2[i][1];
                    dp2[i][0] = dp2[i][1] = (int)1e9;
                }
            }
            ans = min(ans, min(dp1[720][w], dp1[720][w ^ 1] + 1));
        }
        printf("Case #%d: %d\n", test, ans);
    }
}
