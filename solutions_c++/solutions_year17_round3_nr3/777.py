#include <bits/stdc++.h>

#define sz(a) (int)a.size()

using namespace std;

const double EPS = 1e-9;

int main() {
    freopen("text.in", "r", stdin);
    freopen("text.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int tn = 0; tn < tests; tn++) {
        printf("Case #%d: ", tn + 1);
        int n, k;
        scanf("%d%d", &n, &k);
        double u;
        scanf("%lf", &u);
        cerr << u << '\n';
        vector<double> p(n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &p[i]);
        }
        double l = 0, r = 1;
        for (int it = 0; it < 100; it++) {
            double m = (l + r) / 2;
            double s = 0;
            for (int i = 0; i < n; i++) {
                if (p[i] >= m + EPS) {
                    continue;
                }
                s += m - p[i];
            }
            if (s <= u) {
                l = m;
            } else {
                r = m;
            }
        }
        double ans = 1.0;
        for (int i = 0; i < n; i++) {
            ans *= max(p[i], l);
        }
        printf("%.10f\n", ans);
    }
    return 0;
}
