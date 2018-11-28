#include <bits/stdc++.h>
using namespace std;

int k[1010], s[1010];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int d, n;
        scanf("%d%d", &d, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &k[i], &s[i]);
        }
        double maxT = 0.0;
        for (int i = 0; i < n; i++) {
            double curT = (d - k[i]) * 1.0 / s[i];
            maxT = max(maxT, curT);
        }
        double res = d / maxT;
        printf("Case #%d: %.20f\n", cas, res);
        fprintf(stderr, "Case #%d: %.20f\n", cas, res);
    }
    return 0;
}