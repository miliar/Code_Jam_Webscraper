#include <bits/stdc++.h>
using namespace std;
const int maxn=1440;
int dp[maxn+10][maxn+10][2];
bool ca[maxn+10],ja[maxn+10];
void solve()
{
    int n,m;
    scanf("%d%d",&n,&m);
    memset(ca,1,sizeof(ca));
    memset(ja,1,sizeof(ja));
    for(int i=0;i<n;i++)
    {
        int s,t;
        scanf("%d%d",&s,&t);
        for(int j=s+1;j<=t;j++)
            ca[j]=0;
    }
    for(int i=0;i<m;i++)
    {
        int s,t;
        scanf("%d%d",&s,&t);
        for(int j=s+1;j<=t;j++)
            ja[j]=0;
    }
    memset(dp,0x3f,sizeof(dp));
    if(ca[1])    dp[1][1][0]=1;
    for(int i=2;i<=maxn;i++)
    {
        for(int j=0;j<=i;j++)
        {
            if(j&&ca[i])
            {
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
            }
            if(ja[i])
            {
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
            }
        }
    }
    int ans=1e9;
    ans=min(ans,dp[maxn][maxn/2][0]-1);
    ans=min(ans,dp[maxn][maxn/2][1]);
    memset(dp,0x3f,sizeof(dp));
    if(ja[1])    dp[1][0][1]=1;
    for(int i=2;i<=maxn;i++)
    {
        for(int j=0;j<=i;j++)
        {
            if(j&&ca[i])
            {
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
            }
            if(ja[i])
            {
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
            }
        }
    }
    ans=min(ans,dp[maxn][maxn/2][0]);
    ans=min(ans,dp[maxn][maxn/2][1]-1);
    printf("%d\n",ans);
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",cas++);
        solve();
    }
    return 0;
}
