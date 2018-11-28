#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    long long T, tI, h0, a0, h1, a1, h2, a2, h3, a3, b, d, t, m, i, j, k;
    bool lc, p;
    scanf("%lld", &T);
    for (tI = 0; tI < T; tI++) {
        m = -1;
        scanf("%lld %lld %lld %lld %lld %lld", &h0, &a0, &h1, &a1, &b, &d);
        for (i = 0; i <= (d ? a1 / d + (a1 % d > 0) : 0); i++) for (j = 0; j <= (b ? ((h1 - a0) / b + ((h1 - a0) / b > 0)) : 0); j++) {
            t = 0;
            lc = 0;
            p = 1;
            h2 = h0;
            a2 = a0;
            h3 = h1;
            a3 = a1;
            for (k = 0; k < i; t++) {
                if (h2 <= a3 - d) {
                    if (lc) {p = 0; break;}
                    h2 = h0;
                    lc = 1;
                } else {
                    k++;
                    a3 -= d;
                    lc = 0;
                }
                h2 -= a3;
                if (h2 <= 0) {p = 0; break;}
            }
            if (!p) continue;
            for (k = 0; k < j; t++) {
                if (h2 <= a3) {
                    if (lc) {p = 0; break;}
                    h2 = h0;
                    lc = 1;
                } else {
                    k++;
                    a2 += b;
                    lc = 0;
                }
                h2 -= a3;
                if (h2 <= 0) {p = 0; break;}
            }
            if (!p) continue;
            for (; h3 > 0; t++) {
                if (h3 <= a2) {h3 -= a2; continue;}
                if (h2 <= a3) {
                    if (lc) {p = 0; break;}
                    h2 = h0;
                    lc = 1;
                } else {
                    h3 -= a2;
                    lc = 0;
                }
                h2 -= a3;
                if (h2 <= 0) {p = 0; break;}
            }
            if (!p) continue;
            m = (m > -1) ? min(m, t) : t;
        }
        printf("Case #%lld: ", tI + 1);
        (m > -1) ? printf("%lld\n", m) : printf("IMPOSSIBLE\n");
    }
    return 0;
}
