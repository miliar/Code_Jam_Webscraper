#include <stdio.h>
#include <limits.h>

int main() {
    int t, d, n, kt, st;
    int ti, a;
    double nt, finish_time, result;
    scanf("%d", &t);
    for (ti = 1; ti <= t; ti++) {
        finish_time = 0;
        scanf("%d %d", &d, &n);
        printf("Case #%d: ", ti);
        for (a = 0; a < n; a++) {
            scanf("%d %d", &kt, &st);
            nt = ((double)d-kt)/st;
            if (nt > finish_time) finish_time = nt;
        }
        //if (finish_time == 0) result = 0;
        result = d/finish_time;
        printf("%f\n", result);
    }
    return 0;
}
