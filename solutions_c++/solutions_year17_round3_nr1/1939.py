#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        int n, k;
        scanf("%d%d", &n, &k);
        bool bol[1005];
        long long r[1005], h[1005];
        for (int i = 0; i < n; i++) {
            bol[i] = false;
            scanf("%lld%lld", &r[i], &h[i]);
        }
        long long res = 0LL, mxsh = 0LL;
        for (; k > 0; k--) {
            int ai = -1;
            long long as = 0LL, ash = 0LL;
            for (int i = 0; i < n; i++) {
                if (bol[i]) {
                    continue;
                }
                long long sh, sv;
                sh = r[i] * r[i];
                sv = 2LL * r[i] * h[i];
                long long s = 0LL;
                if (mxsh < sh) {
                    s += sh - mxsh;
                }
                s += sv;
                if (as < s) {
                    ai = i;
                    as = s;
                    ash = sh;
                }
            }
            bol[ai] = true;
            res += as;
            mxsh = max(mxsh, ash);
        }
        printf("Case #%d: %.6lf\n", tc, M_PI * (double) res);
    }
    return 0;
}
