#include <bits/stdc++.h>
#define maxn 2450
#define inf 0x3f3f3f3f
#define REP(i,x,y) for(int i=x;i<(y);i++)
using namespace std;
int dp[maxn][maxn][2];
int vis[2][maxn],n,m;
int main()
{
    freopen("data2.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;scanf("%d",&T);int cas=1;
    while(T--){
        memset(vis,0,sizeof(vis));
        scanf("%d %d",&n,&m);
        REP(i,1,n+1){
            int bg,ed;scanf("%d %d",&bg,&ed);
            REP(j,bg+1,ed+1) vis[0][j]=1;
        }
        REP(i,1,m+1){
            int bg,ed;scanf("%d %d",&bg,&ed);
            REP(j,bg+1,ed+1) vis[1][j]=1;
        }
        memset(dp,inf,sizeof(dp));
        dp[0][0][0]=0;
        REP(i,1,1441){
            REP(j,1,i+1){
                if(!vis[0][i]) dp[i][j][0]=min(dp[i][j][0],min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1));
                if(!vis[1][i]) dp[i][j][1]=min(dp[i][j][1],min(dp[i-1][j][1],dp[i-1][j][0]+1));
            }
        }
        int ans=min(dp[1440][720][0],dp[1440][720][1]+1);
        memset(dp,inf,sizeof(dp));
        dp[0][0][0]=0;
        REP(i,1,1441){
            REP(j,1,i+1){
                if(!vis[1][i]) dp[i][j][0]=min(dp[i][j][0],min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1));
                if(!vis[0][i]) dp[i][j][1]=min(dp[i][j][1],min(dp[i-1][j][1],dp[i-1][j][0]+1));
            }
        }
        ans=min(ans,min(dp[1440][720][0],dp[1440][720][1]+1));
        printf("Case #%d: %d\n",cas++,ans);
    }
}
