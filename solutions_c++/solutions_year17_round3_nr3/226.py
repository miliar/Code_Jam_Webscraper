#include <bits/stdc++.h>

using namespace std;

const double eps = 1e-12;

typedef long long LL;

const int N = 100;

double p[N];

void solve(int nt) {
    int n, k;
    scanf("%d%d", &n, &k);
    double sum;
    scanf("%lf", &sum);

    for (int i = 0; i < n; i++) {
        scanf("%lf", p+i);
    }
    sort(p, p+n);

    p[n] = 1;

    for (int i = 1; i <= n; i++) {
        if (abs(p[i]-p[i-1]) < eps) continue;
        double sub = (p[i] - p[i-1]) * i;
        if (sum < sub || abs(sum-sub) < eps) {
            sum /= i;
            for (int j = 0; j < i; j++)
                p[j] = p[i-1] + sum;
            break;
        }
        else {
            sum -= sub;
            for (int j = 0; j < i; j++)
                p[j] = p[i];
        }
    }

    double ans = 1;
    for (int i = 0; i < n; i++) ans *= p[i];

    printf("Case #%d: %.10f\n", nt, ans);
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
