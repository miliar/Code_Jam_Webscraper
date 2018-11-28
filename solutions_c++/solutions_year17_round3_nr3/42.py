#include <algorithm>
#include <cstdio>

const int N = 50;

double p[N + 1];

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        int n;
        double u;
        scanf("%d%*d%lf", &n, &u);
        for (int i = 0; i < n; ++ i) {
            scanf("%lf", p + i);
        }
        std::sort(p, p + n);
        p[n] = 1;
        double result = 0.;
        double sum = 0.;
        for (int i = 0; i < n; ++ i) {
            sum += p[i];
            double left = u - (p[i] * (i + 1) - sum);
            if (left >= 0) {
                double now = std::min(p[i] + left / (i + 1), 1.0);
                double pd = 1.0;
                for (int j = 0; j < n; ++ j) {
                    if (j <= i) {
                        pd *= now;
                    } else {
                        pd *= p[j];
                    }
                }
                result = std::max(result, pd);
            }
        }
        printf("Case #%d: %.8f\n", t, result);
    }
}
