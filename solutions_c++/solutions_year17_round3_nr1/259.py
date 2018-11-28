#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int n, k;
ll dp[1005][1005];

struct entry {
    int r, h;
    ll side;
    bool operator<(const entry& rhs) const {
        return r < rhs.r;
    }
} e[1005];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    const ld PI = acosl(-1);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        cin >> n >> k;
        for (int i = 1; i <= n; ++i) {
            cin >> e[i].r >> e[i].h;
            e[i].side = e[i].r * 2LL * e[i].h;
        }
        sort(e + 1, e + n + 1);
        for (int i = 1; i < 1005; ++i)
            dp[0][i] = -4e18;
        dp[0][0] = 0;
        ll ans = 0;
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = 0;
            for (int j = 1; j <= k; ++j)
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + e[i].side);
            ans = max(ans, dp[i - 1][k - 1] + e[i].side + e[i].r * 1LL * e[i].r);
        }
        cout << "Case #" << ttt << ": " << setprecision(17) << fixed << ans * PI << "\n";
    }

    return 0;
}
