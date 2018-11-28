#include<bits/stdc++.h>
using namespace std;

#define MAX 110
#define eps 1e-9

typedef long long ll;

double e[MAX],s[MAX],dis[MAX][MAX],dp[MAX][MAX];
ll n;

void floyd(int n)
{
    int i,j,k;
    ll curr;
    for(k=1; k<=n; ++k)
    {
        for(i=1; i<=n; ++i)
        {
            for(j=1; j<=n; ++j)
            {
                if(dis[i][k]==-1 || dis[k][j] ==-1)
                    continue;
                curr = dis[i][k]+dis[k][j];
                if(dis[i][j]==-1 || curr<dis[i][j])
                    dis[i][j]=curr;
            }
        }
    }
}

double cal(ll i, ll h)
{
    if(i==n)
        return 0;
    if(dp[i][h]>eps)
        return dp[i][h];
    //printf("%lld %lld\n",i,h);
    double ret1,ret2;
    ret1=ret2=9999999999999;
  //ret1=ret2=-1;
    if(dis[h][i+1]<=s[h])
        ret1=cal(i+1,h)+(dis[i][i+1]/e[h]);
    if(dis[i][i+1]<=s[i])
        ret2=cal(i+1,i)+(dis[i][i+1]/e[i]);
    //if(i==2 && h==1)
     //   printf("%lf %lf %lld %lld\n",e[i],cal(i+1,i),i,h);
    return dp[i][h]=min(ret1,ret2);
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,ti,i,j,k,q,u,v;
    scanf("%lld",&t);
    for(ti=1; ti<=t; ++ti)
    {
        memset(dis,0,sizeof(dis));
        memset(dp,-1,sizeof(dp));
        scanf("%lld %lld",&n,&q);
        for(i=1; i<=n; ++i)
            scanf("%lf %lf",&s[i], &e[i]);
        for(i=1; i<=n; ++i)
        {
            for(j=1; j<=n; ++j)
                scanf("%lf",&dis[i][j]);
        }
        floyd(n);
     /*   for(i=1; i<=n; ++i)
        {
            for(j=1; j<=n; ++j)
                printf("%lf ",dis[i][j]);
            puts("");
        }*/
        while(q--)
        {
            scanf("%lld %lld",&u,&v);
            printf("Case #%lld: %.8lf\n",ti,cal(1,1));
       }
    }
    return 0;
}
