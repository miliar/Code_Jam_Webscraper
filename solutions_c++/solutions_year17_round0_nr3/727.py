#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define pb push_back
#define sz(x) (int)x.size()
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;
const int N = 25;

int T;
ll n, k;
map<ll, int> vis;
vector<ll> c;

void dfs(ll n) {
    if (n < 1) return;
    if (vis[n]) return;
    vis[n] = 1;
    c.pb(n);
    ll mid = (n + 1) / 2;
    dfs(mid - 1);
    dfs(n - mid);
}

ll dp[555];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%lld%lld", &n, &k);
        vis.clear(); c.clear();
        dfs(n);
        sort(c.begin(), c.end());
        reverse(c.begin(), c.end());
        vis.clear();
        for (int i = 0; i < sz(c); i++) vis[c[i]] = i;
        memset(dp, 0, sizeof(dp));
        dp[0] = 1;
        for (int i = 0; i < sz(c); i++) {
            ll u = c[i];
            ll mid = (u + 1) / 2;
            if (vis.count(mid - 1)) dp[vis[mid - 1]] += dp[i];
            if (vis.count(u - mid)) dp[vis[u - mid]] += dp[i];
        }
       // for (int i = 0; i < sz(c); i++) printf("%lld %lld\n", c[i], dp[i]);
        for (int i = 0; i < sz(c); i++) {
            if (k <= dp[i]) {
                ll mid = (c[i] + 1) / 2;
                printf("Case #%d: %lld %lld\n", ++cas, c[i] - mid, mid - 1);
                break;
            }
            k -= dp[i];
        }
    }
    return 0;
}
