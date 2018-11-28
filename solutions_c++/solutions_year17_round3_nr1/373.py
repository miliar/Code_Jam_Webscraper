#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
using namespace std;
const double pi=acos(-1.0);
const int mod=1e9+7;

PII a[1005];
long long  dp[1005][1005];

int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        int n,K;
        cin>>n>>K;
        for(int i=1;i<=n;i++)
            scanf("%d%d",&a[i].AA,&a[i].BB);
        sort(a+1,a+1+n);
        memset(dp,0,sizeof(dp));
        long long ans=0;
        for(int i=n;i>0;i--)
        {
            long long now=2long long*a[i].AA*a[i].BB;
            for(int j=1;j<=K;j++)
            {
                for(int k=n+1;k>i;k--)
                {
                    long long temp=dp[k][j-1]+now;
                    if(j==1)  temp += 1long long*a[i].AA*a[i].AA;
                    dp[i][j]=max(dp[i][j],temp);
                }
            }
            ans=max(ans,dp[i][K]);
        }
        printf("Case #%d: %.10f\n",cas++,ans*pi);
    }
    return 0 ;
}

