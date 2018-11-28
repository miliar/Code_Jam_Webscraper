#include<bits/stdc++.h>
using namespace std;



long long e[200],s[200];
long long d[200][200];
bool inq[200];
double dist[200];
int n,q;
double spfa(int ss,int tt)
{
    queue<int>q;
    q.push(ss);
    for(int i=1;i<=n;i++)
        dist[i]=1e60,inq[i]=0;
    dist[ss]=0.0;
    while(!q.empty())
    {
        int x=q.front();
        q.pop();
        inq[x]=0;
        for(int i=1;i<=n;i++)
            if(d[x][i]<=e[x])
            {
                double t=1.0*d[x][i]/s[x];
                if(dist[i]>dist[x]+t)
                {
                    dist[i]=dist[x]+t;
                    if(inq[i]==0)
                        inq[i]=1,q.push(i);
                }
            }
    }
    return dist[tt];
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d:",ti++);
        scanf("%d%d",&n,&q);
        for(int i=1;i<=n;i++)
            scanf("%lld%lld",e+i,s+i);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                scanf("%lld",&d[i][j]);
                if(d[i][j]==-1)
                    d[i][j]=1ll<<60;
            }
        for(int k=1;k<=n;k++)
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    d[i][j]=min(d[i][k]+d[k][j],d[i][j]);
        while(q--)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            printf(" %.8f",spfa(x,y));
        }
        puts("");
    }
	return 0;
}
