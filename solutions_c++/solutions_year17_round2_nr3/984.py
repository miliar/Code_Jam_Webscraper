#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;

const int maxn = 100 + 5;
const ll INFD = 1LL << 58;
const double INF = 1e15;
const double eps = 1e-8;

double d[maxn];
ll g[maxn][maxn];
int e[maxn], s[maxn];
bool inq[maxn];

int dcmp(double x)
{
    if(fabs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

void floyd(int n)
{
    for(int k = 1; k <= n; ++k)
    {
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j) g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
        }
    }
}

double spfa(int n, int st, int ed)
{
    queue<int> que;
    fill(d + 1, d + n + 1, INF);
    memset(inq, 0, sizeof(inq));
    d[st] = 0;
    que.push(st);
    inq[st] = true;
    while(!que.empty())
    {
        int u = que.front();
        que.pop();
        inq[u] = false;
        for(int v = 1; v <= n; ++v)
        {
            if(g[u][v] > e[u]) continue;
            double tmp = d[u] + 1.0 * g[u][v] / s[u];
            if(dcmp(d[v] - tmp) > 0)
            {
                d[v] = tmp;
                if(!inq[v])
                {
                    que.push(v);
                    inq[v] = true;
                }
            }
        }
    }
    return d[ed];
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int n, q;
        scanf("%d%d", &n, &q);
        for(int i = 1; i <= n; ++i) scanf("%d%d", &e[i], &s[i]);
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j)
            {
                scanf("%lld", &g[i][j]);
                if(g[i][j] == -1) g[i][j] = INFD;
            }
        }
        floyd(n);
        printf("Case #%d:", ++cas);
        while(q--)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            printf(" %.10f", spfa(n, u, v));
        }
        puts("");
    }
    return 0;
}
