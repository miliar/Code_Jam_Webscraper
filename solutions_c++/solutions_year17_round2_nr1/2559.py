#include <cstdio>
#include <algorithm>
using namespace std;

int x[1010];
double s[1010];

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        int d, n;
        scanf("%d %d", &d, &n);
        for (int i = 1; i <= n; i++)
            scanf("%d %lf", &x[i], &s[i]);
        for (int i = n - 1; i >= 0; i--) {
            if (i == 0 || (d - x[i]) * s[i+1] < (d - x[i+1]) * s[i])
                s[i] = (d - x[i]) * s[i + 1] / (d - x[i+1]);
        }
        printf("Case #%d: %lf\n", tc, s[0]);
    }
    return 0;
}
