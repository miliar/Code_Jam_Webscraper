#include <stdio.h>

#define MAXCIFRE 20

int calc_cifre(long long N) {
    int c = 0;
    while (N > 0) {
        c++;
        N /= 10;
    }
    return c;
}

long long N;
int T, C;
int cifre[MAXCIFRE];
long long count = 0;
long long last = 0;

void dp (int index, int limit) {
    if (index >= C) {
        long long converted = 0;
        for (int i = 0; i < C; i++) {
            converted = converted*10 + cifre[i];
        }
        if (converted > 0 && converted <= N) {
            //printf("%lld\n", converted);
            if (last < converted) {
                last = converted;
                count++;
            }
        }
        return;
    }
    for (int i = 9; i >= limit; i--) {
        cifre[index] = i;
        dp(index+1, i);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &T);
    int i = 0;
    while (T-- > 0) {
        scanf("%lld", &N);
        C = calc_cifre(N);
        last = 0;
        dp(0, 0);
        printf("Case #%d: %lld\n", ++i, last);
    }

    return 0;
}
