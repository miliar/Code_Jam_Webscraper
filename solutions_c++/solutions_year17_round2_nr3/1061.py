#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int test_number) {
    int n, q;
    cin >> n >> q;
    vector<ll> e(n), s(n);
    vector<vector<ll>> d(n, vector<ll>(n));
    vector<ll> u(q), v(q);

    for (int i=0; i<n; ++i)
        cin >> e[i] >> s[i];

    for (int i=0; i<n; ++i)
        for (int j=0; j<n; ++j)
            cin >> d[i][j];

    for (int i=0; i<q; ++i)
        cin >> u[i] >> v[i];


    vector<ll> prefix_sum(n, 0);
    for (int i=1; i<n; ++i)
        prefix_sum[i] = prefix_sum[i-1] + d[i-1][i];
    vector<vector<double>> dp(n, vector<double>(n, 1e18));
    dp[1][0] = double(prefix_sum[1]) / double(s[0]);

    for (int i=1; i<n-1; ++i) {
        for (int j=0; j<i; ++j) {
            if (prefix_sum[i + 1] - prefix_sum[j] <= e[j])
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + double(d[i][i+1]) / double(s[j]));

            if (d[i][i+1] <= e[i])
                dp[i+1][i] = min(dp[i+1][i], dp[i][j] + double(d[i][i+1]) / double(s[i]));
        }
    }

    double ans = 1e18;
    for (int i=0; i<n; ++i)
        ans = min(ans, dp[n-1][i]);

    printf("Case #%d: %.9f\n", test_number, ans);
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
        solve(t);


    return 0;
}
