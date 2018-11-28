#include <bits/stdc++.h>
using namespace std;

int dp[110][110][110][4];

void ck(int &x, int y) {
    if (x == -1 || x < y) {
        x = y;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int a[4] = {0, 0, 0, 0};
        int n, P;
        scanf("%d%d", &n, &P);
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            a[x % P]++;
        }
        memset(dp, -1, sizeof(dp));
        int tot = a[1] + a[2] + a[3];
        dp[a[1]][a[2]][a[3]][0] = a[0];
        for (int i = tot; i > 0; i--) {
            int p[4];
            for (p[1] = 0; p[1] <= i; p[1]++) {
                for (p[2] = 0; p[1] + p[2] <= i; p[2]++) {
                    p[3] = i - p[1] - p[2];
                    for (int k = 0; k < P; k++) {
                        if (dp[p[1]][p[2]][p[3]][k] == -1) {
                            continue;
                        }
                        int cur = dp[p[1]][p[2]][p[3]][k];
                        for (int l = 1; l <= 3; l++) {
                            if (p[l] > 0) {
                                p[l]--;
                                ck(dp[p[1]][p[2]][p[3]][(k + l) % P], cur + (k == 0 ? 1 : 0));
                                p[l]++;
                            }
                        }
                    }
                }
            }
        }
        int res = dp[0][0][0][0];
        for (int i = 0; i < P; i++) {
            ck(res, dp[0][0][0][i]);
        }
        printf("Case #%d: %d\n", cas, res);
        fprintf(stderr, "Case #%d: %d\n", cas, res);
    }
    return 0;
}