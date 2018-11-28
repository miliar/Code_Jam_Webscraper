#include <stdio.h>

int main()
{
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        long long n;
        scanf("%lld", &n);
        long long x = 0;
        long long pw[18] = {1};
        for (int i = 1; i < 18; ++ i)
            pw[i] = pw[i - 1] * 10;
        for (int pos = 17, last = 0; pos >= 0; -- pos) {
            for (int digit = 9; digit >= last; -- digit) {
                long long tmp = 0;
                for (int i = 0; i <= pos; ++ i)
                    tmp += digit * pw[i];
                if (x + tmp <= n) {
                    x += pw[pos] * digit;
                    last = digit;
                    break;
                }
            }
        }
        printf("Case #%d: %lld\n", ca, x);
    }
}
