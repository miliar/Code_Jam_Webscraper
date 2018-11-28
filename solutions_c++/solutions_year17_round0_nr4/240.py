#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <random>
#include <vector>
#include <array>
#include <bitset>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

using namespace std;
using ll = long long;
using ull = unsigned long long;
constexpr ll TEN(int n) { return (n==0) ? 1 : 10*TEN(n-1); }
template<class T> using V = vector<T>;
template<class T> using VV = V<V<T>>;
int bsr(int x) { return 31 - __builtin_clz(x); }

template <class E>
using Graph = vector<vector<E>>;

template<class C, C INF> // Cap
struct MaxFlow {
    int V;
    vector<int> level, iter;
    //gを破壊するので注意
    template<class E>
    C exec(Graph<E> &g, int s, int t) {
        V = (int)g.size();
        level.resize(V);
        iter.resize(V);
        C flow = 0;
        while (true) {
            bfs(g, s);
            if (level[t] < 0) return flow;
            fill_n(iter.begin(), V, 0);
            while (true) {
                C f = dfs(g, s, t, INF);
                if (!f) break;
                flow += f;
            }
        }
    }

    template<class E>
    void bfs(const Graph<E> &g, int s) {
        fill_n(level.begin(), V, -1);
        queue<int> que;
        level[s] = 0;
        que.push(s);
        while (!que.empty()) {
            int v = que.front(); que.pop();
            for (E e: g[v]) {
                if (e.cap <= 0) continue;
                if (level[e.to] < 0) {
                    level[e.to] = level[v] + 1;
                    que.push(e.to);
                }
            }
        }
    }

    template<class E>
    C dfs(Graph<E> &g, int v, int t, C f) {
        if (v == t) return f;
        for (int &i = iter[v]; i < (int)g[v].size(); i++) {
            E &e = g[v][i];
            if (e.cap <= 0) continue;
            if (level[v] < level[e.to]) {
                C d = dfs(g, e.to, t, min(f, e.cap));
                if (d <= 0) continue;
                e.cap -= d;
                g[e.to][e.rev].cap += d;
                return d;
            }
        }
        return 0;
    }
};

struct Edge {
    int to, cap, rev;
};

void add_edge(Graph<Edge> &g, int from, int to, int cap) {
    g[from].push_back(Edge{to, cap, (int)g[to].size()});
    g[to].push_back(Edge{from, 0, (int)g[from].size()-1});
}

using P = pair<int, int>;

V<P> calc(int n, VV<bool> g, V<bool> row, V<bool> col) {
    assert(g.size() == n);
    assert(g[0].size() == n);
    assert(row.size() == n);
    assert(col.size() == n);
    Graph<Edge> f(2*n+2);
    int sv = 2*n, tv = sv+1;
    for (int i = 0; i < n; i++) {
        if (row[i]) continue;
        add_edge(f, sv, i, 1);
    }
    for (int i = 0; i < n; i++) {
        if (col[i]) continue;
        add_edge(f, n+i, tv, 1);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g[i][j]) continue;
            add_edge(f, i, n+j, 1);
        }
    }
    MaxFlow<int, TEN(8)> mf;
    mf.exec(f, sv, tv);
    V<P> res;
    for (int i = 0; i < n; i++) {
        for (auto e: f[i]) {
            int j = e.to;
            if (n <= j && j < 2*n && e.cap == 0) {
                res.push_back(P(j-n, i));
            }
        }
    }
    return res;
}

int n, m;
V<char> cv;
V<int> xv, yv;
VV<bool> res1, res2;

int calc1() {
    VV<bool> g = VV<bool>(n, V<bool>(n));
    V<bool> row(n), col(n);
    for (int i = 0; i < m; i++) {
        char c = cv[i];
        int x = xv[i];
        int y = yv[i];
        if (c != '+') {
            row[y] = true;
            col[x] = true;
        }
    }
    auto res = calc(n, g, row, col);
/*    for (auto p: res) {
        cout << p.first << " " << p.second << endl;
    }*/
    res1 = VV<bool>(n, V<bool>(n));
    for (auto p: res) {
        res1[p.second][p.first] = true;
    }
    return int(res.size());
}
int calc2() {
    VV<bool> g = VV<bool>(2*n-1, V<bool>(2*n-1, true));
    V<bool> row(2*n-1), col(2*n-1);
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            int nx = x-y+n-1;
            int ny = x+y;
            g[ny][nx] = false;
        }
    }


    for (int i = 0; i < m; i++) {
        char c = cv[i];
        int x = xv[i];
        int y = yv[i];
        int nx = x-y+n-1;
        int ny = x+y;
        if (c != 'x') {
            row[ny] = true;
            col[nx] = true;
        }
    }
    auto res = calc(2*n-1, g, row, col);
/*    for (auto p: res) {
        int nx = p.first, ny = p.second;
        int x = (nx+ny-(n-1))/2;
        int y = (ny-nx+(n-1))/2;
        cout << x << " " << y << endl;
    }*/
    res2 = VV<bool>(n, V<bool>(n));
    for (auto p: res) {
        int nx = p.first, ny = p.second;
        int x = (nx+ny-(n-1))/2;
        int y = (ny-nx+(n-1))/2;
        res2[y][x] = true;        
    }
    return int(res.size());
}

void solve() {
    cin >> n >> m;
    res1 = VV<bool>(n);
    res2 = VV<bool>(n);
    cv = V<char>(m);
    xv = V<int>(m);
    yv = V<int>(m);
    int ans = m;
    VV<char> first = VV<char>(n, V<char>(n, '.'));
    for (int i = 0; i < m; i++) {
        cin >> cv[i] >> yv[i] >> xv[i];
        xv[i]--; yv[i]--;
        if (cv[i] == 'o') ans++;
        first[yv[i]][xv[i]] = cv[i];
    }
    ans += calc1();
    ans += calc2();

/*    cout << "debug 1" << endl;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cout << (res1[y][x] ? '#' : '.');
        }
        cout << endl;
    }
    cout << "debug 2" << endl;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cout << (res2[y][x] ? '#' : '.');
        }
        cout << endl;
    }*/
    struct Q {
        char c;
        int x, y;
    };
    V<Q> buf;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            bool f1 = res1[y][x];
            bool f2 = res2[y][x];
            if (first[y][x] == 'x' || first[y][x] == 'o') f1 = true;
            if (first[y][x] == '+' || first[y][x] == 'o') f2 = true;
            char c;
            if (f1 && f2) c = 'o';
            else if (f1) c = 'x';
            else if (f2) c = '+';
            else c = '.';
//            cout << c;
            if (c != first[y][x]) {
                buf.push_back(Q{c, x, y});
            }
        }
//        cout << endl;
    }

    cout << ans << " " << buf.size() << endl;
    for (auto q: buf) {
        cout << q.c << " " << q.y+1 << " " << q.x+1 << endl;
    }
}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }
    return 0;
}
