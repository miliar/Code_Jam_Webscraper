#include <stdio.h>
#include <algorithm>

int main()
{
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        int D, N;
        scanf("%d%d", &D, &N);
        double t = -1;
        for (int i = 0; i < N; ++ i) {
            int K, S;
            scanf("%d%d", &K, &S);
            t = std::max(t, (D - K) * 1. / S);
        }
        printf("Case #%d: %.6f\n", ca, D / t);
    }
}
