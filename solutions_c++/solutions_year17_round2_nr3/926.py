#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;
typedef long long ll;
const int maxn = 200;



double mpt[maxn];
bool vis[maxn];
bool inq[maxn];


double ans[maxn];

ll ab[maxn],sp[maxn];
ll mp[maxn][maxn];

int n,Q_Q;
void spfa(int st)
{
    queue<int> que;
    memset(inq,0,sizeof(inq));
    memset(vis,0,sizeof(vis));

    vis[st] = 1;
    mpt[st] = 0;
    inq[st] = 1;
    que.push(st);

    while(!que.empty())
    {
        int now = que.front();
        que.pop();
        inq[now] = 0;

        for (int x = 1; x <= n; x++)
        {
            if (now == x) continue;
            if (mp[now][x] == -1 ) continue;
            if(mp[now][x] > ab[now]) continue;
            double cost = 1.0*mp[now][x]/(1.0*sp[now]);
            if (!vis[x])
            {
                vis[x] = 1;
                mpt[x] = mpt[now]+cost;
                if (!inq[x])
                {
                    que.push(x);
                    inq[x] = 1;
                }
            }
            else if(mpt[x] > mpt[now]+cost)
            {
            	                vis[x] = 1;
                mpt[x] = mpt[now]+cost;
                if (!inq[x])
                {
                    que.push(x);
                    inq[x] = 1;
                }
            }
        }
    }
}

int main()
{

    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int ca = 0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&Q_Q);
        for (int i = 1; i <= n; i++)
            scanf("%lld%lld",&ab[i],&sp[i]);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                scanf("%lld",&mp[i][j]);

        for (int k = 1; k <= n; k++)
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                {
                    if (i == j) continue;
                    if (mp[i][k] == -1 || mp[k][j] == -1) continue;
                    if (mp[i][j] == -1 || mp[i][j] > mp[i][k]+mp[k][j]) mp[i][j] = mp[i][k]+mp[k][j];
                }
        int u,v;
        for (int i = 1; i <= Q_Q; i++)
        {
            scanf("%d%d",&u,&v);
            spfa(u);
            ans[i] = mpt[v];
        }
        printf("Case #%d: ",++ca);
        for (int i = 1; i < Q_Q; i++) printf("%.8f ",ans[i]);
        printf("%.8f\n",ans[Q_Q]);
    }
    return 0;
}
