#include <bits/stdc++.h>
using namespace std;

const double INF = 1e18;
const int N = 105;

int t, n, q;
double a[N], b[N];
double f[N][N], g[N][N];

int main() {
    ios::sync_with_stdio(false);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        cin >> n >> q;
        for (int i = 1; i <= n; ++i) cin >> a[i] >> b[i];
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) f[i][j] = g[i][j] = INF;
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) {
            cin >> f[i][j]; if (f[i][j] == -1) f[i][j] = INF;
        }
        for (int i = 1; i <= n; ++i) f[i][i] = g[i][i] = 0;
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) for (int k = 1; k <= n; ++k) {
            f[j][k] = min(f[j][k], f[j][i] + f[i][k]);
        }
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) {
            if (a[i] < f[i][j]) continue;
            g[i][j] = f[i][j] / b[i];
        }
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) for (int k = 1; k <= n; ++k) {
            g[j][k] = min(g[j][k], g[j][i] + g[i][k]);
        }
        cout << "Case #" << T << ": ";
        for (int i = 1; i <= q; ++i) {
            int s, t; cin >> s >> t;
            cout << fixed << setprecision(6) << g[s][t] << ' ';
        }
        cout << '\n';
    }
}
