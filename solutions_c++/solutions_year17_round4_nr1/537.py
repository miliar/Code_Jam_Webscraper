#include <bits/stdc++.h>

using namespace std;

int cnt[4];

int dp[101][101][101][4];

inline void up(int &x, int v) {
    x = max(x, v);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        memset(cnt, 0, sizeof(cnt));
        int n, P;
        scanf("%d%d", &n, &P);
        int ans = 0;
        for (int x, i = 0; i < n; ++ i) {
            scanf("%d", &x);
            x %= P;
            if (x == 0) {
                ++ ans;
                continue;
            }
            ++ cnt[x];
        }
        memset(dp, -0x3f, sizeof(dp));
        dp[0][0][0][0] = 0;
        for (int i = 0; i <= cnt[1]; ++ i) {
            for (int j = 0; j <= cnt[2]; ++ j) {
                for (int k = 0; k <= cnt[3]; ++ k) {
                    for (int v = 0; v < P; ++ v) {
                        if (dp[i][j][k][v] == -1)
                            continue;
                        if (i < cnt[1]) {
                            int nv = (v + 1) % P;
                            up(dp[i + 1][j][k][nv], dp[i][j][k][v] + (v == 0));
                        }
                        if (j < cnt[2]) {
                            int nv = (v + 2) % P;
                            up(dp[i][j + 1][k][nv], dp[i][j][k][v] + (v == 0));
                        }
                        if (k < cnt[3]) {
                            int nv = (v + 3) % P;
                            up(dp[i][j][k + 1][nv], dp[i][j][k][v] + (v == 0));
                        }
                    }
                }
            }
        }
        int ret = 0;
        for (int i = 0; i < P; ++ i)
            ret = max(ret, dp[cnt[1]][cnt[2]][cnt[3]][i]);
        printf("Case #%d: %d\n", cas, ans + ret);
    }
    return 0;
}
