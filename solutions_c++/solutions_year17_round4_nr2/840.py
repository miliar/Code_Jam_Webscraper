// Kappa 123
#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "file"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);
//--------------- Min-Cost Max-Flow (Dijkstra) ---------------//
const int MAXN = 1010; // NUMBER OF VERTICES
int k = INF; // REQUIRED FLOW (INF IF MAX FLOW)
int maxFlow = 0; // RESULTING FLOW WILL BE HERE
int minCost = 0; // RESULTING COST WILL BE HERE
struct edge
{
    int a, b, cap, flow, cost, origCost;
};
vector<edge> edges;
vector<int> g[MAXN];
int pot[MAXN];
int parent[MAXN];
bool used[MAXN];
void add_edge(int a, int b, int u, int c)
{
    edge e1 = {a, b, u, 0, c, c};
    edge e2 = {b, a, 0, 0, -c, -c};
    g[a].pb(edges.size());
    edges.pb(e1);
    g[b].pb(edges.size());
    edges.pb(e2);
}
void bellman_ford(int s, int t)
{
    for(int i = 0; i < MAXN; i++)
        pot[i] = INF;
    pot[s] = 0;
    for(int iter = 0; iter < MAXN - 1; iter++)
    {
        for(int v = 0; v < MAXN; v++)
        {
            if(pot[v] < INF)
            {
                for(int i = 0; i < g[v].size(); i++)
                {
                    int id = g[v][i];
                    if(pot[edges[id].b] > pot[v] + edges[id].cost && edges[id].cap - edges[id].flow > 0)
                        pot[edges[id].b] = pot[v] + edges[id].cost;
                }
            }
        }
    }
}
bool dijkstra(int s, int t)
{
    for(int i = 0; i < MAXN; i++)
        parent[i] = -1, pot[i] = INF, used[i] = 0;
    pot[s] = 0;
    for(int i = 0; i < MAXN; i++) // use this for dense graphs, change to priority_queue for sparse graphs
    {
        int v = -1;
        for(int j = 0; j < MAXN; j++)
            if(!used[j] && (v == -1 || pot[j] < pot[v]))
                v = j;
        if(pot[v] == INF)
            break;
        used[v] = 1;
        for(int j = 0; j < g[v].size(); j++)
        {
            int id = g[v][j];
            int to = edges[id].b;
            if(edges[id].cap - edges[id].flow > 0 && !used[to])
            {
                if(parent[to] == -1 || pot[to] > pot[v] + edges[id].cost)
                {
                    parent[to] = id;
                    pot[to] = pot[v] + edges[id].cost;
                }
            }
        }
    }
    return parent[t] != -1;
}
void reduce()
{
    for(int i = 0; i < MAXN; i++)
    {
        if(pot[i] != INF)
        {
            for(int j = 0; j < g[i].size(); j++)
            {
                int id = g[i][j];
                int to = edges[id].b;
                if(edges[id].cap - edges[id].flow > 0)
                    edges[id].cost += pot[i] - pot[to];
                else
                    edges[id].cost = 0;
            }
        }
    }
}
void MCMF(int s, int t)
{
    bellman_ford(s, t);
    reduce();
    while(maxFlow < k)
    {
        if(dijkstra(s, t))
        {
            reduce();
            int cur = t, d = INF;
            while(cur != s)
            {
                int id = parent[cur];
                d = min(d, edges[id].cap - edges[id].flow);
                cur = edges[id].a;
            }
            cur = t;
            while(cur != s)
            {
                int id = parent[cur];
                edges[id].flow += d;
                edges[id ^ 1].flow -= d;
                cur = edges[id].a;
            }
            maxFlow += d;
        }
        else
            break;
    }
    for(auto e: edges)
        if(e.flow > 0)
            minCost += e.origCost * e.flow;
}
//------------------------------------------------------------//

int posL[1010], posR[1010];

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++)
    {
        cerr << tcase << endl;
        edges.clear();
        for(int i = 0; i < MAXN; i++)
        {
            g[i].clear();
            parent[i] = 0;
            used[i] = 0;
            pot[i] = 0;
        }
        int n, m, c;
        cin >> n >> c >> m;
        int L = 0, R = 0;
        for(int i = 0; i < m; i++)
        {
            int p, b;
            cin >> p >> b;
            if(b == 1)
                posL[L++] = p;
            else
                posR[R++] = p;
        }
        for(int i = 0; i < L; i++)
        {
            for(int j = 0; j < R; j++)
            {
                if(posL[i] == 1 && posR[j] == 1)
                    continue;
                int cost = (posL[i] == posR[j]);
                add_edge(i + 1, L + j + 1, 1, cost);
            }
        }
        for(int i = 0; i < R; i++)
            add_edge(L + i + 1, L + R + 1, 1, 0);
        for(int i = 0; i < L; i++)
            add_edge(0, i + 1, 1, 0);
        maxFlow = 0;
        minCost = 0;
        MCMF(0, L + R + 1);
        cout << "Case #" << tcase << ": " << L + R - maxFlow << " " << minCost << '\n';
    }
    return 0;
}
