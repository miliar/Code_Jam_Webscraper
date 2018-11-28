#include <bits/stdc++.h>
using namespace std;

#define INF 0X3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define MOD 1000000007
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define sz(X) int((X).size())
#define all(X) (X).begin(), (X).end()
#define rall(X) (X).rbegin(), (X).rend()
#define pow2(X) ((X)*(X))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int N = 64;

struct Edge {
    int v, c, f, next;
    Edge() {}
    Edge(int v, int c, int f, int next) : v(v), c(c), f(f), next(next) {}
};

#define MAXN 11123
#define MAXM 111234

int n, m, head[MAXN], lvl[MAXN], src, snk, work[MAXN];
Edge e[MAXM];

void init(int _n, int _src, int _snk) {
    n = _n;
    m = 0;
    src = _src;
    snk = _snk;
    memset(head, -1, sizeof(head));
}

void addEdge(int u, int v, int c) {
    e[m] = Edge(v, c, 0, head[u]);
    head[u] = m++;
    e[m] = Edge(u, 0, 0, head[v]);
    head[v] = m++;
}

bool bfs() {
    queue<int> q;
    memset(lvl, -1, n * sizeof(int));
    lvl[src] = 0;
    q.push(src);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int i = head[u]; i != -1; i = e[i].next) {
            if (e[i].f < e[i].c && lvl[e[i].v] == -1) {
                lvl[e[i].v] = lvl[u] + 1;
                q.push(e[i].v);
                if (e[i].v == snk)
                    return 1;
            }
        }
    }
    return 0;
}

int dfs(int u, int f) {
    if (u == snk)
        return f;
    for (int &i = work[u]; i != -1; i = e[i].next) {
        if (e[i].f < e[i].c && lvl[u] + 1 == lvl[e[i].v]) {
            int minf = dfs(e[i].v, min(f, e[i].c - e[i].f));
            if (minf > 0) {
                e[i].f += minf;
                e[i^1].f -= minf;
                return minf;
            }
        }
    }
    return 0;
}

int dinic() {
    int f, ret = 0;
    while (bfs()) {
        memcpy(work, head, n * sizeof(int));
        while (f = dfs(src, INF))
            ret += f;
    }
    return ret;
}

// check if [a,b] and [c,d] intersects
int intersects(int a, int b, int c, int d) {
    if (c > b) return 0;
    if (a > d) return 0;
    return 1;
}

int main() {
    int tt, n, p, v[N], q[N][N], l[N][N], r[N][N];
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%d %d", &n, &p);
        for (int i = 1; i <= n; i++)
            scanf("%d", &v[i]);
        for (int j = 1; j <= n; j++) {
            for (int i = 1; i <= p; i++) {
                scanf("%d", &q[i][j]);
                l[i][j] = ceil((double)q[i][j]/(1.1*v[j])-1e-8);
                r[i][j] = floor((double)q[i][j]/(0.9*v[j])+1e-8);
            }
        }
        init(n*p+2, 0, n*p+1);
        for (int i = 1; i <= p; i++) {
            if (l[i][1] <= r[i][1])
                addEdge(src, i, 1);
            if (l[i][n] <= r[i][n])
                addEdge((n-1)*p+i, snk, 1);
        }
        for (int j = 1; j < n; j++) {
            for (int i = 1; i <= p; i++) {
                if (l[i][j] > r[i][j]) continue;
                for (int k = 1; k <= p; k++) {
                    if (l[k][j+1] > r[k][j+1]) continue;
                    if (!intersects(l[i][j], r[i][j], l[k][j+1], r[k][j+1])) continue;
                    addEdge((j-1)*p + i, j*p + k, 1);
                }
            }
        }
        printf("Case #%d: %d\n", t, dinic());
    }
    return 0;
}