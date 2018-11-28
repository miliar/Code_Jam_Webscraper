#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn=1010;
const double PI=acos(-1);
int t,n,k;
struct pan{
    int r,h;
    double rs,hs;
}p[maxn];

bool cmp(pan x,pan y)
{
    if(x.rs==y.rs) return x.hs>y.hs;
    return x.rs>y.rs;
}
double dp[maxn][maxn];
int dp2[maxn][maxn];
int main()
{
  //  freopen("in.in","r",stdin);
   // freopen("out.out","w",stdout);
    cin>>t;
    int cas=0;
    while(t--)
    {
        cin>>n>>k;
        for(int i=0;i<n;i++)
        {
            int r,h;
            cin>>r>>h;
            p[i].r=r;
            p[i].h=h;
            p[i].rs=PI*r*r;
            p[i].hs=2*PI*r*h;
        }
        sort(p,p+n,cmp);
        for(int i=0;i<n;i++)
            for(int j=0;j<=k;j++)
               dp[i][j]=0;
        for(int i=0;i<n;i++)
        {
            dp[i][1]=max(dp[i-1][1],p[i].hs+p[i].rs);
            for(int j=2;j<=k;j++)
            {
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+p[i].hs);
                dp[i][j]=max(dp[i][j],dp[i-1][j]);
            }
        }
        printf("Case #%d: %.9lf\n",++cas,dp[n-1][k]);
    }
    return 0;
}
