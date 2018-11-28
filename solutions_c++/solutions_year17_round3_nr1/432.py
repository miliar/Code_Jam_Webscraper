#include<bits/stdc++.h>
using namespace std;
double pi=2.00*acos(0.0);
struct info{
double r,h;
}ar[200000];

bool comp(info x,info y)
{
    return x.r>y.r;
}

int n,k;
double dp[2000][2000];
int vis[2000][2000];
double go(int p,int t)
{

    if(t==k) return 0;
    if(p>=n) return -100000000.00;
    if(vis[p][t]==1) return dp[p][t];
    dp[p][t]=max(go(p+1,t),2.00*pi*ar[p].r*ar[p].h+go(p+1,t+1));
    vis[p][t]=1;
    return dp[p][t];
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ts;
    scanf("%d",&ts);

    for(t=1;t<=ts;t++)
    {
        scanf("%d%d",&n,&k);
        for(int i=0;i<2000;i++)for(int j=0;j<2000;j++)
        {
            vis[i][j]=0;
        }
        double ans=0.00;
        for(int i=0;i<n;i++)
            scanf("%lf%lf",&ar[i].r,&ar[i].h);
        sort(ar,ar+n,comp);
        for(int i=0;i<n;i++)
        {
            ans=max(ans,pi*ar[i].r*ar[i].r+2.00*pi*ar[i].r*ar[i].h+go(i+1,1));
        }
        printf("Case #%d: %0.10lf\n",t,ans);
    }

}
