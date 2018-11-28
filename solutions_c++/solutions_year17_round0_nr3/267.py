#include <cstdio>

#define N 64

int T;
long long n, k, t;

long long f(long long n, long long k) {
    long long a = 1, b = 0;
    do {
        if (k <= a)
            return n;
        if (k <= a + b)
            return n - 1;
        k -= a + b;
        if (n&1) {
            a = a + a + b;
            n /= 2;
        } else {
            b = a + b + b;
            n /= 2;
        }
    } while (1);
}

int main() {
    scanf("%d", &T);
    for (int r = 1; r <= T; ++r) {
        printf("Case #%d: ", r);
        scanf("%lld%lld", &n, &k);
        t = f(n, k);
        printf("%lld %lld\n", t >> 1, (t - 1) >> 1);
    }
    return 0;
}
