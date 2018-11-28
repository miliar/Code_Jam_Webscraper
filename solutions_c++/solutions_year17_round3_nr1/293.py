#include <bits/stdc++.h>

using namespace std;

const int dd = 1007;

typedef long long ll;

ll dp[dd][dd];
ll p[dd][dd];

const double pi = atan2(1, 1) * 4;

int main() {
    int t;
    scanf("%d", &t);

    for (int test = 0; test < t; test++) {
        int n, k;
        scanf("%d %d", &n, &k);

        vector<pair<ll, ll> > A(n + 1);

        for (int i = 1; i <= n; i++) {
            scanf("%lld %lld", &A[i].first, &A[i].second);
        }

        sort(A.begin(), A.end());

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = p[i - 1][j - 1] + 2 * A[j].first * A[j].second;
            }

            for (int j = 1; j <= n; j++) {
                p[i][j] = max(dp[i][j], p[i][j - 1]);
            }
        }
        ll ans = 0;
        for (int j = 1; j <= n; j++)
            ans = max(ans, dp[k][j] + A[j].first * A[j].first);
        printf("Case #%d: %.9f\n", test + 1, ans * pi);
    }

    return 0;
}
