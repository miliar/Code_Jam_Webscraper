#include <bits/stdc++.h>
using namespace std;

#ifdef SG
#include <debug.h>
#else
#define show(...)
#define debug(...)
#define deepen(...)
#define timer(...)
#endif

#define ARG4(_1,_2,_3,_4,...) _4

#define forn3(i,l,r) for (int i = int(l); i < int(r); ++i)
#define forn2(i,n) forn3 (i, 0, n)
#define forn(...) ARG4(__VA_ARGS__, forn3, forn2) (__VA_ARGS__)

#define ford3(i,l,r) for (int i = int(r) - 1; i >= int(l); --i)
#define ford2(i,n) ford3 (i, 0, n)
#define ford(...) ARG4(__VA_ARGS__, ford3, ford2) (__VA_ARGS__)

#define ve vector
#define pa pair
#define tu tuple
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define fs first
#define sc second
#define all(a) (a).begin(), (a).end()
#define sz(a) ((int)(a).size())

typedef long double ld;
typedef int64_t ll;
typedef uint64_t ull;
typedef uint32_t ui;
typedef uint16_t us;
typedef uint8_t uc;
typedef pa<int, int> pii;
typedef pa<int, ll> pil;
typedef pa<ll, int> pli;
typedef pa<ll, ll> pll;
typedef ve<int> vi;

typedef tu< int, int, int > tiii;

const ld pi = 3.1415926535897932384626433832795l;

template<typename T> inline auto sqr (T x) -> decltype(x * x) {return x * x;}
template<typename T1, typename T2> inline bool umx (T1& a, T2 b) {if (a < b) {a = b; return 1;} return 0;}
template<typename T1, typename T2> inline bool umn (T1& a, T2 b) {if (b < a) {a = b; return 1;} return 0;}

struct Input {
    int r, c;
    ve< string > f;

    bool read () {
        if (!(cin >> r >> c)) return 0;
        f.resize(r);
        forn (i, r) {
            cin >> ws >> f[i];
        }
        return 1;
    }

    void init (const Input &input) {
        *this = input;
    }
};

struct Data: Input {
    ve< string > ans;
    bool ok;

    void write (int id) {
        cout << "Case #" << id << ": ";
        if (ok) {
            cout << "POSSIBLE\n";
            for (const auto &s : ans) {
                cout << s << '\n';
            }
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
};

const int DX[] = {-1, 0, 1, 0};
const int DY[] = {0, 1, 0, -1};

const int MAXN = 100;

struct Solution: Data {

    ve< pii > shoot;
    int used_d[MAXN][MAXN][2];
    int id[MAXN][MAXN];

    ve< vi > g, gt;
    vi used, order, comp;

    bool field(int x, int y) {
        return (0 <= x && x < r && 0 <= y && y < c && f[x][y] != '#');
    }

    int mut_dir(int dir, char tp) {
        if (tp == '/') {
            dir ^= 1;
        } else if (tp == '\\') {
            dir ^= 3;
        }
        return dir;
    }

    int rdfs(int x, int y, int dir, int sid) {
        return dfs(x, y, dir, sid) && dfs(x, y, dir ^ 2, sid);
    }

    int dfs(int x, int y, int dir, int sid) {
        used_d[x][y][dir & 1] = sid;
        dir = mut_dir(dir, f[x][y]);
        int nx = x + DX[dir], ny = y + DY[dir];
        if (!field(nx, ny)) return 1;
        if (used_d[nx][ny][dir & 1] != -1)
            return 0;
        if (id[nx][ny] != -1)
            return 0;
        return dfs(nx, ny, dir, sid);
    }

    void dfs1(int v) {
        used[v] = 1;
        for (int to: g[v]) {
            if (!used[to]) dfs1(to);
        }
        order.pb(v);
    }

    void dfs2(int v, int cl) {
        comp[v] = cl;
        for (int to: gt[v]) {
            if (comp[to] == -1) dfs2(to, cl);
        }
    }

    void solve () {
        ok = false;
        ans.clear();
        shoot.clear();
        memset(id, -1, sizeof(id));
        forn (i, r) {
            forn (j, c) {
                if (f[i][j] == '-' || f[i][j] == '|') {
                    f[i][j] = '-';
                    id[i][j] = sz(shoot);
                    shoot.emplace_back(i, j);
                }
            }
        }
        debug(shoot);
        debug("here");
        vi msk(sz(shoot), 0);
        forn (i, sz(shoot)) {
            int x = shoot[i].first, y = shoot[i].second;
            msk[i] = 0;
            forn (it, 2) {
                memset(used_d, -1, sizeof(used_d));
                if (rdfs(x, y, it, 2 * i + it)) {
                    msk[i] |= (1 << it);
                }
            }
            debug(i, msk[i]);
            if (!msk[i]) {
                // no chances
                return;
            }
        }
        debug(msk);
        memset(used_d, -1, sizeof(used_d));
        // 2-SAT itself
        g.assign(2 * sz(shoot), vi());
        gt = g;
        forn (i, sz(shoot)) {
            int x = shoot[i].first, y = shoot[i].second;
            forn (it, 2) {
                if ((msk[i] & (1 << it))) {
                    rdfs(x, y, it, 2 * i + it);
                }
            }
            int l = i * 2, r = i * 2 + 1;
            if (msk[i] == 1) {
                r = l;
            }
            if (msk[i] == 2) {
                l = r;
            }
            debug(mt(i, l, r));
            g[l ^ 1].pb(r);
            gt[r].pb(l ^ 1);
            g[r ^ 1].pb(l);
            gt[l].pb(r ^ 1);
        }
        forn (i, r) {
            forn (j, c) {
                if (f[i][j] != '.') {
                    continue;
                }
                int a = used_d[i][j][0], b = used_d[i][j][1];
                debug(mt(i, j, a, b));
                if (a == -1 && b == -1) {
                    return;
                }
                if (b == -1) b = a;
                if (a == -1) a = b;
                g[a ^ 1].pb(b);
                gt[b].pb(a ^ 1);
                g[b ^ 1].pb(a);
                gt[a].pb(b ^ 1);
            }
        }
        used.assign(2 * sz(shoot), 0);
        order.clear();
        forn (i, 2 * sz(shoot)) {
            if (!used[i]) dfs1(i);
        }
        debug(order);
        comp.assign(2 * sz(shoot), -1);
        int cid = 0;
        for (auto it = order.rbegin(); it != order.rend(); ++it) {
            int v = *it;
            if (comp[v] == -1) dfs2(v, cid++);
        }
        debug(comp);
        forn (i, sz(shoot)) {
            if (comp[i * 2] == comp[i * 2 + 1]) {
                return;
            }
        }
        ok = true;
        ans = f;
        forn (i, sz(shoot)) {
            int x = shoot[i].first, y = shoot[i].second;
            if (comp[2 * i] > comp[2 * i + 1]) {
                ans[x][y] = '|';
            } else {
                ans[x][y] = '-';
            }
        }
    }

    void clear () {
        *this = Solution();
    }
};

Solution sol;

int main () {
    cout.setf(ios::showpoint | ios::fixed);
    cout.precision(20);
    int t;
    scanf("%d", &t);
    forn (i, t) {
        sol.read();
        sol.solve();
        sol.write(i + 1);
        sol.clear();
    }
    return 0;
}
