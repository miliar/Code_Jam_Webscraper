#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int INF=0x3f3f3f3f;
int busy[2][1505];
int dp[2][1505][2];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        memset(busy,0,sizeof(busy));
        int n[2];
        for(int i=0;i<2;i++)
            scanf("%d",&n[i]);
        for(int i=0;i<2;i++)
            for(int j=0;j<n[i];j++)
            {
                int l,r;
                scanf("%d%d",&l,&r);
                for(int k=l;k<r;k++)
                    busy[i][k]=1;
            }
        int res=INF;
        for(int st=0;st<2;st++)
        {
            if(busy[st][0])continue;
            memset(dp,INF,sizeof(dp));
            int now=0,la=1;
            dp[now][st][st]=0;
            for(int i=0;i+1<1440;i++)
            {
                swap(now,la);
                memset(dp[now],INF,sizeof(dp[now]));
                for(int t=0;t<=720;t++)
                    for(int j=0;j<2;j++)
                        for(int k=0;k<2;k++)
                        {
                            if(busy[k][i+1])continue;
                            dp[now][t+k][k]=min(dp[now][t+k][k],dp[la][t][j]+(j^k));
                        }
            }
            for(int k=0;k<2;k++)
                res=min(res,dp[now][720][k]+(st^k));
        }
        printf("Case #%d: %d\n",ca,res);
    }
    return 0;
}
