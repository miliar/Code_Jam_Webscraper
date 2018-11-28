#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>
#include <iostream>
#include <set>
#include <math.h>

#define long long long

using namespace std;

const double pi = acos(-1.0);
int n, k;
pair<int, int> p[1010];
double dp[1010][1010];

void solve(int t) {
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; ++i) {
        scanf("%d%d", &p[i].first, &p[i].second);
        p[i].first = -p[i].first;
    }
    sort(p + 1, p + n + 1);
    double ans = 0;
    for (int i = 1; i <= n; ++i) {
        p[i].first = -p[i].first;
        for (int j = 1; j <= i; ++j) {
            dp[i][j] = dp[i - 1][j];
            double cur = dp[i - 1][j - 1];
            cur += 2 * pi * p[i].first * p[i].second;
            if (j == 1) {
                cur += pi * p[i].first * p[i].first;
            }
            dp[i][j] = max(dp[i][j], cur);
            if (j == k) {
                ans = max(ans, dp[i][j]);
            }
        }
    }
    printf("Case #%d: %.10g\n", t, ans);
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int i = 1; i <= tests; ++i) {
        solve(i);
    }

    return 0;
}
