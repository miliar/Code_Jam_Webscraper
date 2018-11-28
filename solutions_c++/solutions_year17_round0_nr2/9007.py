#include <stdio.h>
#include <math.h>

long long solve(long long n) {
    long long o = n;
    int p = n % 10;
    int c = 0;
    int d;
    int max = p;
    int maxc = c;
    n /= 10;
    while(n > 0) {
        c++;
        d = n % 10;
        if (d > p) {
            max = d;
            maxc = c;
        }
        p = d;
        n /= 10;
    }
    if (maxc == 0) return o;
    //printf("maxc is %d, max is %d\n", maxc, max);
    long long t1 = (long long)pow(10, maxc);
    long long next = o / t1 * t1 - 1;
    return solve(next);
}

int main() {
    int T;
    scanf("%d\n", &T);
    for(int i = 0; i < T; i++) {
        long long N;
        scanf("%lld\n", &N);
        printf("Case #%d: %lld\n", i + 1, solve(N));
    }
    return 0;
}
