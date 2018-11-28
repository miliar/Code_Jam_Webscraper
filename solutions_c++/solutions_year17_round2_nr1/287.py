#include <bits/stdc++.h>
using namespace std;

const int N = (int) 1e3 + 10;
int n, d, k[N], s[N];

int main() {
    freopen("A.inp", "r", stdin);
    freopen("A.out", "w", stdout);
    int TC; cin >> TC;
    for (int testID = 1; testID <= TC; ++testID) {
        cin >> d >> n;
        for (int i = 1; i <= n; ++i) cin >> k[i] >> s[i];

        double l = 1e-9, r = 1e18, f = -1;
        for (int times = 0; times < 100; ++times) {
            double m = (l + r) / 2;
            double t = d / m;
            bool flag = true;
            for (int i = 1; i <= n; ++i)
                flag &= k[i] + s[i] * t > d;
            if (flag) {
                f = m;
                l = m;
            }
            else r = m;
        }
        cout << "Case #" << testID << ": " << fixed << setprecision(10) << f << endl;
    }
    return 0;
}
