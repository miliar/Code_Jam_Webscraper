#include <cstdio>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        long long n, k, mx, mn;
        scanf("%lld%lld", &n, &k);
        for (; k > 0LL; k >>= 1) {
            mx = n >> 1;
            mn = (n - 1LL) >> 1;
            n = (k & 1LL) ? mn : mx;
        }
        printf("Case #%d: %lld %lld\n", tc, mx, mn);
    }
}
