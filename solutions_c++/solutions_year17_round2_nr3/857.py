#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 207;
const long double INF = 1e18;

int tc, n, q;
long long e[MAX_N], s[MAX_N], dist[MAX_N];
long double dp[MAX_N][MAX_N];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout.precision(20);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> q;
        for (int i = 0; i < n; i++) {
            cin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long long tmp;
                cin >> tmp;
                if (i + 1 == j) {
                    dist[j] = dist[i] + tmp;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = INF;
            }
        }
        dp[0][0] = 0;
        int tmp;
        cin >> tmp >> tmp;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j <= i; j++) {
                if (dist[i + 1] - dist[j] <= e[j]) {
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + (long double) (dist[i + 1] - dist[i]) / (long double) s[j]);
                }
                if (dist[i + 1] - dist[i] <= e[i]) {
                    dp[i + 1][i] = min(dp[i + 1][i], dp[i][j] + (long double) (dist[i + 1] - dist[i]) / (long double) s[i]);
                }
            }
        }
        long double ans = INF;
        for (int i = 0; i < n; i++) {
            ans = min(ans, dp[n - 1][i]);
        }
        cout << (double) ans << "\n";
    }
}
