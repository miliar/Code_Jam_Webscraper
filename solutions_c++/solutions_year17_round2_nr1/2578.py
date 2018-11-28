#include <cstdio>

int main(void) {
    int T, N, cas = 1;
    double max_t, t, D, K, S;

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
        scanf("%lf %d", &D, &N);
        max_t = -1;
        for(int i = 0; i < N; ++i) {
            scanf("%lf %lf", &K, &S);
            t = (D-K)/S;
            if(max_t < t) max_t = t;
        }

        printf("Case #%d: %lf\n", cas, D/max_t);
    }


    return 0;
}
