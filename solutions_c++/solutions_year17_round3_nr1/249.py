#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    int T;

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int n, k;
        cin >> n >> k;
        vector<pair<long long, long long>> p(n);
        vector<long long> v(n);
        for (int i = 0; i < n; ++i) {
            cin >> p[i].first >> p[i].second;
        }
        sort(p.begin(), p.end());
        long long best = 0;
        for (int i = n - 1; i >= k - 1; --i) {
            for (int j = 0; j < i; ++j) {
                v[j] = p[j].first * p[j].second;
            }
            sort(v.begin(), v.begin() + i);
            long long cur = p[i].first * p[i].first + 2 * p[i].first * p[i].second;
            for (int j = i - 1; j >= i - k + 1; --j)
                cur += 2 * v[j];
            best = max(best, cur);
        }
        cout << "Case #" << t << ": " << fixed << setprecision(18) << acos(-1.) * best << "\n";
    }

    return 0;
}
