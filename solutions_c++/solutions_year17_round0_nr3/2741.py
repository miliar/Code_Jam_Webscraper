#include <stdio.h>

int main() {
    int tn, cn;
    for (scanf("%d", &tn), cn = 1; cn <= tn; cn++) {
        long long n, k;
        scanf("%lld%lld", &n, &k);
        while (k > 2) {
            if (k % 2 == 0) {
                k /= 2;
                n /= 2;
            } else {
                k = k / 2;
                n = (n - 1) / 2;
            }
        }
        if (k == 2) {
            n /= 2;
        }
        printf("Case #%d: %lld %lld\n", cn, n / 2, (n - 1) / 2);
    }
    return 0;
}
