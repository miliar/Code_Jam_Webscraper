#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;

#define forn(i, a, n) for (int i = a; i < n; ++i)
#define ford(i, a, n) for (int i = n - 1; i >= a; --i)
#define fore(i, a, n) for (int i = a; i <= n; ++i)
#define all(a) (a).begin(), (a).end()
#define fs first
#define sn second
#define trace(a)\
    for (auto i : a) cerr << i << ' ';\
    cerr << '\n'
#define eb emplace_back

#ifndef M_PI
const ld M_PI = acos(-1.0);
#endif

const ld eps = 1e-9;
const int INF = 2000000000;
const ll LINF = 1ll * INF * INF;
const ll MOD = 1000000007;

const int MAXN = 410;
 
int n, c[MAXN][MAXN], f[MAXN][MAXN], s, t, d[MAXN], ptr[MAXN], q[MAXN];
 
bool bfs() {
    int qh=0, qt=0;
    q[qt++] = s;
    memset (d, -1, n * sizeof d[0]);
    d[s] = 0;
    while (qh < qt) {
        int v = q[qh++];
        for (int to=0; to<n; ++to)
            if (d[to] == -1 && f[v][to] < c[v][to]) {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
    }
    return d[t] != -1;
}
 
int dfs (int v, int flow) {
    if (!flow)  return 0;
    if (v == t)  return flow;
    for (int & to=ptr[v]; to<n; ++to) {
        if (d[to] != d[v] + 1)  continue;
        int pushed = dfs (to, min (flow, c[v][to] - f[v][to]));
        if (pushed) {
            f[v][to] += pushed;
            f[to][v] -= pushed;
            return pushed;
        }
    }
    return 0;
}
 
int dinic() {
    memset(q, 0, MAXN * sizeof q[0]);
    int flow = 0;
    for (;;) {
        if (!bfs())  break;
        memset (ptr, 0, n * sizeof ptr[0]);
        while (int pushed = dfs (s, INF))
            flow += pushed;
    }
    return flow;
}

void solve() {
    int _n, m;
    cin >> _n >> m;
    int ans = 0;
    vector<char> ch(m);
    vector<int> x(m), y(m);
    forn(i, 0, m) {
        cin >> ch[i] >> x[i] >> y[i];
        --x[i], --y[i];
        ++ans;
        if (ch[i] == 'o') ++ans;
    }
    set<int> xs, ys, sums, difs;
    forn(i, 0, _n) xs.insert(i);
    forn(i, 0, _n) ys.insert(i);
    forn(i, 0, 2 * _n - 1) sums.insert(i);
    forn(i, 1 - _n, _n) difs.insert(i);
    forn(i, 0, m) {
        if (ch[i] != 'x') {
            sums.erase(x[i] + y[i]);
            difs.erase(x[i] - y[i]);
        }
        if (ch[i] != '+') {
            xs.erase(x[i]);
            ys.erase(y[i]);
        }
    }

    n = 2 * _n + 2;
    forn(i, 0, n)
        forn(j, 0, n)
            c[i][j] = f[i][j] = 0;
    for (int i : xs)
        for (int j : ys)
            c[i][j + _n] = 1;
    s = n - 2, t = n - 1;
    forn(i, 0, _n) c[s][i] = 1;
    forn(i, 0, _n) c[i + _n][t] = 1;
    ans += dinic();
    set<pair<int, int>> orth;
    forn(i, 0, _n) forn(j, 0, _n) if (f[i][j + _n]) orth.emplace(i, j);

    n = 4 * _n;
    forn(i, 0, n)
        forn(j, 0, n)
            c[i][j] = f[i][j] = 0;
    /*for (int i : sums)
        for (int j : difs) {
            if ((i + j) % 2) continue;
            int _x = (i + j) / 2, _y = (i - j) / 2;
            if (_x < 0 || _x >= _n || _y < 0 || _y >= _n) continue;
            c[i][j + 3 * _n - 2] = 1;
        }*/
    forn(_x, 0, _n) forn(_y, 0, _n) {
        int sum = _x + _y, dif = _x - _y;
        if (sums.find(sum) == sums.end() || difs.find(dif) == difs.end()) continue;
        c[sum][dif + (_n - 1) + (2 * _n - 1)] = 1;
    }
    s = n - 2, t = n - 1;
    forn(i, 0, 2 * _n - 1) c[s][i] = 1;
    forn(i, 0, 2 * _n - 1) c[i + 2 * _n - 1][t] = 1;
    ans += dinic();
    set<pair<int, int>> diag;
    forn(i, 0, 2 * _n - 1) forn(j, 0, 2 * _n - 1) if (f[i][j + 2 * _n - 1]) {
        int df = j - (_n - 1);
        int _x = (i + df) / 2, _y = (i - df) / 2;
        assert(c[i][j + 2 * _n - 1]);
        diag.emplace(_x, _y);
    }

    map<pair<int, int>, char> mp, out;
    forn(i, 0, m) mp[{x[i], y[i]}] = ch[i];
    for (auto p : orth) {
        if (mp.find(p) != mp.end()) {
            mp[p] = 'o';
            out[p] = 'o';
        } else {
            mp[p] = 'x';
            out[p] = 'x';
        }
    }
    for (auto p : diag) {
        if (mp.find(p) != mp.end()) {
            mp[p] = 'o';
            out[p] = 'o';
        } else {
            mp[p] = '+';
            out[p] = '+';
        }
    }
    cout << ans << ' ' << out.size() << '\n';
    for (auto q : out) {
        cout << q.sn << ' ' <<  1 + q.fs.fs << ' ' << 1 + q.fs.sn << '\n';
    }

    /*for (auto p : orth) cout << p.fs << ' ' << p.sn << '\n';
    cout << '\n';
    for (auto p : diag) cout << p.fs << ' ' << p.sn << '\n';
    cout << '\n';*/
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int _t;
    cin >> _t;
    forn(i, 0, _t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
