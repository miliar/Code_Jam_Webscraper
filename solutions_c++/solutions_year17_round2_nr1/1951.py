#include <cstdio>
#include <cstdlib>

double _max(double a, double b) {
    return (a>b)?a:b;
}
int main() {
    int T, D, N;
    int m, s;
    double max_t;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        max_t = 0.0;
        scanf("%d%d", &D, &N);
        for (int i = 0; i < N; i++) {
            int cur_s, cur_m;
            scanf("%d%d", &cur_m, &cur_s);
            double cur_t = (D-cur_m)/(double)cur_s;
            max_t = _max(cur_t, max_t);
        }
        printf("Case #%d: %.6lf\n", tt, D/max_t);
    }
    return 0;
}
