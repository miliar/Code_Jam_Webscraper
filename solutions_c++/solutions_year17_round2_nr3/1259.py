#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 105;
int n, e[N], s[N], d[N];
double f[N];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%*d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", e+i, s+i);
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j == i + 1) {
                    scanf("%d", d+i);
                } else {
                    scanf("%*d");
                }
            }
        }
        scanf("%*d%*d");
        f[n-1] = 0;
        for (int i = n - 2; i >= 0; --i) {
            f[i] = 1e20;
            for (int j = i + 1, dis = d[i]; j < n && e[i] >= dis; ++j) {
                f[i] = min(f[i], f[j] + 1.0 * dis / s[i]);
                dis += d[j];
            }
        }
        printf("Case #%d: %.8f\n", cas, f[0]);
    }
}
