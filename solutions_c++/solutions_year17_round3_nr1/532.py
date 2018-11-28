#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

const double PI = acos(-1.0);
int n, k;
typedef std::pair<double, double> Pii;
Pii a[1000+10], b[1000+10];

bool cmp(Pii x, Pii y)
{
    return x.second > y.second;
}

int main()
{
    int T_T, t_t;
    scanf("%d", &T_T);
    for (t_t = 1; t_t <= T_T; ++t_t) {
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; ++i) {
            int r, h;
            scanf("%d%d", &r, &h);
            a[i].first = PI * r * r;
            a[i].second = PI * 2 * r * h;
        }
        std::sort(a+1, a+1+n);
        double res = 0;
        for (int i = k; i <= n; ++i) {
            double tmp = a[i].first + a[i].second;
            for (int j = 1; j < i; ++j) {
                b[j] = a[j];
            }
            std::sort(b+1, b+i, cmp);
            for (int j = 1; j <= k-1; ++j) {
                tmp += b[j].second;
            }
            res = std::max(res, tmp);
        }
        printf("Case #%d: %f\n", t_t, res);
    }
}
