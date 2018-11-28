#include <bits/stdc++.h>
#define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
using namespace std;

typedef long long ll;
typedef double ld;

int main() {
    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        int n, k;
        scanf("%d %d", &n, &k);

        ld x;
        scanf("%lf", &x);
        vector<ld> p(n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &p[i]);
        }

        sort(p.begin(), p.end());

        ld ans = 0;

        for (int q = 1; q <= n; q++) {

            ld l = 0, r = 1;
            for (int it = 0; it < 100; it++) {
                ld m = (l + r) / 2;

                ld s = 0;
                for (int i = 0; i < q; i++) s += max(0.0, m - p[i]);
                if (s <= x) l = m;
                else r = m;
            }

            ld w = 1;
            for (int i = 0; i < q; i++)
                w *= max(p[i], l);
            for (int i = q; i < n; i++)
                w *= p[i];
            ans = max(ans, w);


        }
        printf("Case #%d: %.10f\n", test, ans);

    }
    return 0;
}
