#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
int g[105],dp[105][105][105][5];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,p;
        scanf("%d%d",&n,&p);
        for(int i=1;i<=n;i++)
            scanf("%d",&g[i]);
        printf("Case #%d: ",ca);
        int cnt[4]={0,0,0,0};
        for(int i=1;i<=n;i++)
            cnt[g[i]%p]++;
        memset(dp,0xcf,sizeof(dp));
        dp[cnt[1]][cnt[2]][cnt[3]][0]=0;
        for(int i=cnt[1];i>=0;i--)
            for(int j=cnt[2];j>=0;j--)
                for(int k=cnt[3];k>=0;k--)
                    for(int t=0;t<p;t++)
                    {
                        if(i)dp[i-1][j][k][(t+1)%p]=max(dp[i-1][j][k][(t+1)%p],dp[i][j][k][t]+(t==0));
                        if(j)dp[i][j-1][k][(t+2)%p]=max(dp[i][j-1][k][(t+2)%p],dp[i][j][k][t]+(t==0));
                        if(k)dp[i][j][k-1][(t+3)%p]=max(dp[i][j][k-1][(t+3)%p],dp[i][j][k][t]+(t==0));
                    }
        int res=0;
        for(int i=0;i<p;i++)
            res=max(res,dp[0][0][0][i]);
        printf("%d\n",res+cnt[0]);
    }
    return 0;
}
