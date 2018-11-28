#include <cstdio>
#include <algorithm>
using std::max;

void prog() {
    long double maxtime = 0;
    long double v, dis, D;
    int n, d;
    scanf("%d%d", &d, &n);
    D = d;
    for(int i = 0, pos, vi; i < n; ++i) {
        scanf("%d%d", &pos, &vi);
        dis = D - pos;
        v = vi;
        maxtime = max(maxtime, dis / v);
    }
    D /= maxtime;
    printf("%.8lf\n", (double) D);
}

int main() {
    int _t;
    scanf("%d", &_t);
    for(int i = 1; i <= _t; ++i) {
        printf("Case #%d: ", i);
        fprintf(stderr, "test %d... ", i);
        prog();
        fprintf(stderr, "OK\n");
    }
}