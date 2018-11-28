#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;
long minattacks(long a, long h, long b) {
    long ans = (h - 1) / a + 1;
    if(b > 0)
        for(long i = 1; h > a + (i - 1) * b; i++)
            ans = min(ans, i + (h - 1) / (a + i * b) + 1);
    return ans;
}
long minmoves1(long a, long h0, long h, long x) {
    if(x == 1)
        return 1;
    if(a >= h0 && a >= h - a)
        return 1L << 50;
    if(a < h && x == 2)
        return 2;
    if(a >= h - a)
        return 1L << 50;
    long step = 0;
    while(x > 1) {
        if(a >= h0) {
            // must heal
            step++;
            h0 = h - a;
        } else {
            step++;
            x--;
            h0 -= a;
        }
    }
    return step + 1;
}
long minmoves(long a, long h, long d, long x) {
    if(x == 1)
        return 1;
    if(a - d >= h)
        return -1;
    if(a < h && x == 2)
        return 2;
    if(2 * a - 3 * d >= h)
        return -2;
    long ans = minmoves1(a, h, h, x);
    if(d) {
        long a1 = a, h0 = h, step = 0;
        while(a1 > 0) {
            if(a1 - d >= h0) {
                step++;
                h0 = h - a1;
            }
            if(a1 - d >= h0)
                break;
            step++;
            a1 -= d;
            if(a1 < 0)
                a1 = 0;
            h0 -= a1;
            ans = min(ans, step + minmoves1(a1, h0, h, x));
        }
    }
    return ans;
}
long solve(long h1, long a1, long h2, long a2, long b, long d) {
    return minmoves(a2, h1, d, minattacks(a1, h2, b));
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        long h1, a1, h2, a2, b, d;
        scanf("%ld %ld %ld %ld %ld %ld", &h1, &a1, &h2, &a2, &b, &d);
        long ans = solve(h1, a1, h2, a2, b, d);
#if 1
        if(ans >= 1 && ans <= 1L << 40)
#else
        if(true)
#endif
            printf("Case #%d: %ld\n", i, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
