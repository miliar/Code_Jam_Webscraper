#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <bitset>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

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

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

const int maxt = 1440;
int pos[2][maxt], dp[2][maxt + 1][maxt + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
#ifdef LOCAL_DEFINE
    freopen("input.txt", "rt", stdin);
#endif

    int T;
    cin >> T;
    for1(tc, T) {
        int n, m;
        cin >> n >> m;
        forn(i, 2) forn(j, maxt) pos[i][j] = 0;
        forn(i, n) {
            int x, y;
            cin >> x >> y;
            while (x < y) pos[0][x++] = 1;
        }
        forn(i, m) {
            int x, y;
            cin >> x >> y;
            while (x < y) pos[1][x++] = 1;
        }
        int ans = 1e9;
        forn(s, 2) {
            forn(i, 2) forn(j, maxt + 1) forn(k, maxt + 1) dp[i][j][k] = 1e9;
            dp[s][0][0] = 0;
            forn(j, maxt) forn(i, 2) forn(k, maxt + 1) {
                if (dp[i][j][k] > 1e8) continue;
                forn(ii, 2) {
                    if (!pos[ii][j]) uin(dp[ii][j + 1][k + ii], dp[i][j][k] + int(i != ii));
                }
            }
            forn(i, 2) uin(ans, dp[i][maxt][maxt / 2] + int(i != s));
        }
        cout << "Case #" << tc << ": " << ans << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
