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
const int MAXN = 1e5;
struct cell {
    int x, y;
};

struct graph {
    int n;
    vector<cell> m;
    vector<bool> used, dell, delr;
    vector<int> pr;
    vector<vector<int>> e;
    graph(int n) {
        this->n = n;
        dell.resize(n, false);
        delr.resize(n, false);
        e.resize(n, vector<int>());
    }
    void del(int x, int y) {
        dell[x] = delr[y] = true;
    }
    void addEdge(int x, int y) {
        if (!dell[x] && !delr[y]) {
            e[x].push_back(y);
        }
    }
    bool dfs(int v) {
        used[v] = true;
        for (auto u : e[v]) {
            if (pr[u] == -1 || (!used[pr[u]] && dfs(pr[u]))) {
                pr[u] = v;
                return true;
            }
        }
        return false;
    }
    void findMatching() {
        used.resize(n, false);
        pr.resize(n, -1);
        for (int v = 0; v < n; ++v) {
            fill(used.begin(), used.end(), false);
            dfs(v);
        }
        for (int v = 0; v < n; ++v) {
            if (pr[v] != -1) {
                m.push_back({pr[v], v});
            }
        }
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<char>> s(n, vector<char>(n, '.'));
    graph rs(n);
    graph es(2 * n - 1);
    int cost = 0;
    forn(i, m) {
        char c;
        int x, y;
        cin >> c >> x >> y;
        x--, y--;
        s[x][y] = c;
        if (c == '+' || c == 'o') {
            cost++;
            es.del(x + y, x - y + n - 1);
        }
        if (c == 'x' || c == 'o') {
            cost++;
            rs.del(x, y);
        }
    }
    vector<vector<char>> t = s;
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            rs.addEdge(x, y);
            es.addEdge(x + y, x - y + n - 1);
        }
    }
    rs.findMatching();
    for (cell c : rs.m) {
        cost++;
        if (t[c.x][c.y] == '.') {
            t[c.x][c.y] = 'x';
        } else {
            t[c.x][c.y] = 'o';
        }
    }
    es.findMatching();
    for (cell c : es.m) {
        cost++;
        c.y = (c.x - c.y + (n - 1))/2;
        c.x -= c.y;
        assert(c.x >= 0 && c.x < n);
        assert(c.y >= 0 && c.y < n);

        if (t[c.x][c.y] == '.') {
            t[c.x][c.y] = '+';
        } else {
            t[c.x][c.y] = 'o';
        }
    }
    vector<tuple<char, int, int>> ans;
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            if (t[x][y] != s[x][y]) {
                ans.push_back(make_tuple(t[x][y], x + 1, y + 1));
            }
        }
    }
    cout << cost << ' ' << ans.size() << '\n';
    for (auto t : ans) {
        cout << get<0>(t) << ' ' << get<1>(t) << ' ' << get<2>(t) << '\n';
    }
}

int main() {
#ifdef LOCAL
    freopen("d.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(i, T) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}

