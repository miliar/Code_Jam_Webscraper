#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 2000;

int T, d, n, p[N], s[N];

int main() {

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &d, &n);
        double m = 0.0;
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &p[i], &s[i]);
            double x = 1.0 * (d - p[i]) / s[i];
            if (x > m) {
                m = x;
            }
        }
        printf("Case #%d: %.10f\n", t, 1.0 * d / m);
    }

    return 0;

}
