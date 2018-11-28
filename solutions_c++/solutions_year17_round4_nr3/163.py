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
const int MAXN = 55;

int r, c;
struct point {
    int x, y;
    point operator + (const point & o )const {
        return {x + o.x, y + o.y};
    }
    bool inside() const {
        return x >= 0 && y >= 0 &&x < r && y < c;
    }
};
const vector<point> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

char t[MAXN][MAXN];
vector<int> x[MAXN][MAXN];
vector<point> path;

bool search(point c, int nd) {
    if (t[c.x][c.y] == '.')
        path.pb(c);
    point nc = c + dirs[nd];
    if (!nc.inside())
        return true;
    if (t[nc.x][nc.y] == '#')
        return true;
    if (t[nc.x][nc.y] == '*')
        return false;
    if (t[nc.x][nc.y] == '\\') {
        nd ^= 1;
    }
    if (t[nc.x][nc.y] == '/') {
        nd ^= 3;
    }
    if (search(nc, nd)) {
        return true;
    } else {
        return false;
    }
}
const int MAXM = 210;
vector<int> e[MAXM];

bool vset[MAXM];


bool val[MAXM];

int beams;
int other(int n) {
    if (n > beams) {
        return n - beams;
    } else {
        return n + beams;
    }
}

bool used[MAXM];
void mark(int v) {
    used[v] = true;
    for (auto u : e[v]) {
        if (!used[u])
            mark(u);
    }
}
void solve() {
    cin >> r >> c;
    forn(i, r) {
        forn(j, c) { 
            x[i][j].clear();
            cin >> t[i][j];
            if (t[i][j] == '|' || t[i][j] == '-') {
                t[i][j] = '*';
            }
        }
    }
    beams = 0;
    clr(val);
    clr(vset);
    forn(i, r) {
        forn(j, c) { 
            if (t[i][j] == '*') {
                beams++;
                path.clear();
                if (!search({i, j}, 0) || !search({i, j}, 2)) {
                    val[beams] = 1;
                    vset[beams] = true;
                } else {
                    for (auto c : path) {
                        x[c.x][c.y].pb(-beams);
                    }
                }
                path.clear();
                if (!search({i, j}, 1) || !search({i, j}, 3)) {
                    if (vset[beams]) {
                        cout << "IMPOSSIBLE\n";
                        return;
                    }
                    val[beams] = 0;
                    vset[beams] = true;
                } else {
                    for (auto c : path) {
                        x[c.x][c.y].pb(beams);
                    }
                }
            }
        }
    }
    forn(i, 2 * beams + 1) {
        e[i].clear();
    }
    forn(i, r) {
        forn(j, c) {
            if (t[i][j] != '.')
                continue;
            assert(x[i][j].size() < 3);
            if (x[i][j].size() == 0){
                cout << "IMPOSSIBLE\n";
                return;
            }
            if (x[i][j].size() == 1) {
                int n = (x[i][j][0]);
                int an = abs(n);
                if (!vset[an]) {
                    vset[an] = true;
                    val[an] = (n > 0);
                } else {
                    if (val[an] != (n > 0)) {
                        cout << "IMPOSSIBLE\n";
                        return;
                    }
                }
            }
            if (x[i][j].size() == 2) {
                int n1 = (x[i][j][0]);
                int an1 = abs(n1);
                if (n1 < 0) {
                    n1 = beams + an1;
                }
                int n2 = (x[i][j][1]);
                int an2 = abs(n2);
                if (n2 < 0) {
                    n2 = beams + an2;
                }
                e[other(n1)].pb(n2);
                e[other(n2)].pb(n1);
            }
        }
    }
    for (int i = 1; i <= beams; ++i) {
        if (vset[i]) {
            if (val[i]) {
                e[other(i)].pb(i);
            } else {
                e[i].pb(other(i));
            }
        }
    }
    for (int i = 1; i <= beams; ++i) {
        clr(used);
        mark(i);
        if (used[i + beams]) {
            clr(used);
            mark(i + beams);
            if (used[i]) {
                cout << "IMPOSSIBLE\n";
                return;
            } else {
                val[i] = false;
            }
        } else {
            val[i] = true;
        }
    }
    int bs = 0;
    cout << "POSSIBLE\n";
    forn(i, r) {
        forn(j, c) {
            if (t[i][j] == '*') {
                ++bs;
                if (val[bs]) {
                    t[i][j] = '-';
                } else {
                    t[i][j] = '|';
                }
            }
            cout << t[i][j];
        }
        cout << '\n';
    }
}

int main() {
#ifdef LOCAL
    freopen("c.in", "r", stdin);
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

