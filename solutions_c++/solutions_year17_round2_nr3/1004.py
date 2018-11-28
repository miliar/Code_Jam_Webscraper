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

int e[105],s[105];
ll sum[105];
int a[105][105];
double dp[105][105];

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int n,q;
        scanf("%d%d",&n,&q);
        for(int i=1;i<=n;i++)
            scanf("%d%d",&e[i],&s[i]);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                scanf("%d",&a[i][j]);
                if(j==i+1)
                    sum[j]=sum[j-1]+a[i][j];
            }
        }
        int u,v;
        scanf("%d%d",&u,&v);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(i==j) dp[i][j]=0;
                else dp[i][j]=1e18;
            }
        }
        for(int i=n;i>0;i--)
        {
            for(int j=i+1;j<=n;j++)
            {
                for(int k=i+1;k<=j;k++)
                {
                    if(sum[k]-sum[i]<=e[i])
                    {
                        double t=(sum[k]-sum[i])*1.0/s[i];
                        dp[i][j]=min(dp[i][j],dp[k][j]+t);
                    }
                }
            }
        }
//        for(int i=1;i<=n;i++)
//        {
//            for(int j=i;j<=n;j++)
//                printf("%d %d %f\n",i,j,dp[i][j]);
//        }
        printf("Case #%d: %.10f\n",cas++,dp[1][n]);
    }
    return 0 ;
}

