#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

static const int MAX_N = 1000;

double L;
int n;
double a[MAX_N], v[MAX_N];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {

        scanf("%lf%d", &L, &n);
        double t = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf", &a[i], &v[i]);
            t = max(t, (L - a[i]) / v[i]);
        }

        double ans = L / t;
        printf("Case #%d: %.12lf\n", test, ans);
    }

    return 0;
}
