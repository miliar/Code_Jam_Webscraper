#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;

const long double inf = 1e18 + 7;
const long double eps = 1e-18;



int main() {
ios_base::sync_with_stdio(0);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    double pi = (double)2 * acos(0);

    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, k;
        cin >> n >> k;
        vector<pair<double, double> > dt;
        for (int i = 0; i < n; ++i) {
            double r, h;
            cin >> r >> h;
            dt.push_back({r, h});
        }
        sort(dt.rbegin(), dt.rend());
        double ans = 0;
        for (int s = 0; s < n - k + 1; ++s) {
            vector<vector<double> > dp(n, vector<double> (k + 1, 0));
            double th = 0;
            dp[s][1] = dt[s].second * dt[s].first * (double)2 * pi;
            for (int i = s + 1; i < n; ++i) {
                dp[i][1] = dt[i].second * dt[i].first * (ld)2 * pi;
                for (int j = s + 1; j < i; ++j) {
                    for (int kk = 1; kk < k - 1; ++kk) {
                        dp[i][kk + 1] = max(dp[i][kk + 1], dp[j][kk] + dp[i][1]);
                    }
                }
                th = max(th, dp[i][k - 1]);
            }
            double nans = pi * dt[s].first * dt[s].first + th + dp[s][1];
            ans = max(ans, nans);
        }
        cout.precision(10);
        cout << "Case #" << tt + 1 << ": " << fixed << ans << endl;
    }
    return 0;
}