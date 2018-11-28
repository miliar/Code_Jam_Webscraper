#include <bits/stdc++.h>

#define ld long double

using namespace std;

const ld eps = 1e-9;
const ld pi = acos(-1.0);

void solve() {
    int n, k;
    scanf("%d %d", &n, &k);
    ld u;
    scanf("%Lf", &u);
    vector<ld> p(n);
    for (int i = 0; i < n; ++i)
        scanf("%Lf", &p[i]);
    sort(p.begin(), p.end());
    ld ans = 0;
    for (int iter = 0; iter <= (int)1e5; ++iter) {
        ld s = (ld)iter / 1e5;
        ld prob = 1.0;
        ld cur = u;
        for (int i = 0; i < n; ++i) {
            if (p[i] < s) {
                ld np = p[i] + min(cur, s - p[i]);
                prob *= np;
                cur -= min(cur, s - p[i]);
            } else {
                prob *= p[i];
            }
        }
        ans = max(ans, prob);
    }
    printf("%.6Lf\n", ans);
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        fprintf(stderr, "Case #%d is working\n", i);

        printf("Case #%d: ", i);
        solve();

        fprintf(stderr, "Case #%d is done\n", i);
    }


    return 0;
}