#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"
#include "vector"
#include "map"
#include "set"
#include "algorithm"
#include "queue"
#include "cmath"
#include <typeinfo>
#include "unordered_set"

#define ll long long
#define ull unsigned long long

const int MAX = 8000 + 100;

struct MCMF
{
    struct Edge
    {
        int from,to,cap,flow,cost;
        Edge() {}
        Edge(int _from,int _to,int _cap,int _flow,int _cost):
            from(_from),to(_to),cap(_cap),flow(_flow),cost(_cost) {}
    };
    int n,m,s,t;
    std::vector<Edge> edge;
    std::vector<int> G[MAX];
    bool inq[MAX];
    int d[MAX],p[MAX],fc[MAX];

    void init(int _n,int _s,int _t)
    {
        n=_n; s=_s; t=_t; m=0;
        edge.clear();
        for(int i = 0; i <= n; i++)
        {
            G[i].clear();
        }
    }

    void AddEdge(int from,int to,int cap,int cost)
    {
        edge.push_back(Edge(from,to,cap,0,cost));
        edge.push_back(Edge(to,from,0,0,-cost));
        m += 2;
        G[from].push_back(m-2);
        G[to].push_back(m-1);
    }

    bool spfa(int& flow, int& cost)
    {
        for (int i = 0; i <= n; i++)
        {
            d[i] = 2000000000;
        }
        memset(inq,0,sizeof(inq));
        d[s] = 0;
        inq[s] = true;
        p[s] = 0;
        fc[s] = 2000000000;
        int a[MAX], b[MAX];

        std::queue<int> que;
        que.push(s);
        while (!que.empty())
        {
            int x = que.front();
            que.pop();
            inq[x]=0;
            for (int i = 0; i < G[x].size(); i++)
            {
                Edge&e = edge[G[x][i]];
                if(e.cap > e.flow && d[e.to] > d[x] + e.cost)
                {
                    d[e.to] = d[x]+e.cost;
                    p[e.to] = G[x][i];
                    fc[e.to] = std::min(fc[x], e.cap - e.flow);
                    if (!inq[e.to])
                    {
                        que.push(e.to);
                        inq[e.to] = true;
                    }
                }
            }
        }
        if (d[t] == 2000000000)
        {
            return 0;
        }
        flow += fc[t];
        cost += fc[t] * d[t];
        int tmp = t;
        while (tmp != s)
        {
            edge[p[tmp]].flow += fc[t];
            edge[p[tmp]^1].flow -= fc[t];
            tmp = edge[p[tmp]].from;
        }

        return 1;
    }

    void GetMincost(int& flow,int& cost)
    {
        flow = 0;
        cost = 0;
        while(spfa(flow,cost))
        {}
    }
};

int N,M,C;
int a[MAX], b[MAX];

MCMF mcmf;

void AddEdge(int mid)
{
    int start = C+M+N+N+1, ed = C+M+N+N+2;

    mcmf.init(ed, start, ed);

    for(int i = 1; i <= C; i++)
    {
        mcmf.AddEdge(start, i, mid, 0);
    }
    for(int i = 1; i <= M; i++)
    {
        mcmf.AddEdge(b[i], C+i,1,0);
        mcmf.AddEdge(C + i, C + M + a[i] + N, 1, 0);
        mcmf.AddEdge(C + i, C + M + a[i], 1, 1);
    }
    for(int i = 1; i < N; i++)
    {
        mcmf.AddEdge(C + M + i + 1, C + M + i, 2000000000, 0);
    }
    for(int i = 1; i <= N; i++)
    {
        mcmf.AddEdge(C+M+i, C+M+N+i, 2000000000, 0);
    }
    for(int i = 1; i <= N; i++)
    {
        mcmf.AddEdge(C + M + N + i, ed, mid, 0);
    }
}


int main()
{
    freopen("B-large (1).in", "r", stdin);
//    freopen("C-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d%d%d", &N, &C, &M);
        for (int i = 1; i <= M; i++)
        {
            scanf("%d%d", &a[i], &b[i]);
        }
        int left = 1, right = M;
        int mid, ans1 = 0, ans2 = 0;
        while (left <= right)
        {
            mid = left + right >> 1;
            AddEdge(mid);
            int tmpFlow, tmpCost;
            mcmf.GetMincost(tmpFlow, tmpCost);
            if (tmpFlow == M)
            {
                right = mid - 1;
                ans1 = mid;
                ans2 = tmpCost;
            }
            else
            {
                left = mid + 1;
            }
        }

        printf("Case #%d: %d %d\n", cas++, ans1, ans2);
    }
	return true;
}
