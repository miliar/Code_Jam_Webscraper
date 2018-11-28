#include <bits/stdc++.h>

using namespace std;

double solve();

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: %.20lf\n", i + 1, solve());
    }
}

double solve() {
    double d;
    int n;
    scanf("%lf%d", &d, &n);
    std::vector<double> k(n), s(n);
    double time = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%lf%lf", &k[i], &s[i]);
        double t = (d - k[i]) / s[i];
        if (t > time) {
            time = t;
        }
    }
    return d / time;
}
