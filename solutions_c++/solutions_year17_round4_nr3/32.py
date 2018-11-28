#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>
#include <numeric>
#include <future>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
bool chmin(T &x, T y) {
    if (x > y) {
        x = y;
        return true;
    }
    return false;
}

template<typename T>
bool chmax(T &x, T y) {
    if (x < y) {
        x = y;
        return true;
    }
    return false;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//--------------------------------------------------------------------------
const int dirs[4][2] = {
        1, 0,
        0, 1,
        -1, 0,
        0, -1,
};

const int maxn = 205;

int mapping[2][4] = {
      3, 2, 1, 0,  // /
      1, 0, 3, 2,  //
};

vector<int> g[maxn * maxn], gt[maxn * maxn];


void add(int a, int b) {
    g[a ^ 1].pb(b);
    g[b ^ 1].pb(a);

    gt[b].pb(a ^ 1);
    gt[a].pb(b ^ 1);
}

vector<int> order;
int comp[maxn * maxn];
int used[maxn * maxn];
int cu = 1;

void dfs2(int v) {
    used[v] = cu;
    for (int to : g[v]) {
        if (used[to] != cu) {
            dfs2(to);
        }
    }
    order.pb(v);
}

void mark(int v, int cc) {
    comp[v] = cc;
    for (int to : gt[v]) {
        if (comp[to] == -1) {
            mark(to, cc);
        }
    }
}

vector<pair<int,int>> vis;
bool bad = false;
int n, m;

bool valid(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}
vector<string> a;

void dfs(int x, int y, int d) {
    if (!valid(x, y)) {
        return;
    }



    if (a[x][y] == '-' || a[x][y] == '|') {
        bad = true;
        return;
    }

    if (a[x][y] == '#') {
        return;
    }

    if (a[x][y] == '/') {
        d = mapping[0][d];
    } else if (a[x][y] == '\\') {
        d = mapping[1][d];
    } else {
        vis.pb(mp(x, y));
    }

    dfs(x + dirs[d][0], y + dirs[d][1], d);
}

int main() {

    srand(0);

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ": ";

        for (int i = 0; i < maxn * maxn; i++) {
            g[i].clear();
            gt[i].clear();
        }



        cin >> n >> m;
        cin.ignore();

        vector<pair<int,int>> lights;

        vector<vector<vector<int>>> control(n, vector<vector<int>>(m));

        a.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];

            for (int j = 0; j < m; j++) {
                if (a[i][j] == '-' || a[i][j] == '|') {
                    lights.pb(mp(i, j));
                }
            }
        }

        bool imp = false;
        for (int i = 0; i < lights.size(); i++) {
            int bcnt = 0;
            // hor
            vis.clear();
            bad = false;

            dfs(lights[i].fst, lights[i].snd - 1, 3);
            dfs(lights[i].fst, lights[i].snd + 1, 1);

            if (!bad) {
                for (auto x : vis) {
                    control[x.fst][x.snd].pb(2 * i + 0);
                }
            } else {
                add(2 * i + 1, 2 * i + 1);
            }

            bcnt += bad;

            // vert
            vis.clear();
            bad = false;

            dfs(lights[i].fst - 1, lights[i].snd, 2);
            dfs(lights[i].fst + 1, lights[i].snd, 0);

            if (!bad) {
                for (auto x : vis) {
                    control[x.fst][x.snd].pb(2 * i + 1);
                }
            } else {
                add(2 * i + 0, 2 * i + 0);
            }

            bcnt += bad;

            if (bcnt == 2) {
                imp = true;
            }
        }

        if (imp) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }



        for (int i = 0; i < n && !imp; i++) {
            for (int j = 0; j < m && !imp; j++) {
                if (a[i][j] == '.' && control[i][j].empty()) {
                    imp = true;
                }

                if (control[i][j].empty()) {
                    continue;
                }

                //cerr << control[i][j] << endl;
                assert(control[i][j].size() <= 2);
                add(control[i][j][0], control[i][j].back());
            }
        }

        cu++;
        order.clear();
        fill(comp, comp + lights.size() * 2, -1);
        for (int i = 0; i < lights.size() * 2; i++) {
            if (used[i] != cu) {
                dfs2(i);
            }
        }

        reverse(order.begin(), order.end());
        int cc = 0;
        for (int v : order) {
            if (comp[v] == -1) {
                mark(v, cc++);
            }
        }


        for (int i = 0; i < lights.size(); i++) {
            if (comp[i * 2 + 0] == comp[i * 2 + 1]) {
                imp = true;
            }
        }

        if (imp) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        set<int> on;

        for (int i = 0; i < lights.size(); i++) {
            if (comp[2 * i + 1] < comp[2 * i + 0]) {
                a[lights[i].fst][lights[i].snd] = '-';
                on.insert(2 * i + 0);
            } else {
                a[lights[i].fst][lights[i].snd] = '|';
                on.insert(2 * i + 1);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (control[i][j].size()) {
                    bool any = false;
                    for (auto v : control[i][j]) {
                        any |= on.count(v) > 0;
                    }

                    assert(any);
                }
            }
        }

        cout << "POSSIBLE" << endl;

        for (int i = 0; i < n; i++) {
            cout << a[i] << endl;
        }

    }

    return 0;
}