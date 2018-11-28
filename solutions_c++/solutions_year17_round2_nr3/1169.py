#include <iostream>
#include <algorithm>
using namespace std;
using LL = long long;
const double INF = 1e18;
const int SIZE = 101;
LL e[SIZE], s[SIZE], d[SIZE];

double solve(int n) {
    double dp[n][n];
    LL p[n];
    for (int i=0; i<n; ++i)
        p[i] = i ? p[i - 1] + d[i] : 0;
    for (int i=0; i<n; ++i)
        fill(dp[i], dp[i] + n, 0);
    for (int i=1; i<n; ++i) {
        dp[i][i] = INF;
        for (int j=0; j<i; ++j) {
            bool endure = p[i] - p[j] <= e[j];
            double time = dp[i - 1][j] + 1.0 * d[i] / s[j];
            dp[i][j] = endure ? time : INF; 
            dp[i][i] = min(dp[i][i], dp[i][j]);
        }
    }
    return dp[n - 1][n - 1];
}

int main() {
    int T; cin >> T;
    for (int t=1; t<=T; ++t) {
        int n, q; cin >> n >> q;
        // Assert q = 1
        for (int i=0; i<n; ++i)
            cin >> e[i] >> s[i];
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                LL x; cin >> x;
                if (i + 1 == j) d[j] = x;
            }
        }
        int _; cin >> _ >> _;
        printf("Case #%d: %.9lf\n", t, solve(n));
    }
}
