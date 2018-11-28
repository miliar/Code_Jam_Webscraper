#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;
const int maxn = 1010;

struct H {
    int k, s;
    bool operator<(const H& rhs) const { return k < rhs.k; }
} h[maxn];

int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int d, n;
        scanf("%d%d", &d, &n);
        for (int i = 1; i <= n; i++) scanf("%d%d", &h[i].k, &h[i].s);
        double v = 1e18;
        for (int i = 1; i <= n; i++) {
            v = min(v, 1.0 * h[i].s * d / (d - h[i].k));
        }
        printf("Case #%d: %.6lf\n", ca, v);
    }
    return 0;
}