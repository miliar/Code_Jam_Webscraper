#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

const double pi = M_PI;
double max(double a, double b) {
    return (a>b)?a:b;
}

int main() {
    int T;
    long long int rs[1001], hs[1001];
    double aa[1001], rr[1001];
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        int n, k;
        scanf("%d%d", &n, &k);
        long long int r, h;
        for (int i = 0; i < n; i++) {
            scanf("%lld%lld", &r, &h);
            aa[i] = 2.0*pi*r*h;
            rr[i] = pi*r*r;
        }
        double ans = 0.0;
        double base = 0.0;
        for (int i = 0; i < n; i++) {
            base = rr[i]+aa[i];
            std::vector<double> V;
            for (int j = 0; j < n; j++) {
                if (j != i)
                    V.push_back(aa[j]);
            }
            std::sort(V.begin(), V.end());
            int len = V.size();
            for (int j = 0; j < k-1; j++) {
                base += V[len-1-j];
            }
            ans = max(ans, base);
        }
        printf("Case #%d: %.9lf\n", tt, ans);
    }

    return 0;
}
