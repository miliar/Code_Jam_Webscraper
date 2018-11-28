#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

void solve() {
    int n, k;
    scanf("%d%d", &n, &k);
    vector<ii> a;
    for(int i = 0; i < n; ++i) {
        int r, h;
        scanf("%d%d", &r, &h);
        a.push_back(ii(r, h));
    }
    sort(a.begin(), a.end());
    vector< vector<ll> > dp = vector< vector<ll> > (n, vector<ll>(k, 0));
    for(int nk = 0; nk < k; ++nk)
        for(int i = nk; i < n; ++i) {
            int r = a[i].first, h = a[i].second;
            if (nk == 0) {
                dp[i][nk] = 1LL * r * r + 2LL * r * h;
                // printf("%d %d %lld\n", i, nk, dp[i][nk]);
                continue;
            }
            for(int j = nk - 1; j < i; ++j) {
                int rj = a[j].first;
                dp[i][nk] = max(dp[i][nk], dp[j][nk - 1] + 1LL * r * r + 2LL * r * h - 1LL * rj * rj);
            }
        }
    ll ans = 0LL;
    for(int i = k - 1; i < n; ++i)
        ans = max(ans, dp[i][k - 1]);
    double res = 1.0 * ans * acos(-1.0);
    printf("%lf\n", res);
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