#include<bits/stdc++.h>
using namespace std;
const int maxn=1e3+200;
const double pi=acos(-1.0);
void init()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
}
struct node
{
    double x,y;
}p[maxn];
bool cmp(node a,node b)
{
    return a.x<b.x;
}
double dp[maxn][maxn];
int main()
{
    init();
    int T,ca=1;scanf("%d",&T);
    while(T--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
            scanf("%lf%lf",&p[i].x,&p[i].y);
        sort(p+1,p+n+1,cmp);
        memset(dp,0,sizeof(dp));
            for(int j=1;j<=k;j++)
                for(int i=1;i<=n;i++)
                    for(int z=j-1;z<i;z++)
                        dp[i][j]=max(max(dp[i-1][j],dp[i][j]),dp[z][j-1]+pi*(p[i].x*p[i].x-p[z].x*p[z].x)+2*pi*p[i].x*p[i].y);
        printf("Case #%d: %.6lf\n",ca++,dp[n][k]);
    }

    return 0;
}
