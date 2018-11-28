#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define LL long long

const double DINF=(double)1e50;
const LL LINF=(LL) 1e18;

const int N=(int)100+10;

int n,q;
int E[N],S[N];
LL G[N][N];

double Time[N][N];

double dis[N];
int inq[N];
void spfa(int st,double *arr)
{
    queue<int> Q;
    for(int i=1;i<=n;i++) arr[i]=DINF;

    arr[st]=0.0;
    inq[st]=1;
    Q.push(st);
    while(!Q.empty())
    {
        int u=Q.front(); Q.pop(); inq[u]=0;
        for(int i=1;i<=n;i++)
        {
            if(G[u][i]>E[u]) continue;
            double ti=(double)G[u][i]/S[u];
            if(arr[i]>ti+arr[u])
            {
                arr[i]=ti+arr[u];
                if(!inq[i]) inq[i]=1, Q.push(i);
            }
        }
    }
}

void work()
{
    int tc; scanf("%d",&tc);
    int T_T=0;
    while(tc--)
    {
        scanf("%d%d",&n,&q);
        for(int i=1;i<=n;i++)
            scanf("%d%d",&E[i],&S[i]);

        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                int x; scanf("%d",&x);
                G[i][j]=x;
                if(x==-1) G[i][j]=LINF;
            }

        for(int k=1;k<=n;k++)
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    G[i][j]=min(G[i][j],G[i][k]+G[k][j]);


//        for(int i=1;i<=n;i++)
//        {
//            for(int j=1;j<=n;j++)
//            {
//                if(G[i][j]>=LINF) printf("-1 ");
//                else printf("%lld ",G[i][j]);
//            }
//            puts("");
//        }

        for(int i=1;i<=n;i++) spfa(i,Time[i]);

        printf("Case #%d:",++T_T);
        while(q--)
        {
            int st,ed; scanf("%d%d",&st,&ed);
            printf(" %.12lf",Time[st][ed]);
        }
        puts("");
    }
}

int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
