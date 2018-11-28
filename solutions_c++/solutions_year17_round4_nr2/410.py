#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for (int i = 0; i < len; i++) cerr << arr[i] << " "; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for (const auto &e : it) cerr << e << " "; cerr << endl;}
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0
#define print_iterable(it) (void)0
#endif

typedef long long ll;
const int N = 1005;
const int V = 2 * N;
const int INF = (int)1e9;

struct Edge
{
    int to, flow, cap, cost;
    Edge(): to(), flow(), cap(), cost() {}
    Edge(int _to, int _cap, int _cost): to(_to), flow(), cap(_cap), cost(_cost) {}
};

int n, c, m;
int guy_deg[N], tick_deg[N];
int last_cost;

int gs, gt, vcnt;
vector<int> go[V];
vector<Edge> edges;
int dist[V];
int q[V], ql, qr;
bool in_q[V];
int par_v[V], par_e[V];

void add_edge(int a, int b, int cap, int cost)
{
    go[a].push_back(edges.size());
    edges.emplace_back(b, cap, cost);
    go[b].push_back(edges.size());
    edges.emplace_back(a, 0, -cost);
}

void q_push(int v)
{
    if (in_q[v])
        return;
    in_q[v] = true;
    q[qr++] = v;
    if (qr == V)
        qr = 0;
}

int q_pop()
{
    int v = q[ql++];
    if (ql == V)
        ql = 0;
    in_q[v] = false;
    return v;
}

int spfa()
{
    fill(dist, dist + vcnt, INF);
    dist[gs] = 0;
    q_push(gs);

    while (ql != qr)
    {
        int v = q_pop();
        for (int eid : go[v])
        {
            auto e = edges[eid];
            if (e.flow == e.cap)
                continue;
            if (dist[e.to] <= dist[v] + e.cost)
                continue;
            dist[e.to] = dist[v] + e.cost;
            par_v[e.to] = v;
            par_e[e.to] = eid;
            q_push(e.to);
        }
    }

    if (dist[gt] == INF)
        return 0;

    int flow = INF;
    for (int v = gt; v != gs; v = par_v[v])
    {
        int eid = par_e[v];
        auto e = edges[eid];
        flow = min(flow, e.cap - e.flow);
    }
    for (int v = gt; v != gs; v = par_v[v])
    {
        int eid = par_e[v];
        edges[eid].flow += flow;
        edges[eid ^ 1].flow -= flow;
    }

    return flow;
}

bool good(int ans)
{
    gs = 2 * n;
    gt = gs + 1;
    vcnt = gt + 1;
    for (int i = 0; i < vcnt; i++)
        go[i].clear();
    edges.clear();

    for (int i = 0; i < n; i++)
    {
        add_edge(i, n + i, INF, 1);
        add_edge(n + i, i, INF, 0);
        if (i > 0)
            add_edge(n + i, n + i - 1, INF, 0);
    }
    for (int i = 0; i < n; i++)
    {
        add_edge(gs, i, tick_deg[i], 0);
        add_edge(i, gt, ans, 0);
    }

    int total = 0, cur;
    while ((cur = spfa()) > 0)
        total += cur;

    if (total != m)
        return false;

    last_cost = 0;
    for (int v = 0; v < vcnt; v++)
        for (int eid : go[v])
        {
            auto e = edges[eid];
            if (e.cap > 0)
                last_cost += e.flow * e.cost;
        }
    return true;
}

void solve()
{
    scanf("%d%d%d", &n, &c, &m);

    fill(tick_deg, tick_deg + n, 0);
    fill(guy_deg, guy_deg + c, 0);

    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        a--, b--;
        tick_deg[a]++;
        guy_deg[b]++;
    }

    int left = -1;
    for (int i = 0; i < c; i++)
        left = max(left, guy_deg[i] - 1);
    int right = m;

    while (right - left > 1)
    {
        int mid = (left + right) / 2;
        if (good(mid))
            right = mid;
        else
            left = mid;
    }

    if (!good(right))
        throw;
    printf("%d %d\n", right, last_cost);
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("\n\ntime = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
