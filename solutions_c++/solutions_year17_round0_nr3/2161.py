#include <cstdio>

typedef unsigned long long ullint;

static inline ullint nextpow2(ullint x)
{
    x |= (x >> 1);
    x |= (x >> 2);
    x |= (x >> 4);
    x |= (x >> 8);
    x |= (x >> 16);
    x |= (x >> 32);
    return x+1;
}

int main()
{
    int t;

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        ullint n, k;
        ullint up, y, z;    /// y - dmax, z - dmin

        scanf("%llu %llu", &n, &k);
        up = nextpow2(k);
        y = (n-k+up/2)/up;
        z = (n-k)/up;
        printf("Case #%d: %llu %llu\n", tc, y, z);
    }
}
