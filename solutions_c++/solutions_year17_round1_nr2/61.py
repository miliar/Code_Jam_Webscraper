#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <memory.h>
#include <iomanip>

using namespace std;

const int MAXN = 2050;
const int INF = 1000000000;

int le[MAXN], ri[MAXN];
int c[MAXN];
int a[MAXN][MAXN];
int num[MAXN][MAXN];

struct edge {
    int a, b, cap, flow;
};

int s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];

void add_edge (int a, int b, int cap) {
    edge e1 = { a, b, cap, 0 };
    edge e2 = { b, a, 0, 0 };
    g[a].push_back ((int) e.size());
    e.push_back (e1);
    g[b].push_back ((int) e.size());
    e.push_back (e2);
}

bool bfs(int n) {
    int qh=0, qt=0;
    q[qt++] = s;
    memset (d, -1, n * sizeof d[0]);
    d[s] = 0;
    while (qh < qt && d[t] == -1) {
        int v = q[qh++];
        for (size_t i=0; i<g[v].size(); ++i) {
            int id = g[v][i],
                    to = e[id].b;
            if (d[to] == -1 && e[id].flow < e[id].cap) {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
        }
    }
    return d[t] != -1;
}

int dfs (int v, int flow) {
    if (!flow)  return 0;
    if (v == t)  return flow;
    for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
        int id = g[v][ptr[v]],
                to = e[id].b;
        if (d[to] != d[v] + 1)  continue;
        int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
        if (pushed) {
            e[id].flow += pushed;
            e[id^1].flow -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic(int n) {
    int flow = 0;
    for (;;) {
        if (!bfs(n))  break;
        memset (ptr, 0, n * sizeof ptr[0]);
        while (int pushed = dfs (s, INF))
            flow += pushed;
    }
    return flow;
}


double get_percent(int x, int y) {
    return 1.0 * y / (1.0 * x);
}

bool inter(int x, int y, int xx, int yy) {
    return max(x, xx) <= min(y, yy);
}

int solve() {
    e.clear();
    for (int i = 0; i < MAXN; i++) {
        g[i].clear();
    }
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &c[i]);
    }
    int id = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
            num[i][j] = ++id;
            int x = (int)(1.0 * a[i][j] / 0.9 / (1.0 * c[i]));
            while (x > 0 && get_percent(x * c[i], a[i][j]) < 0.9) {
                --x;
            }
            le[id] = ri[id] = -1;
            if (get_percent(x * c[i], a[i][j]) > 1.1) {
                continue;
            }
            le[id] = x;
            x = (int)(1.0 * a[i][j] / 1.1 / (1.0 * c[i]));
            while (get_percent(x * c[i], a[i][j]) > 1.1) {
                ++x;
            }
            if (get_percent(x * c[i], a[i][j]) < 0.9) {
                le[id] = ri[id] = -1;
                continue;
            }
            ri[id] = x;
            swap(le[id], ri[id]);
           // cout << le[id] << " " << ri[id] << "?" << endl;
        }
    }
    s = 0;
    t = id + 1;
    for (int i = 1; i <= m; i++) {
        if (le[i] != -1) add_edge(0, i, 1);
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= m; j++) {
            for (int jj = 1; jj <= m; jj++) {
                int px = num[i][j];
                int py = num[i + 1][jj];
                if (le[px] == -1 || le[py] == -1) continue;
                if (inter(le[px], ri[px], le[py], ri[py])) {
                    add_edge(px, py, 1);
                   // cout << i << " " << j << " " << jj << "!" << endl;
                }
            }
        }
    }
    for (int j = 1; j <= m; j++) {
        if (le[num[n][j]] != -1) add_edge(num[n][j], t, 1);
    }
    return dinic(id + 2);
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d", &tc);
    for (int i = 1; i <= tc; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}