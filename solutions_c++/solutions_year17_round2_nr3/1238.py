#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int T,n,q,a[103],b[103],len;
LL d[103];
double dp[103];
double solve(int s,int t)
{
    dp[s]=0;
    for(int i=s+1;i<=t;++i)
    {
        dp[i]=1e100;
        for(int k=s;k<i;++k)
            if(a[k]>=d[i-1]-d[k-1])
                dp[i]=min(dp[i],dp[k]+1.0*(d[i-1]-d[k-1])/b[k]);
    }
    return dp[t];
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d%d",&n,&q);
        for(int i=1;i<=n;++i)
            scanf("%d%d",a+i,b+i);
        for(int i=1;i<=n;++i)
            for(int j=1;j<=n;++j)
            {
                if(i+1==j)
                    cin>>d[i];
                else scanf("%*d");
            }
        for(int i=2;i<n;++i)
            d[i]+=d[i-1];
        printf("Case #%d:",t);
        while(q--)
        {
            int s,t;
            scanf("%d%d",&s,&t);
            printf(" %.10f",solve(s,t));
        }
        putchar('\n');
    }
    return 0;
}
