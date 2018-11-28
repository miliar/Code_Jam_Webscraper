#include <bits/stdc++.h>

using namespace std;

const double pi = acos(-1.0);

int r[1005], h[1005], id[1005];

long long dp[1005][1005];

bool cmp(int x, int y) {
    return r[x] > r[y];
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 1; i <= n; ++ i)
            scanf("%d%d", r + i, h + i), id[i] = i;
        sort(id + 1, id + 1 + n, cmp);
        for(int i = 1; i <= n; ++ i) {
            int x = id[i];
            dp[i][1] = 1ll * r[x] * r[x] + 2ll * r[x] * h[x];
        }
        for(int j = 2; j <= m; ++ j) {
            long long mx = -(1ll << 60);
            for(int i = 1; i < j; ++ i) {
                dp[i][j] = -(1ll << 60);
                mx = max(mx, dp[i][j - 1]);
            }
            for(int i = j; i <= n; ++ i) {
                int x = id[i];
                dp[i][j] = mx + 2ll * r[x] * h[x];
                mx = max(mx, dp[i][j - 1]);
            }
        }
        long long ans = 0;
        for(int i = m; i <= n; ++ i)
            ans = max(ans, dp[i][m]);
        printf("Case #%d: %.20f\n", cas, ans * pi);
    }
    return 0;
}
