#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
const ld PI = acos(-1.);


int main() {
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll n, k;
        cin >> n >> k;
        vector<pair<ll, ll>> pan(n, pair<ll, ll>());
        vector<vector<ll>> dp(n, vector<ll>(k, 0));
        for (int i = 0; i < n; ++i) {
            cin >> pan[i].first >> pan[i].second;
        }
        sort(pan.rbegin(), pan.rend());
        dp[0][0] = pan[0].first * (pan[0].first + 2 * pan[0].second);
        for (ll i = 1; i < n; ++i) {
            for (ll j = min(i, k - 1); j > -1; --j) {
                dp[i][j] = dp[i - 1][j];
                if (j == 0) {
                    dp[i][j] = max(dp[i][j], pan[i].first * (pan[i].first + 2 * pan[i].second));
                    continue;
                }
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2 * pan[i].first * pan[i].second);
            }
        }
        cout.precision(10);
        cout << fixed << "Case #" << t << ": " << PI * dp[n-1][k-1] << endl;
    }
    return 0;
}