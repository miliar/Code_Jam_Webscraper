#include <bits/stdc++.h>

#define ld long double

using namespace std;

const ld eps = 1e-9;
const ld pi = acos(-1.0);

struct item {
    ld r, h;
    item(ld r = 0, ld h = 0) : r(r), h(h) {}
    bool operator<(const item& o) const {
        if (r == o.r)
            return h > o.h;
        return r < o.r;
    }
};

void solve() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<item> a(n);
    for (int i = 0; i < n; ++i)
        scanf("%Lf %Lf", &a[i].r, &a[i].h);
    sort(a.begin(), a.end());
    vector<vector<ld>> dp(n + 1, vector<ld>(n + 1));
    vector<vector<ld>> mx(n + 2, vector<ld>(n + 2));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (j == 1)
                dp[i][j] = a[i - 1].r * a[i - 1].r + a[i - 1].h * 2.0 * a[i - 1].r;
            else {
                ld val = a[i - 1].h * 2.0 * a[i - 1].r + a[i - 1].r * a[i - 1].r;
                val += mx[i][j - 1];
                dp[i][j] = max(dp[i][j], val);
            }
            ld cval = dp[i][j] - a[i - 1].r * a[i - 1].r;
            mx[i + 1][j] = max(mx[i + 1][j], mx[i][j]);
            mx[i + 1][j] = max(mx[i + 1][j], cval);
        }
    }
    ld ans = 0;
    for (int i = 1; i <= n; ++i)
        ans = max(ans, dp[i][k]);
    printf("%.7Lf\n", ans * pi);
}

void solve_stupid() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<item> a(n);
    for (int i = 0; i < n; ++i)
        scanf("%Lf %Lf", &a[i].r, &a[i].h);
    sort(a.begin(), a.end());
    ld ans = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        item p;
        ld cur = 0;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1)
                ++cnt;
        }
        if (cnt != k)
            continue;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                cur += a[i].h * 2.0 * pi * a[i].r;
                cur += pi * (a[i].r * a[i].r - p.r * p.r);
                p = a[i];
            }
        }
        if (ans < cur) {
            ans = cur;
        }
    }
    printf("%.7Lf\n", ans);
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        fprintf(stderr, "Case #%d is working\n", i);

        printf("Case #%d: ", i);
        solve();

        fprintf(stderr, "Case #%d is done\n", i);
    }


    return 0;
}