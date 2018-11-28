#include <bits/stdc++.h>

using namespace std;

double a[100], u;

void solve() {
    int n, k;
    scanf("%d%d", &n, &k);
    scanf("%lf", &u);
    for(int i = 0; i < n; ++i)
        scanf("%lf", a + i);
    double l = 0, r = 1.0;
    for(int it = 0; it < 1000; ++it) {
        double mid = (l + r) / 2;
        double sum = 0.0;
        for(int i = 0; i < n; ++i)
            if (a[i] < mid)
                sum += mid - a[i];
        if (sum <= u) l = mid;
        else r = mid;
    }
    double ans = 1.0;
    for(int i = 0; i < n; ++i)
        if (a[i] < l)
            ans *= l;
        else
            ans *= a[i];
    printf("%lf\n", ans);
}

int main() {
    int ntests;
    scanf("%d", &ntests);
    for(int t = 1; t <= ntests; ++t) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}