#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        int n, d;
        double mx = 0;
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            int x, y;
            cin >> x >> y;
            mx = max(mx, 1.0 * (d - x) / y);
        }
        cout << "Case #" << T << ": ";
        cout << fixed << setprecision(6) << 1.0 * d / mx << '\n';
    }
}
