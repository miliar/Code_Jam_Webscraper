#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <queue>

using namespace std;

#define DEBUG

int T;
int n, k;
double u;
vector < double > p;

bool ok(double x) {
    double extra = 0;
    for (int i = 0; i < n; ++i) {
        extra += max(x - p[i], 0.0);
    }

    return extra <= u;
}

double solve() {
    scanf("%d %d", &n, &k);
    scanf("%lf", &u);

    p.resize(n);
    for (int i = 0; i < n; ++i) {
        scanf("%lf", &p[i]);
    }

    if (ok(1.0)) {
        return 1.0;
    }

    double l = 0;
    double r = 1.0;
    double m;

    for (int t = 0; t < 30; ++t) {
        m = (l + r) / 2;

        if (ok(m)) {
            l = m;
        } else {
            r = m;
        }
    }

    double ans = 1;

    for (int i = 0; i < n; ++i) {
        ans *= max(m, p[i]);
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %0.8lf\n", t, solve());
    }

    return 0;
}