#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;
double dp[1005][1005];
double pi = acos(-1.0);
struct node
{
    int h,r;
    bool operator < (const node& u) const
    {
        return (r==u.r && h > u.h) || r > u.r;
    }
};
node nn[1005];
int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w", stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
        {
            scanf("%d%d",&nn[i].r,&nn[i].h);
        }
        sort(nn+1, nn+n+1);
        for(int i=0;i<=n;i++)
        for(int j=0;j<=k;j++) dp[i][j]=0;
        for(int i=0;i<n;i++)
        for(int j=0;j<=k;j++)
        {
            double xx = 2*pi*nn[i+1].r*nn[i+1].h;
            if(j==0)
            xx+=pi * nn[i+1].r * nn[i+1].r;
            dp[i+1][j+1]=max(dp[i][j]+xx,dp[i+1][j+1]);
            dp[i+1][j]=max(dp[i+1][j],dp[i][j]);
        }
        printf("Case #%d: %.8f\n", ++cas, dp[n][k]);
    }

}
