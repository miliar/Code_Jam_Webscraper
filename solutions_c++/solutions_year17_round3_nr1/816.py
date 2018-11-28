#include <bits/stdc++.h>

using namespace std;

#define PI acos(-1)
#define EPS 1e-9
#define ll long long

int t, n, k;

struct pan {
    ll r, h;
} pans[1010];

bool cmp(pan a, pan b) {
    return a.r > b.r;
}

long double dp[1010][1010][2];

long double solve(int ind, int chosen, bool p) {
    if (fabs(dp[ind][chosen][p] + 1.0) > EPS) return dp[ind][chosen][p];

    if (ind == n) {
        if (chosen == k) return 0.0;
        else return -100000000000000000000000000000000000000000.0;
    }

    long double ret = 0.0, area = 2.0, circ = pans[ind].r;
    area *= PI; area *= (long double) pans[ind].r; area *= (long double) pans[ind].h;
    circ *= circ; circ *= PI;

    ret = max(solve(ind+1, chosen, p), solve(ind+1, chosen+1, true) + area + (p? 0.0 : circ));

    return dp[ind][chosen][p] = ret;
}

int main() {
    scanf("%d", &t);
    for (int tc = 0; tc < t; tc++) {
        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; i++)
            scanf("%lld %lld", &pans[i].r, &pans[i].h);

        sort(pans, pans+n, cmp);

        for (int i = 0; i < 1010; i++)
            for (int j = 0; j < 1010; j++)
                dp[i][j][0] = dp[i][j][1] = -1.0;

        long double ans = solve(0, 0, 0);

        printf("Case #%d: %.9Lf\n", tc+1, ans);
    }

    return 0;
}
