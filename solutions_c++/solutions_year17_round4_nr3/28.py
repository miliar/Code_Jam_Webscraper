#define _GLIBCXX_CXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef long long ll;

const int maxn = 200100; //2 x number of variables

namespace TwoSAT {
    int n; //number of variables
    int used[maxn];
    vector<int> g[maxn];
    vector<int> gr[maxn];
    int comp[maxn];
    int res[maxn];

    void addEdge(int u, int v) { //u or v
        assert(u < n*2);
        assert(v < n*2);
        g[u].push_back(v ^ 1);
        g[v].push_back(u ^ 1);
        gr[u ^ 1].push_back(v);
        gr[v ^ 1].push_back(u);
    }

    vector<int> ord;
    void dfs1(int u) {
        used[u] = true;
        for (int v: g[u]) {
            if (used[v])
                continue;
            dfs1(v);
        }
        ord.push_back(u);
    }

    int COL = 0;
    void dfs2(int u) {
        used[u] = true;
        comp[u] = COL;
        for (int v: gr[u]) {
            if (used[v])
                continue;
            dfs2(v);
        }
    }

    void mark(int u) {
        res[u / 2] = u % 2;
        used[u] = true;
        for (int v: g[u]) {
            if (used[v])
                continue;
            mark(v);
        }
    }

    bool run() {
        fill(res, res + 2 * n, -1);
        fill(used, used + 2 * n, false);
        fill(comp, comp + 2 * n, 0);
        ord.clear();
        COL = 0;
        forn (i, 2 * n)
            if (!used[i])
                dfs1(i);
        reverse(ord.begin(), ord.end());
//         cerr << n << " " << ord.size() << endl;
        assert((int) ord.size() == (2 * n));
        fill(used, used + 2 * n, false);
        for (int u: ord) if (!used[u]) {
            dfs2(u);
            ++COL;
        }
        forn (i, n)
            if (comp[i * 2] == comp[i * 2 + 1])
                return false;
        forn(i, n) res[i] = comp[i*2] < comp[i*2+1];
        return true;

        reverse(ord.begin(), ord.end());
        fill(used, used + 2 * n, false);
        for (int u: ord) {
            if (res[u / 2] != -1) {
                continue;
            }
            mark(u);
        }
        return true;
    }
};

int n, m;
char c[60][60];
int b[60][60];
vector<pii> pos;
vector<int> by[60][60];

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

bool go(int x, int y, int d, int col) {
//     cerr << "go " << d << endl;
    vector<pii> put;
    while (true) {
        x += dx[d], y += dy[d];
//         cerr << x << " " << y << endl;
        if (x < 0 || y < 0 || x >= n || y >= m || c[x][y] == '#') {
            for (auto kv: put) {
                by[kv.fi][kv.se].pb(col);
            }
            return true;
        }
        if (c[x][y] == '.') {
            put.pb({x, y});
        }

        if (c[x][y] == '-') {
            return false;
        }
        if (c[x][y] == '/') {
            const static int sw[] = {3, 2, 1, 0};
            d = sw[d];
        }
        if (c[x][y] == '\\') {
            const static int sw[] = {1, 0, 3, 2};
            d = sw[d];
        }
    }
}

void solve(int tn) {
    cin >> n >> m;
    forn(i, n) cin >> c[i];
//     if (tn != 25) return;
    pos.clear();
    forn(i, n) forn(j, m) by[i][j].clear();
    forn(i, n) forn(j, m) {
        if (c[i][j] == '-' || c[i][j] == '|') {
            c[i][j] = '-';
            pos.pb({i, j});
        }
    }
    TwoSAT::n = pos.size();
    forn(i, pos.size() * 2) {
        TwoSAT::g[i].clear();
        TwoSAT::gr[i].clear();
    }

    bool fail = false;
    forn(i, pos.size()) {
        bool can0 = true, can1 = true;
        int x, y;
        tie(x, y) = pos[i];
        if (!go(x, y, 1, i*2+0)) can0 = false;
        if (!go(x, y, 3, i*2+0)) can0 = false;
        if (!go(x, y, 0, i*2+1)) can1 = false;
        if (!go(x, y, 2, i*2+1)) can1 = false;
        if (!can0 && !can1) {
            fail = true;
            break;
        } else if (!can0) {
            TwoSAT::addEdge(i*2+1, i*2+1);
        } else if (!can1) {
            TwoSAT::addEdge(i*2, i*2);
        }
    }
    /*
    forn(i, n) forn(j, m) if (c[i][j] == '.') {
        cerr << i << " " << j << ": ";
        for (int x: by[i][j]) cerr << x << " ";
        cerr << endl;
    }
    */
    if (!fail) {
        forn(i, n) forn(j, m) if (c[i][j] == '.') {
            auto& a = by[i][j];
            assert(a.size() <= 2);
            if (a.empty()) {
                fail = true;
                break;
            } else if (a.size() == 1) {
                int x = a[0];
                TwoSAT::addEdge(x, x);
            } else {
                int x = a[0], y = a[1];
                TwoSAT::addEdge(x, y);
            }
        }

        if (!TwoSAT::run()) {
            fail = true;
        }
    }
    cout << "Case #" << tn << ": ";
    if (fail) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    cout << "POSSIBLE\n";
    int p = 0;
    forn(i, n) {
        forn(j, m) {
            if (c[i][j] == '-') {
                c[i][j] = "|-"[TwoSAT::res[p++]];
            }
        }
    }
    forn(i, n) {
        cout << c[i] << "\n";
    }
    /*
    memset(b, 0, sizeof b);
    forn(i, n) forn(j, m) {
        if (c[i][j] == '-') {
            int x = i, y = j;
            while (true) {
                --y;
                if (y < 0) break;
                if (c[x][y] == '#') break;
                assert(c[x][y] == '.');
                b[x][y] = 1;
            }
            y = j;
            while (true) {
                ++y;
                if (y >= m) break;
                if (c[x][y] == '#') break;
                assert(c[x][y] == '.');
                b[x][y] = 1;
            }
        }
        if (c[i][j] == '|') {
            int x = i, y = j;
            while (true) {
                --x;
                if (x < 0) break;
                if (c[x][y] == '#') break;
                assert(c[x][y] == '.');
                b[x][y] = 1;
            }
            x = i;
            while (true) {
                ++x;
                if (x >= n) break;
                if (c[x][y] == '#') break;
                assert(c[x][y] == '.');
                b[x][y] = 1;
            }
        }
    }
    forn(i, n) forn(j, m) if (c[i][j] == '.') {
//         cerr << i << " " << j << endl;
        assert(b[i][j]);
    }
    assert(p == TwoSAT::n);
    */
}

int main() {
#ifdef LOCAL
//     freopen("c.in", "r", stdin);
#endif

    int t;
    cin >> t;
    forn(i, t) {
        solve(i+1);
    }

#ifdef LOCAL
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
    return 0;
}
