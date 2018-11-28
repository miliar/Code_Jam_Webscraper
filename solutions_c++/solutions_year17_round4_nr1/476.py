#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>
#include <fstream>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vpi;
typedef vector<vi> vvi;
typedef vector<vpi> vvpi;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<vll> vvll;
typedef vector<vpll> vvpll;

const int INF = 1001001001;
const ll INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }
int in() { int x; cin >> x; return x; }
double fin() { double x; cin >> x; return x; }
string sin() { string x; cin >> x; return x; }
ll llin() { ll x; cin >> x; return x; }

int cnt[4];
int dp[101][101][101];

void solve() {
    int n, p;

    cin >> n >> p;
    memset(cnt, 0, sizeof(cnt));
    memset(dp, 0, sizeof(dp));
    forn (i, n) {
        int t = in();
        cnt[t % p]++;
    }
    dp[0][0][0] = 0;
    for (int i = 0; i <= cnt[1]; i++) {
        for (int j = 0; j <= cnt[2]; j++) {
            for (int k = 0; k <= cnt[3]; k++) {
                if (p == 2) {
                    if (i >= 2 && dp[i - 2][j][k] != -1)
                        dp[i][j][k] = dp[i - 2][j][k] + 1;
                } else if (p == 3) {
                    if (i >= 3 && dp[i - 3][j][k] != -1)
                        uax(dp[i][j][k], dp[i - 3][j][k] + 1);
                    if (j >= 3 && dp[i][j - 3][k] != -1)
                        uax(dp[i][j][k], dp[i][j - 3][k] + 1);
                    if (i >= 1 && j >= 1 && dp[i - 1][j - 1][k] != -1)
                        uax(dp[i][j][k], dp[i - 1][j - 1][k] + 1);
                } else if (p == 4) {
                    if (i >= 4 && dp[i - 4][j][k] != -1)
                        uax(dp[i][j][k], dp[i - 4][j][k] + 1);
                    if (j >= 2 && dp[i][j - 2][k] != -1)
                        uax(dp[i][j][k], dp[i][j - 2][k] + 1);
                    if (k >= 4 && dp[i][j][k - 4] != -1)
                        uax(dp[i][j][k], dp[i][j][k - 4] + 1);
                    if (i >= 2 && j >= 1 && dp[i - 2][j - 1][k] != -1)
                        uax(dp[i][j][k], dp[i - 2][j - 1][k] + 1);
                    if (k >= 2 && j >= 1 && dp[i][j - 1][k - 2] != -1)
                        uax(dp[i][j][k], dp[i][j - 1][k - 2] + 1);
                    if (i >= 1 && k >= 1 && dp[i - 1][j][k - 1] != -1)
                        uax(dp[i][j][k], dp[i - 1][j][k - 1] + 1);
                }
            }
        }
    }
    int m = cnt[1] + 2 * cnt[2] + 3 * cnt[3];
    int sol = dp[cnt[1]][cnt[2]][cnt[3]] + cnt[0];
    if (m % p != 0) sol++;

    cout << ' ' << sol << endl;
}

int main() {

#ifdef LOCAL_ENV
    freopen("sol.in", "r", stdin);
    freopen("sol.out", "w", stdout);
#else
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#endif

    int nc;
    cin >> nc;
    for (int tc = 1; tc <= nc; tc++) {
        cout << "Case #" << tc << ":";
        solve();
    }
    return 0;
}
