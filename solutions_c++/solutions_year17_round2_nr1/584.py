#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int d, n;
        scanf("%d%d", &d, &n);
        double m = 0;
        for (int i = 0; i < n; i++) {
            int k, s;
            scanf("%d%d", &k, &s);
            m = max(m, (double) (d - k) / s);
        }
        printf("Case #%d: %.10lf\n", t, d / m);
    }
    return 0;
}