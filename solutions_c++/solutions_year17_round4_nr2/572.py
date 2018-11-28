#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cerr << #x " = " << (x) << '\n'
#define DBG         cerr << "Hi" << '\n'
#define pb          push_back
#define PI          acos(-1.00)
#define xx          first
#define yy          second
#define eps         1e-9
#define INF         inf
typedef long long int LL;
typedef double db;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
// Works only on directed Graph
// *** 0 based indexing
// MAXE = twice the number of edges
/// Zobayer vai's code

/// 1 based indexing
/// MAXE = twice the number of edges
/// for directed edge, cap[nEdge] = 0

const int MAXN = 2010, MAXE = 2100000; // MAXE = twice the number of edges
int src, snk, nNode, nEdge;
int Q[MAXN], fin[MAXN], pro[MAXN], dist[MAXN];
int flow[MAXE], cap[MAXE], nxt[MAXE], to[MAXE];
const int inf = 1e9;
inline void init(int _src, int _snk, int _n)
{
    src = _src, snk = _snk, nNode = _n, nEdge = 0;
    mem(fin, -1);
}

inline void add(int u, int v, int _cap)
{
    to[nEdge] = v, cap[nEdge] = _cap, flow[nEdge] = 0, nxt[nEdge] = fin[u], fin[u] = nEdge++;
    to[nEdge] = u, cap[nEdge] = 0, flow[nEdge] = 0, nxt[nEdge] = fin[v], fin[v] = nEdge++; // for directed cap[nEdge]=0 here
}

bool bfs()
{
    int st, en, i, u, v;
    mem(dist, -1);
    dist[src] = st = en = 0;
    Q[en++] = src;
    while(st < en)
    {
        u = Q[st++];
        for(i=fin[u]; i>=0; i=nxt[i])
        {
            v = to[i];
            if(flow[i] < cap[i] && dist[v]==-1)
            {
                dist[v] = dist[u]+1;
                Q[en++] = v;
            }
        }
    }
    return dist[snk]!=-1;
}

int dfs(int u, int fl)
{
    if(u==snk) return fl;
    for(int &e=pro[u], v, df; e>=0; e=nxt[e])
    {
        v = to[e];
        if(flow[e] < cap[e] && dist[v]==dist[u]+1)
        {
            df = dfs(v, min(cap[e]-flow[e], fl));
            if(df>0)
            {
                flow[e] += df;
                flow[e^1] -= df;
                return df;
            }
        }
    }
    return 0;
}

int dinitz()   // 1-based indexing
{
    int ret = 0;
    int df;
    while(bfs())
    {
        for(int i=1; i<=nNode; i++) pro[i] = fin[i];
        while(true)
        {
            df = dfs(src, inf);
            if(df) ret += df;
            else break;
        }
    }
    return ret;
}

int cnt[1010];
int ticket[1010][2], n, c, m;
void buildGraph(int x)
{
    int src = n+c+1, snk = src+1;
    init(src, snk, snk);
    for(int i = 1; i<=c; i++)
        add(src, i, cnt[i]);
    for(int i = 1; i<=n; i++)
        add(i+c,snk,x);
    for(int i = 1; i<=m; i++)
    {
        for(int j = 1; j<=ticket[i][1]; j++)
            add(ticket[i][0], j+c, 1);
    }
}

bool ok(int mid)
{
    buildGraph(mid);
    return dinitz() == m;
}

struct MCMF
{
// Works only on directed Graph
// *** 0 based indexing
// MAXE = twice the number of edges
    int src, snk, nNode, nEdge;
    int fin[MAXN], pre[MAXN], dist[MAXN];
    int cap[MAXE], cost[MAXE], Next[MAXE], to[MAXE], from[MAXE];


    inline void init(int _src, int _snk, int nodes)
    {
        memset(fin, -1, sizeof(fin));
        nNode = nodes, nEdge = 0;
        src = _src, snk = _snk;
    }

    inline void add(int u, int v, int _cap, int _cost)
    {
        from[nEdge] = u, to[nEdge] = v, cap[nEdge] = _cap, cost[nEdge] = _cost;
        Next[nEdge] = fin[u], fin[u] = nEdge++;
        from[nEdge] = v, to[nEdge] = u, cap[nEdge] = 0, cost[nEdge] = -(_cost);
        Next[nEdge] = fin[v], fin[v] = nEdge++;
        assert(nEdge <= MAXE);
    }

    bool bellman()
    {
        int iter, u, v, i;
        bool flag = true;
        memset(dist, 0x7f, sizeof(dist));
        memset(pre, -1, sizeof(pre));
        dist[src] = 0;
        for(iter = 1; iter < nNode && flag; iter++)
        {
            flag = false;
            for(u = 0; u < nNode; u++)
            {
                for(i = fin[u]; i >= 0; i = Next[i])
                {
                    v = to[i];
                    if(cap[i] && dist[v] > dist[u] + cost[i])
                    {
                        dist[v] = dist[u] + cost[i];
                        pre[v] = i;
                        flag = true;
                    }
                }
            }
        }
        return (dist[snk] < INF);
    }

    int mcmf(int &fcost)
    {
        int netflow, i, bot, u;
        netflow = fcost = 0;
        while(bellman())
        {
            bot = INF;
            for(u = pre[snk]; u >= 0; u = pre[from[u]]) bot = min(bot, cap[u]);
            for(u = pre[snk]; u >= 0; u = pre[from[u]])
            {
                cap[u] -= bot;
                cap[u^1] += bot;

                fcost += bot * cost[u];
            }
            netflow += bot;
        }
        return netflow;
    }

}my;

int go(int x)
{
    int src = n+c+1, snk = src+1;
    my.init(src, snk, snk);
    for(int i = 1; i<=c; i++)
        my.add(src, i, cnt[i], 0);
    for(int i = 1; i<=n; i++)
        my.add(i+c,snk,x,0);
    for(int i = 1; i<=m; i++)
    {
        for(int j = 1; j<ticket[i][1]; j++)
            my.add(ticket[i][0], j+c, 1, 1);
        my.add(ticket[i][0], ticket[i][1]+c, 1, 0);
    }
    int ret;
    my.mcmf(ret);
    return ret;
}

pii solve(int lo)
{
    int hi = 1005, mid, ans;
    while(lo < hi)
    {
        mid = (lo+hi)/2;
        if(ok(mid))
            hi = mid;
        else
            lo = mid+1;
    }
    ans = lo;
    pii ret;
    ret.xx = ans;
    ret.yy = go(ans);
    return ret;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, cs, t;
    sf(t);
    FRE(cs,1,t)
    {
        D(cs);
        mem(cnt,0);
        sfff(n,c,m);
        int mx = 0;
        FRE(i,1,m)
        {
            sff(ticket[i][1], ticket[i][0]);
            cnt[ticket[i][0]]++;
            mx = max(cnt[ticket[i][0]], mx);
        }

        pii ans = solve(mx);
        printf("Case #%d: %d %d\n",cs,ans.xx,ans.yy);
    }
    return 0;
}


