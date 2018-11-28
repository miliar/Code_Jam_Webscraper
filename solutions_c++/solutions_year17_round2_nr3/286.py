#include <bits/stdc++.h>
using namespace std;
const int N = 105;
typedef long long ll;

int t, tc, n;
int q, e[N], s[N], d[N][N];

ll dist[N][N];
double dp[N][N];

int main() {
    cout.precision(10);
    cout << fixed;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> t;
    while (t--) {
        cin >> n;
        cout << "Case #" << ++tc << ": ";
        // small
        cin >> q;
        for (int i = 1; i <= n; ++i)
            cin >> e[i] >> s[i];
        for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) {
            cin >> d[i][j];
            if (i == j) dist[i][j] =0;
            else if (d[i][j] == -1) dist[i][j] = LLONG_MAX;
            else dist[i][j] = d[i][j];
        }
        for (int k = 1; k <= n; ++k)
        for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            if (dist[i][k] != LLONG_MAX && dist[k][j] != LLONG_MAX)
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j]);
        for (int u = 1; u <= n; ++u) {
            for (int v = 1; v <= n; ++v) {
                if (u == v) dp[u][v] = 0;
                else {
                    if (dist[u][v] <= e[u])
                        dp[u][v] = 1.0 * dist[u][v] / s[u];
                    else
                        dp[u][v] = HUGE_VAL;
                }
            }
        }
        for (int k = 1; k <= n; ++k)
        for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) {
            if (dp[i][k] != HUGE_VAL && dp[k][j] != HUGE_VAL)
                dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j]);
        }
        while (q-- > 0) {
            int u, v;
            cin >> u >> v;
            cout << ' ' << dp[u][v];
        }
        cout << '\n';
    }
}
