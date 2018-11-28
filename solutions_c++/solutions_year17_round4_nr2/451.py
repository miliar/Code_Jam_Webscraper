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

const int maxc = 1010;
const int maxn = 1010;

int n, c, m;
int chose[maxc][maxn];
int cnt[maxn], cnt2[maxc];
int adj[maxn][maxn];

pi solven(int days) {
    memset(adj, 0, sizeof(adj));
    for (int i = 1; i <= n; i++) {
        adj[0][i] = cnt[i];
        adj[i][n + 1] = days;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            adj[j][i] = INF;
        }
    }
    queue<int> q;
    int f[maxn];
    int v[maxn];
    int minf[maxn];
    while (1) {
        memset(v, -1, sizeof(v));
        memset(minf, 0, sizeof(minf));
        q = {};
        q.push(0);
        v[0] = -2;
        minf[0] = INF;
        while (!q.empty()) {
            int u = q.front();
            if (u == n + 1) break;
            q.pop();
            for (int i = 0; i <= n + 1; i++) {
                if (adj[u][i] > 0 && v[i] == -1) {
                    v[i] = u;
                    minf[i] = min(minf[u], adj[u][i]);
                    if (i == n + 1) break;
                    q.push(i);
                }
            }
            if (minf[n + 1] > 0) break;
        }
        if (minf[n + 1] == 0) break;
        int ind = n + 1;
        while (ind != 0) {
            adj[v[ind]][ind] -= minf[n + 1];
            adj[ind][v[ind]] += minf[n + 1];
            ind = v[ind];
        }
    }
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += adj[n + 1][i];
    }
    if (sum == m) {
        int prom = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++)
                prom += adj[i][j];
        }
        return mp(1, prom);
    } else {
        return mp(0, 0);
    }
}

void solve() {
    cin >> n >> c >> m;

    memset(chose, 0, sizeof(chose));
    memset(cnt, 0, sizeof(cnt));
    memset(cnt2, 0, sizeof(cnt2));
    int mc = 0;
    forn (i, m) {
        int p = in();
        int b = in();
        chose[b][p]++;
        cnt[p]++;
        cnt2[b]++;
        uax(mc, cnt2[b]);
    }
    int l = mc, r = m;
    while (l < r) {
        int days = (l + r) >> 1;

        pi res = solven(days);
        if (res.fi) {
            r = days;
        } else {
            l = days + 1;
        }
    }
    pi res = solven(l);
    cout << ' ' << l << ' ' << res.se << '\n';
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
