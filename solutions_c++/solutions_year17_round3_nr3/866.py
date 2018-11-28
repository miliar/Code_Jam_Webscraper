#include <bits/stdc++.h>
using namespace std;

const int maxn = 50 + 5;
double p[maxn], u;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t, kase = 0; cin >> t; while (t--) {
        cout << "Case #" << ++kase << ": ";
        int n, k; cin >> n >> k >> u;
        for (int i = 0; i < n; ++i) cin >> p[i];
        p[n] = 1.0;
        sort(p, p + n);
        int ind = 0;
        while (u > 0.0 && ind < n) {
            double add = (p[ind + 1] - p[ind]) * (ind + 1);
            if (add <= u) {
                for (int j = 0; j <= ind; ++j) p[j] = p[ind + 1];
                u -= add;
            } else {
                double ok = u / (double)(ind + 1);
                for (int j = 0; j <= ind; ++j) p[j] += ok;
                u = 0.0;
            }
            ++ind;
        }
        double ans = 1.0;
        for (int i = 0; i < n; ++i) ans *= p[i];
        cout << fixed << setprecision(9) << ans << '\n';
    }
    return 0;
}
