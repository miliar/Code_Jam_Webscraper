#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

PII a[1005];
double  dp[1005][1005];

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int n,K;
        cin>>n>>K;
        for(int i=1;i<=n;i++)
            scanf("%d%d",&a[i].AA,&a[i].BB);
        sort(a+1,a+1+n);
        memset(dp,0,sizeof(dp));
        double ans=0;
        for(int i=n;i>0;i--)
        {
            double now=2*pi*a[i].AA*a[i].BB;
            for(int j=1;j<=K;j++)
            {
                for(int k=n+1;k>i;k--)
                {
                    double temp=dp[k][j-1]+now;
                    if(j==1)  temp+=pi*a[i].AA*a[i].AA;
                    dp[i][j]=max(dp[i][j],temp);
                }
            }
            ans=max(ans,dp[i][K]);
        }
        printf("Case #%d: %.10f\n",cas++,ans);
    }
    return 0 ;
}

