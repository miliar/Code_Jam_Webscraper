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
        double u;
        cin >> u;
        vector<double> p(n);
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }
        sort(p.begin(), p.end());
        for (int i = 0; i < n; ++i) {
            double diff = (i == n - 1 ? 1.0 : p[i + 1]) - p[i];
            if (diff * (i + 1) <= u) {
                for (int j = 0; j <= i; ++j) {
                    p[j] += diff;
                }
                u -= diff * (i + 1);
            }
            else {
                for (int j = 0; j <= i; ++j)
                    p[j] += u / (i + 1);
                break;
            }
        }
        double ans = 1.0;
        for (double prob: p)
            ans *= prob;
        cout << "Case #" << t << ": " << fixed << setprecision(18) << ans << "\n";
    }

    return 0;
}
