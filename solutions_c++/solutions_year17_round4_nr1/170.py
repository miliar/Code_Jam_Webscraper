#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <bitset>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb push_back
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;
const ld PI = acos(-1.0L);
const int MAXN = 110;
const int MAXP = 4;
int dp[4][MAXN][MAXN][MAXN];

void upd(int & a, int b) {
    a = min(a, b);
}

void solve() {
    int n, p;
    cin >> n >> p;
    vector<int> c(p);
    forn(i, n) {
        int x;
        cin >> x;
        x %= p;
        c[x]++;
    }
    forn(i, 4 - p) {
        c.pb(0);
    }
       
    forn(r, 4) {
        for (int i = c[1]; i >= 0; --i) {
            for (int j = c[2]; j >= 0; --j) {
                for (int g = c[3]; g >= 0; --g) {
                    dp[r][i][j][g] = INF;
                }
            }
        }
    }
    dp[0][c[1]][c[2]][c[3]] = 0;
    for (int i = c[1]; i >= 0; --i) {
        for (int j = c[2]; j >= 0; --j) {
            for (int g = c[3]; g >= 0; --g) {
                if (i == 0 && j == 0 && g == 0)
                    continue;
                forn(r, 4) {
                    if (i > 0)
                        upd(dp[(r - 1 + p)%p][i - 1][j][g], dp[r][i][j][g] + (r != 0 ? 1 : 0));
                    if (j > 0)
                        upd(dp[(r - 2 + p)%p][i][j - 1][g], dp[r][i][j][g] + (r != 0 ? 1 : 0));
                    if (g > 0)
                        upd(dp[(r - 3 + p)%p][i][j][g - 1], dp[r][i][j][g] + (r != 0 ? 1 : 0));
                }
            }
        }
    }
    int mn = INF;
    forn(i, p)
        mn = min(dp[i][0][0][0], mn);
    
    cout << n - mn << '\n';
}

int main() {
#ifdef LOCAL
    freopen("a.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(t, T) {
        printf("Case #%d: ", t +1);
        solve();
    }
    return 0;
}

