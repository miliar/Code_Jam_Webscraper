#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second

constexpr int MAXN = 1010;


double jizz() {
    double d; int n;
    scanf("%lf%d", &d, &n);

    vector<pair<double, double>> ps(n);
    for (int i = 0; i < n; ++i) scanf("%lf%lf", &ps[i].F, &ps[i].S);

    double t = 0;

    for (int i = 0; i < n; ++i) t = max(t, (d - ps[i].F) / ps[i].S);

    return d / t;
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %.6lf\n", t, jizz());
    }

    return 0;
}
