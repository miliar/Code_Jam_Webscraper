#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
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

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

const int maxn = 110;

int f[maxn][maxn], nf[maxn][maxn];
int ls[4 * maxn], rs[4 * maxn];
int vis[4 * maxn], match[4 * maxn];
vi e[4 * maxn];

bool dfs(int v) {
    if (vis[v]) return false;
    vis[v] = 1;
    for (int u: e[v]) {
        if (match[u] == -1 || dfs(match[u])) {
            match[u] = v;
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tc, T) {
        int n, m;
        cin >> n >> m;
        forn(i, n) forn(j, n) f[i][j] = nf[i][j] = 0;
        forn(i, m) {
            char c;
            int x, y;
            cin >> c >> x >> y;
            --x; --y;
            if (c == 'x') f[x][y] = 1;
            else if (c == '+') f[x][y] = 2;
            else f[x][y] = 3;
        }

        int cost = 0;
        forn(i, 3 * n - 1) e[i].clear(), match[i] = -1, ls[i] = rs[i] = 0;
        forn(i, n) forn(j, n) {
            int d1 = i + j, d2 = n - i - 1 + j;
            if (f[i][j] & 1) ls[i] = rs[j] = 1, ++cost;
            if (f[i][j] & 2) ls[n + d1] = rs[n + d2] = 1, ++cost;
        }

        forn(i, n) forn(j, n) {
            int d1 = i + j, d2 = n - i - 1 + j;
            if (!ls[i] && !rs[j]) e[i].pb(j);
            if (!ls[n + d1] && !rs[n + d2]) e[n + d1].pb(n + d2);
        }

        forn(i, 3 * n - 1) {
            forn(j, 3 * n - 1) vis[j] = 0;
            if (dfs(i)) ++cost;
        }

        forn(j, n) {
            int i = match[j];
            if (i != -1) nf[i][j] |= 1;
        }

        forn(j, 2 * n - 1) {
            int i = match[n + j];
            if (i != -1) {
                i -= n;
                int x = (i - j + n - 1) / 2, y = (i + j - n + 1) / 2;
                nf[x][y] |= 2;
            }
        }

        int ch = 0;
        forn(i, n) forn(j, n) ch += int(f[i][j] != (f[i][j] | nf[i][j]));

        cout << "Case #" << tc << ": " << cost << ' ' << ch << '\n';
        forn(i, n) forn(j, n) {
            if (f[i][j] != (f[i][j] | nf[i][j])) cout << ".x+o"[f[i][j] | nf[i][j]] << ' ' << i + 1 << ' ' << j + 1 << '\n';
        }
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
