#include <bits/stdc++.h>

using namespace std;

int main() {

    // freopen("C-large.in", "r", stdin);
    // freopen("C-large.out", "w", stdout);

    int T, k = 0; long long N, K, TW, C;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%lld%lld", &N, &K);
        TW = 1; C = 1;
        while(C < K) {
            N -= TW;
            TW <<= 1;
            C += TW;
        }
        if (TW > 1) {
            C -= TW;
            if (K - C <= N % TW) {
                N = N / TW + 1;
            } else {
                N = N / TW;
            }
        }
        printf("%lld %lld\n", N / 2, N - N / 2 - 1);
    }

    return 0;
}
