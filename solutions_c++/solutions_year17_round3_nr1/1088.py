#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<double,double> PDD;
const double pi = acos(-1.0);
const double e = exp(1.0);
int T,n,k;
double ans;
PDD in[1005];
double dp[1005][1005];
inline double sqr(double x){return x*x;}
void solve()
{
    ans=0;
    for(int i=1;i<=n;++i)
    {
        dp[i][1]=pi*sqr(in[i].first);
        dp[i][1]+=2*pi*in[i].first*in[i].second;
    }
    for(int j=2;j<=k;++j)
    {
        double m=dp[j-1][j-1]-pi*sqr(in[j-1].first);
        for(int i=j;i<=n;++i)
        {
            dp[i][j]=m+pi*(sqr(in[i].first))+2*pi*in[i].first*in[i].second;
            m=max(m,dp[i][j-1]-pi*sqr(in[i].first));
        }
    }/*
        for(int j=2;j<=k&&j<=i;++j)
        {
            for(int t=i-1;t>=j-1;--t)
                dp[i][j]=max(dp[i][j],
                             dp[t][j-1]+pi*(sqr(in[i].first)-sqr(in[t].first))+2*pi*in[i].first*in[i].second);
        }
    }*/
    for(int i=k;i<=n;++i)
        ans=max(ans,dp[i][k]);
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;++i)
            scanf("%lf%lf",&in[i].first,&in[i].second);
        sort(in+1,in+1+n);
        for(int i=1;i<=n;++i)
            for(int j=1;j<=n;++j)
                dp[i][j]=0;
        solve();
        printf("Case #%d: %.10f\n",t,ans);
    }
    return 0;
}
