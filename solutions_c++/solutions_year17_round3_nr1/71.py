#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
pair<double, double> a[1024];
double dp[1024][1024];
double pi = M_PI;

void read() {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf", &a[i].first, &a[i].second);
    }
}

void solve() {
    sort(a, a + n);
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            dp[i][j] = -1e100;
        }
    }

    dp[n - 1][1] = pi * a[n - 1].first * a[n - 1].second * 2;
    for (int i = n - 2; i >= 0; i--) {
        dp[i][1] = pi * a[i].first * a[i].second * 2;
        for (int j = 2; j <= k; j++) {
            for (int d = i + 1; d < n; d++) {
                dp[i][j] = max(dp[i][j], dp[d][j - 1] + pi * a[i].first * a[i].second * 2 + pi * (a[d].first * a[d].first - a[i].first * a[i].first ));
            }
        }
    }

    double ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, dp[i][k] + pi * a[i].first * a[i].first);
    }
    printf ("%lf\n", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

