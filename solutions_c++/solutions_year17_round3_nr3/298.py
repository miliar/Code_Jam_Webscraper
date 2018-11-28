#include <bits/stdc++.h>
#define MAXN 1123

using namespace std;

double g[MAXN];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int N, K;
        scanf("%d%d", &N, &K);
        double xx;
        scanf("%lf", &xx);
        for (int i = 0; i < N; ++i) {
            scanf("%lf", &g[i]);
        }
        sort(g, g + N);
        double ans = 0.0;
        double sum = 0;
        for (int i = 0; i < N; ++i) {
            sum += g[i];
            double tmp = (sum + xx) / (i + 1);
            if (tmp >= g[i]) {
                double tmpAns = 1.0;
                for (int j = 0; j <= i; ++j) {
                    tmpAns *= tmp;
                }
                for (int j = i + 1; j < N; ++j) {
                    tmpAns *= g[j];
                }
                ans = max(ans, tmpAns);
            }
        }
        printf("Case #%d: %.10lf\n", ca, ans);
    }
    return 0;
}