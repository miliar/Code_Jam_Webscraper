#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

void solve(int nt) {
    int d, n;
    scanf("%d%d", &d, &n);
    double ans = 1e20;
    for (int i = 0; i < n; i++) {
        int k, s;
        scanf("%d%d", &k, &s);
        ans = min(ans, d/((d-k)*1.0/s));
    }
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
