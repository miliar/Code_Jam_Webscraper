#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
using namespace std;
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double pi=acos(-1.0);
const int mod=1e9+7;

int vis[1500];
int dp[1500][1500][3][3];

int main()
{
    freopen("databl.in","r",stdin);
    freopen("databl.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        memset(vis,0,sizeof(vis));
        for(int i=1;i<=n;i++)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            for(int j=c+1;j<=d;j++)
                vis[j]=1;
        }
        for(int i=1;i<=m;i++)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            for(int j=c+1;j<=d;j++)
                vis[j]=2;
        }
        memset(dp,inf,sizeof(dp));
        //dp[0][0][1][1]=dp[0][0][2]=0;
        if(vis[1]!=1)
            dp[1][1][1][1]=0;
        if(vis[1]!=2)
            dp[1][0][2][2]=0;
        for(int i=2;i<=1440;i++)
        {
            for(int j=0;j<=720;j++)
            {
                if(vis[i]!=1)
                {
                    if(j>0)
                    {
                        for(int k=1;k<=2;k++)
                             dp[i][j][1][k]=min(dp[i][j][1][k],dp[i-1][j-1][1][k]);
                    }
                    for(int k=1;k<=2;k++)
                    dp[i][j][1][k]=min(dp[i][j][1][k],dp[i-1][j-1][2][k]+1);
                }
                //i  minutes B
                if(vis[i]!=2)
                {
                    for(int k=1;k<=2;k++)
                    {
                        dp[i][j][2][k]=min(dp[i][j][2][k],dp[i-1][j][2][k]);
                        dp[i][j][2][k]=min(dp[i][j][2][k],dp[i-1][j][1][k]+1);
                    }
                }
            }
        }
        int ans=inf;
        for(int i=1;i<=2;i++)
        {
            for(int j=1;j<=2;j++)
            {
                if(i!=j)
                    dp[1440][720][i][j]++;
                ans=min(ans,dp[1440][720][i][j]);
            }
        }

        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0 ;
}

