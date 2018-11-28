#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back

const int N = 1010;
int k[N], s[N];

bool check(double v, int d, int n) {
    double time = d / v;
    for (int i = 1; i <= n; ++i) {
        if ((d - k[i]) + 1e-7 > time * s[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, tt;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt) {
        int d, n;
        scanf("%d%d", &d, &n);
//        cout << d << ' ' << n << "\n";
        for (int i = 1; i <= n; ++i) {
            scanf("%d%d", k + i, s + i);
//            cout << k[i] << ' ' << s[i] << "\n";
        }
//        cout << "\n";
        double l = 0, r = 1e+16;
        for (int j = 0; j < 200; ++j) {
            double mid = (l + r) / 2;
            if (check(mid, d, n)) {
                l = mid;
            } else {
                r = mid;
            }
        }
        printf("Case #%d: %.10f\n", tt, l);
    }
    return 0;
}
