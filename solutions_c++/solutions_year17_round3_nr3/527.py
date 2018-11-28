#include <cstdio>
#include <iostream>

typedef long long lint;
int n , k;
double m , p[100];


int main()
{
    int T, t;
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        scanf("%d%d", &n, &k);
        scanf("%lf", &m);
        for (int i = 1; i <= n; ++i) {
            scanf("%lf", p+i);
        }
        std::sort(p+1, p+1+n);
        double res = 1;
        double tmp;
        p[n + 1] = 1;
        for (int i = 1; i <= n+1; ++i) {
            tmp = 0;
            for (int j = 1; j <= i-1; ++j) {
                tmp += p[i] - p[j];
            }
            tmp = std::min(tmp, m);
            m -= tmp;
            for (int j = 1; j <= i-1; ++j) {
                p[j] += tmp / (i-1);
            }
        }
        for (int i = 1; i <= n; ++i) {
            res *= p[i];
        }
        printf("%f\n", res);
    }
}
