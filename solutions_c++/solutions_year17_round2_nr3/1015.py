#define DEBUG
#define TXTOUT
#include<bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const double EPS = 1e-8;
const int M = 1e2 + 10;
int n, q;
int e[M];
int s[M];
int d[M][M];
struct Query {
    int u, v;
}query[M];
double dp[M];
double Solve() {
    for (int i = 1; i <= n; i++) {
        dp[i] = -1;
    }
    dp[1] = 0;
    for (int i = 1; i < n; i++) {
        int sum = 0;
        for (int j = i + 1; j <= n; j++) {
            sum += d[j - 1][j];
            if (sum > e[i]) break;
            double now = dp[i] + sum * 1.0 / s[i];
            if (dp[j] < 0) {
                dp[j] = now;
            } else {
                dp[j] = min(dp[j], now);
            }
        }
    }
    return dp[n];
}
int main() {
    #ifdef TXTOUT
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    #endif // TXTOUT
    int t, cas = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; i++) {
            scanf("%d%d", &e[i], &s[i]);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf("%d", &d[i][j]);
            }
        }
        for (int i = 0; i < q; i++) {
            scanf("%d%d", &query[i].u, &query[i].v);
        }
        printf("Case #%d: %.9f\n", cas++, Solve());
    }
    return 0;
}
