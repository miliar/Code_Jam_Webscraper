#include <bits/stdc++.h>
#define eps 1e-8
using namespace std;

int T, N;
double D, x, v;

double solve() {
    scanf("%lf %d", &D, &N);

    double res;

    for(int i=0;i<N;i++) {
        scanf("%lf %lf", &x, &v);

        double t_i = (D - x) / v;
        double v_i = D / t_i;

        res = i ? min(res, v_i) : v_i;
    }

    return res;
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%d", &T);

    for(int k=1;k<=T;k++) {
        printf("Case #%d: %.6f\n", k, solve());
    }

    return 0;
}
