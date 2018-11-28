#include <algorithm>
#include <cstdio>
#include <cstring>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        long long d, n;
        scanf("%lld %lld", &d, &n);
        double mt = -1;
        for (int i = 0; i < n; ++i) {
            long long k, s;
            scanf("%lld %lld", &k, &s);
            if (mt == -1) {
                mt = (double) (d - k) / s;
            }
            mt = std::max(mt, (double) (d - k) / s);
        }
        
        printf("Case #%d: %.7lf\n", t, (double) d / mt);
    }
    return 0;
}
