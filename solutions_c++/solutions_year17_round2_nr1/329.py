#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int kases;
int d, n, k[2000], s[2000];

int main() {
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d", &d, &n);
        double time = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &k[i], &s[i]);
            time = max(time, (double)(d - k[i]) / s[i]);
        }
        printf("Case #%d: %.6f\n", kase, d / time);
    }
    return 0;
}
