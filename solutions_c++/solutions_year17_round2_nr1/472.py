#include <bits/stdc++.h>

using namespace std;

void solve(int test) {
    int D, n;
    cin >> D >> n;
    double ans = 1e18;
    for (int i = 0; i < n; ++i) {
        int x, v;
        cin >> x >> v;
        ans = min(ans, 1.0 * D * v / (D - x));
    }
    cout << "Case #" << test << ": " << ans << '\n';
}

signed main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false); cin.tie(0);
    cout << fixed; cout.precision(12);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
