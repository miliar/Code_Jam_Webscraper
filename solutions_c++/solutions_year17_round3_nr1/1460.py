///Lol kek cheburek///
#include <bits/stdc++.h>
#pragma pack(1)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pii;
typedef vector<int> vi;
typedef vector< pii > vii;
typedef long double ld;

#define pb push_back
#define mp make_pair
#define ins insert
#define ers erase

#define elif else if
#define all(v) (v).begin(),(v).end()
#define len(s) int((s).size())

#define fi first
#define se second
#define x first
#define y second

#define fpos krevedka
#define left Levo
#define right ishtenem
#define next nastupniy
#define prev poperedniy
#define div dilyty_sukotay

#define I64 "%lld"

#define I "%d"
#define II I I
#define III II I
#define IIII II II
#define IIIII III II
#define IIIIII III III
#define IIIIIII IIII III
#define IIIIIIII IIII IIII

#define dbg cout << "dbg\n"
#define files(name) freopen(name".in", "r", stdin);freopen(name".out","w", stdout);
#define UOIfiles(name) freopen(name".dat", "r", stdin);freopen(name".sol","w", stdout);


ll sqr(ll x) {
    return x * x;
}

const ll md = 1e9 + 7;
const ll md2 = 2e9 + 7;
const ld PI = acos(-1);
const int MAXN = 2e6 + 1;
const int MAXLOG = 45;
const int INF = 1e9 + 1;
const int RNG = 1e8 + 10;
const pii turns[4] = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
const char signs[4] = {'D', 'L', 'R', 'U'};

///end template ///

int n, k;
pii a[2000];
ll dp[2000][2000];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);
    //cin.tie(nullptr);

    int tests;
    scanf(I, &tests);
    for(int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        scanf(II, &n, &k);
        for(int i = 0; i < n; i++) {
            scanf(I64 I64, &a[i].fi, &a[i].se);
        }
        sort(a, a + n, greater<pii>());
        dp[0][1] = 2 * a[0].fi * a[0].se + sqr(a[0].fi);
        ll ans = dp[0][k];
        for(int i = 1; i < n; i++) {
            dp[i][1] = max(dp[i - 1][1], 2 * a[i].fi * a[i].se + sqr(a[i].fi));
            for(int j = 2; j <= k; j++) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 2 * a[i].fi * a[i].se);
            }
            ans = max(ans, dp[i][k]);
        }

        cout << fixed << setprecision(20) << PI * ld(ans) << "\n";
    }
}
