
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>
#define inf 0x3f3f3f3f
using namespace std;

int dp[1500][800][3];
int l1[1500];
int l2[1500];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int M;
    int tes = 0;
    cin >> M;
    while (M--)
    {
        int t1,t2;
        cin >> t1 >> t2;
        memset(l1,0,sizeof(l1));
        memset(l2,0,sizeof(l2));
        for (int i = 1;i<=t1;i++)
        {
            int a,b;
            cin >>a >> b;
            for (int j = a + 1; j<=b;j++)
                l1[j] = 1;
        }
        for (int i = 1;i<=t2;i++)
        {
            int a,b;
            cin >>a >> b;
            for (int j = a + 1; j<=b;j++)
                l2[j] = 1;
        }
        int ans = 0;
        memset(dp,inf,sizeof(dp));
        dp[0][0][0] = 0;
        for (int i = 1; i<=1440; i++)
        {
            for (int j = 1; j<=i; j++)
            {
                if (l1[i]!=1)dp[i][j][0] =min( min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1),dp[i][j][0]);
                if (l2[i]!=1)dp[i][j][1] =min( min(dp[i-1][j][1],dp[i-1][j][0]+1),dp[i][j][1]);
            }
        }
        ans = min(dp[1440][720][0],dp[1440][720][1]+1);
        memset(dp,inf,sizeof(dp));
        dp[0][0][0] = 0;
        for (int i = 1; i<=1440; i++)
        {
            for (int j = 1; j<=i; j++)
            {
                if (l2[i]!=1)dp[i][j][0] =min( min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1),dp[i][j][0]);
                if (l1[i]!=1)dp[i][j][1] =min( min(dp[i-1][j][1],dp[i-1][j][0]+1),dp[i][j][1]);
            }
        }
        ans = min (min(dp[1440][720][0],dp[1440][720][1]+1),ans);
    printf("Case #%d: %d\n",++tes,ans);
    }
}
