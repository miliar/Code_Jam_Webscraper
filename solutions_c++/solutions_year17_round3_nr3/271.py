#include <bits/stdc++.h>

using namespace std;

const int MX_SZ = 100 + 5;
const long double EPS = 1e-12;

void solve(int t) {
    int n, k;
    cin >> n >> k;
    long double p;
    cin >> p;
    vector<long double> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long double l = 0, r = 2;
    while (l + EPS < r) {
        long double m = (l + r) / 2;
        long double c_sum = 0;
        // cout << m << endl;
        for (int i = 0; i < n; ++i) {
            if (a[i] < m) {
                c_sum += m - a[i];
            }
        }
        if (c_sum < p) {
            l = m;
        } else {
            r = m;
        }
    }

    long double ans = 1;
    for (int i = 0; i < n; ++i) {
       ans *= max(a[i], l);
    }
    cout << "Case #" << t << ": " << fixed << setprecision(64) << ans << endl;
}

int main() {
    freopen("C-small-1-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
