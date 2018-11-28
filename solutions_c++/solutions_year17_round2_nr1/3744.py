#include<stdio.h>

int main() {
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++) {
        int D, N;
        scanf("%d%d", &D, &N);
        double s = 0;
        for (int i = 0; i < N; i++) {
            int K, S;
            scanf("%d%d", &K, &S);
            double s0 = 1.0 * K * S / (D - K) + S;
            if (s == 0 || s0 < s) {
                s = s0;
            }
        }
        printf("Case #%d: %.6f\n", t, s);
    }
}
