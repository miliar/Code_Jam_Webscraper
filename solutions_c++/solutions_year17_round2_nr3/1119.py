#include <bits/stdc++.h>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;
typedef pair<int,int> PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int K=1e6+7;
const int mod=1e9+7;


int n,q;
double mxv[K],d[K],mxd[K],sum[K],dp[K];
int main(void)
{
    freopen("ans.txt","w",stdout);
    int t,cnt=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>q;
        sum[n]=0;
        for(int i=1; i<=n; i++)
            scanf("%lf%lf",mxd+i,mxv+i);
        for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++)
        {
            double x;
            scanf("%lf",&x);
            if(x>0) d[i]=x;
        }
        int x,y;
        scanf("%d%d",&x,&y);
        for(int i=n-1;i;i--)
            sum[i]=sum[i+1]+d[i];
        for(int i=1;i<n;i++)
            dp[i]=1e18;
        dp[n]=0;
        for(int i=n;i!=1;i--)
        for(int j=i-1;j;j--)
        if(sum[j]-sum[i]<mxd[j]+eps)
            dp[j]=min(dp[j],dp[i]+(sum[j]-sum[i])/mxv[j]);
        printf("Case #%d: %.8f\n",cnt++,dp[1]);
    }
    return 0;
}
