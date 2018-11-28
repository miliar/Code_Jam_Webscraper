#include <bits/stdc++.h>

using namespace std;

bool A[2000], B[2000];

int dp[730][730][2];

const int inf = 0x3f3f3f3f;

inline void up(int &x, int v) {
    x = min(x, v);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n, m;
        scanf("%d%d", &n, &m);
        memset(A, 0, sizeof(A));
        memset(B, 0, sizeof(B));
        for(int i = 0; i < n; ++ i) {
            int x, y;
            scanf("%d%d", &x, &y);
            for(int j = x; j < y; ++ j)
                A[j] = true;
        }
        for(int i = 0; i < m; ++ i) {
            int l, r;
            scanf("%d%d", &l, &r);
            for(int j = l; j < r; ++ j)
                B[j] = true;
        }
        int ans = 0x3f3f3f3f;
        if(!A[0]) {
            memset(dp, 0x3f, sizeof(dp));
            dp[1][0][0] = 0;
            for(int i = 0; i <= 720; ++ i) {
                for(int j = 0; j <= 720; ++ j) {
                    int t = i + j;
                    if(t >= 1440)
                        continue;
                    if(dp[i][j][0] != inf) {
                        if(!A[t] && i < 720)
                            up(dp[i + 1][j][0], dp[i][j][0]);
                        if(!B[t] && j < 720)
                            up(dp[i][j + 1][1], dp[i][j][0] + 1);
                    }
                    if(dp[i][j][1] != inf) {
                        if(!A[t] && i < 720)
                            up(dp[i + 1][j][0], dp[i][j][1] + 1);
                        if(!B[t] && j < 720)
                            up(dp[i][j + 1][1], dp[i][j][1]);
                    }
                }
            }
            ans = min(dp[720][720][0], dp[720][720][1] + 1);
        }
        if(!B[0]) {
            memset(dp, 0x3f, sizeof(dp));
            dp[0][1][1] = 0;
            for(int i = 0; i <= 720; ++ i) {
                for(int j = 0; j <= 720; ++ j) {
                    int t = i + j;
                    if(t >= 1440)
                        continue;
                    if(dp[i][j][0] != inf) {
                        if(!A[t] && i < 720)
                            up(dp[i + 1][j][0], dp[i][j][0]);
                        if(!B[t] && j < 720)
                            up(dp[i][j + 1][1], dp[i][j][0] + 1);
                    }
                    if(dp[i][j][1] != inf) {
                        if(!A[t] && i < 720)
                            up(dp[i + 1][j][0], dp[i][j][1] + 1);
                        if(!B[t] && j < 720)
                            up(dp[i][j + 1][1], dp[i][j][1]);
                    }
                }
            }
            ans = min(ans, dp[720][720][0] + 1);
            ans = min(ans, dp[720][720][1]);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
