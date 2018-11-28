#include <bits/stdc++.h>

#define sz(a) (int)a.size()

using namespace std;

const double pi = 3.141592653589793;

int main() {
    freopen("text.in", "r", stdin);
    freopen("text.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int tn = 0; tn < tests; tn++) {
        printf("Case #%d: ", tn + 1);
        int n, k;
        scanf("%d%d", &n, &k);
        vector<pair<int, int>> pancakes(n);
        for (int i = 0; i < n; i++) {
            int r, h;
            scanf("%d%d", &r, &h);
            pancakes.emplace_back(r, h);
        }
        sort(pancakes.begin(), pancakes.end());
        vector<vector<long long>> dp(sz(pancakes) + 1, vector<long long>(k + 1, -1e18));
        dp[0][0] = 0;
        for (int i = 1; i <= sz(pancakes); i++) {
            dp[i][0] = 0;
            for (int j = 1; j <= k; j++) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + pancakes[i - 1].first * 1LL * pancakes[i - 1].second);
            }
        }
        long long answer = 0;
        for (int i = 1; i <= sz(pancakes); i++) {
            answer = max(answer, dp[i - 1][k - 1] * 2 + pancakes[i - 1].first * 1LL * pancakes[i - 1].second * 2 + pancakes[i - 1].first * 1LL * pancakes[i - 1].first);
        }
        printf("%.10f\n", answer * pi);
    }
    return 0;
}
