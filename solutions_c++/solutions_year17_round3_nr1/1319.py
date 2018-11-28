#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;
typedef pair<double,int> PII;
const int MAXN=2222;
const int MAXM=233333;
const double PI=acos(-1.0);
int T,n,m;
struct item
{
    double r,h;
}a[MAXN];
bool cmp(item a,item b)
{
    return a.r>b.r;
}
double dp[MAXN][MAXN];
int main()
{
    scanf("%d",&T);
    int ta,tb;
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&n,&m);
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++)
            scanf("%lf%lf",&a[i].r,&a[i].h);
        sort(a,a+n,cmp);
        double ans=0;
        for(int i=0;i<n;i++)
        {
            dp[i][0]=PI*a[i].r*a[i].r+2*PI*a[i].h*a[i].r;
            for(int k=1;k<m;k++)
            {
                for(int j=0;j<i;j++)
                {
                    dp[i][k]=max(dp[i][k],dp[j][k-1]+2*PI*a[i].h*a[i].r);
                }
            }
            ans=max(ans,dp[i][m-1]);
        }
        printf("Case #%d: ",kase);
        printf("%.8f\n",ans);

    }
    return 0;
}
