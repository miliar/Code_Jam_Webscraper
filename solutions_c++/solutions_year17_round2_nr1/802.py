#include <bits/stdc++.h>

using namespace std;

int main() {

    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);

    int T, k = 0, D, N, S, K; double max_t, t;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d", &D, &N);
        max_t = 0;
        while(N--) {
            scanf("%d%d", &K, &S);
            t = (double)1.0 * (D - K) / S;
            if (max_t < t)
                max_t = t;
        }
        printf("%.6f\n", (double)1.0 * D / max_t);
    }

    return 0;
}
