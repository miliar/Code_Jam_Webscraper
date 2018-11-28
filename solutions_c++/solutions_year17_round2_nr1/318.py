#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int T, D, N, k, s;

int main() {
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &D, &N);
        long double longest = 0.0;
        for (int i = 0; i < N; ++i) {
            scanf("%d %d", &k, &s);
            long double need = (D - k) / (long double) s;
            longest = max(need, longest);
        }
        long double answer = D / longest;
        printf("Case #%d: %0.9Lf\n", t, answer);
    }

    return 0;
}
