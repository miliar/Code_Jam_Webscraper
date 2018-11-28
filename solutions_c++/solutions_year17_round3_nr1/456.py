#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#define LL long long
#define CLR(a,x) memset(a,x,sizeof(a))

#define fread freopen("A-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)
using namespace std;

const int maxm=3e5+10;

const double pai=acos(-1.0);

struct CAKE
{
    int r,h;
    bool operator<(const CAKE &t)const
    {
        return (r==t.r)?h>t.h:r>t.r;
    }
}cake[1010];
void MAX(double &x,double y){if (y>x) x=y;}

double cnt(double r,double h)
{
    return 2.0*pai*r*h;
}
int n,k;
double dp[1010][1010];
int main()
{
//    fread;
//   fwrite;
    int t;
    cin>>t;
    for (int T=1;T<=t;T++)
    {
        cin>>n;
        cin>>k;
        for(int i=1;i<=n;i++)
            cin>>cake[i].r,cin>>cake[i].h;

        sort(cake+1,cake+1+n);



        for (int i=1;i<=k;i++) dp[0][i]=0.0;
        for (int i=1;i<=n;i++)
        {
            dp[i][1]=cnt(cake[i].r,cake[i].h)+pai*cake[i].r*cake[i].r;
            MAX(dp[i][1],dp[i-1][1]);
            for (int j=2;j<=min(i,k);j++)
            {
                dp[i][j]=dp[i-1][j];
                MAX(dp[i][j],dp[i-1][j-1]+cnt(cake[i].r,cake[i].h));
            }
        }
        printf("Case #%d: %.9lf\n",T,dp[n][k]);
    }
    return 0;
}
