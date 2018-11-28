#include <bits/stdc++.h>
#define TR(c, it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define FOR(i, a, b) for(int i = (a), _b = (b); i < _b; ++i)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; --i)
#define FORE(i, a, b) for(int i = (a), _b = (b); i <= _b; ++i)
#define SZ(c) (int) (c).size()

using namespace std;
const double PI = acos(-1);
const double eps = 1e-6;
const int N = 55;

int n, k;
double p;
double a[N];

int main() {
    //freopen("A.inp", "r", stdin);
    //freopen("A.out", "w", stdout);
    //ios::sync_with_stdio(false); cin.tie(NULL);
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        scanf("%d %d", &n, &k);
        scanf("%lf", &p);
        FOR(i, 0, n) cin >> a[i];
        double ll = 0.0, rr = 1.0;
        while ((ll + eps) < rr) {
            double mm = (ll + rr) / 2.0;
            double ss = 0;
            for (int i = 0; i < n; ++i)
                if (a[i] < mm) ss += mm - a[i];
            if (ss <= p) ll = mm;
            else rr = mm;
        }
        double ss = 0;
        for (int i = 0; i < n; ++i)
                if (a[i] < ll) ss += (ll - a[i]), a[i] = ll;
        ss = p - ss;
        ss /= n;
        for (int i = 0; i < n; ++i) a[i] += ss;
        double ans = 1.0;
        for (int i = 0; i < n; ++i) ans = ans * a[i];
        printf("Case #%d: %.08lf\n", test, ans);
    }
    return 0;
}


