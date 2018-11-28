#include <bits/stdc++.h>

using namespace std;

const double EPS = 1e-9;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        long long d;
        int n;
        cin >> d >> n;
        vector<pair<long long, long long>> k(n);
        for (int i = 0; i < n; ++i) {
            cin >> k[i].first >> k[i].second;
        }
        sort(k.begin(), k.end());
        vector<int> p(n);
        p[n - 1] = n;

        for (int i = n - 2; i >= 0; --i) {
            p[i] = n;
            for (int j = i + 1; j < n; ++j) {
                if (k[j].second >= k[i].second)
                    continue;
                long long d1 = k[j].first - k[i].first;
                long long d2 = k[i].second - k[j].second;
                long long d3 = d - k[j].first;
                long long d4 = k[j].second;
                if (p[j] < n) {
                    d3 = k[p[j]].first - k[j].first;
                    d4 = k[j].second - k[p[j]].second;
                }
                if (d1 * d4 < d2 * d3) {
                    p[i] = j;
                    break;
                }
            }
        }

        double ans = 1e13;
        for (int i = 0; i < n; ++i) {
            long long d1 = k[i].first;
            long long d3 = d - k[i].first;
            long long d4 = k[i].second;
            if (p[i] < n) {
                d3 = k[p[i]].first - k[i].first;
                d4 = k[i].second - k[p[i]].second;
            }
            ans = min(ans, (d1 * d4 + 0.0) / d3 + k[i].second);
        }
        cout << "Case #" << t << ": " << fixed << setprecision(9) << ans << "\n";
    }

    return 0;
}
