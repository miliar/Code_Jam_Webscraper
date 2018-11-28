#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <utility>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <cmath>
#include <cassert>

#define __GCJ__

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn = 110;

double a[maxn];

void solve() {
    int n;
    double U;
    scanf("%d%*d", &n);
    scanf("%lf", &U);
    for (int i = 0; i < n; ++i) {
        scanf("%lf", a + i);
    }
    sort(a, a + n);
    double ans = 0;
    for (int i = 0; i < n; ++i) {
        // suppose we rise a[0..i] to somewhere less than or equal to a[i + 1]
        double s = 0;
        for (int j = 0; j <= i; ++j) {
            s += a[j];
        }
        double bound = (U + s) / (i + 1);
        if (bound < a[i]) {
            break;
        }
        if (i == n - 1 || bound <= a[i + 1]) {
            // printf("accept i = %d, bound = %.3lf\n", i, bound);
            double p = 1;
            for (int j = 0; j < n; ++j) {
                p *= (j <= i) ? bound : a[j];
            }
            ans = max(ans, p);
        }
    }
    printf("%.12lf\n", ans);
}

int main() {
#ifdef __WYL__
    freopen("t.in", "r", stdin);
    // freopen("t.out", "w", stdout);
#endif

#ifdef __GCJ__
    int __T;
    scanf("%d\n", &__T);
    for (int __i = 1; __i <= __T; ++__i) {
        printf("Case #%d: ", __i);
        solve();
    }
#else
    solve();
#endif

#ifdef __WYL__
    fclose(stdin);
    fclose(stdout);
#endif
    return 0;
};
