#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        int n;
        double d, mx = 0;
        scanf("%lf%d", &d, &n);
        for (int i = 0; i < n; i++) {
            double k, s;
            scanf("%lf%lf", &k, &s);
            mx = max(mx, (d - k) / s);
        }
        printf("Case #%d: %.6lf\n", tc, d / mx);
    }
    return 0;
}
