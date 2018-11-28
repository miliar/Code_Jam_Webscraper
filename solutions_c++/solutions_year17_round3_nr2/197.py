#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int type[1500],dp[1500][750][2];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,n,m,a,b;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&m);
        fill(type,type+1444,-1);
        memset(dp,0x3f,sizeof(dp));
        for (int i=1;i<=n;++i)
        {
            scanf("%d%d",&a,&b);
            for (int j=a;j<b;++j) type[j]=0;
        }
        for (int i=1;i<=m;++i)
        {
            scanf("%d%d",&a,&b);
            for (int j=a;j<b;++j) type[j]=1;
        }
        dp[0][0][0]=dp[0][0][1]=1;
        for (int i=1;i<=1440;++i)
            for (int j=0;j<=720&&j<=i;++j)
            {
                if (type[i-1]!=0&&j>0)
                    dp[i][j][0]=min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1);
                if (type[i-1]!=1)
                    dp[i][j][1]=min(dp[i-1][j][0]+1,dp[i-1][j][1]);
            }
        for (int i=0;i<2;++i)
            if (dp[1440][720][i]%2!=0)
                --dp[1440][720][i];
        printf("Case #%d: %d\n",cas,min(dp[1440][720][0],dp[1440][720][1]));
    }
    return 0;
}
