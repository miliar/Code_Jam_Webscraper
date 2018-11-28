#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
const double PI=acos(-1);
struct node
{
    double r,h;
}a[1005];
int cmp(node a,node b)
{
    return a.r>b.r;
}

void fre(){
    freopen("A-large.in" ,"r",stdin );
    freopen("asdf.out","w",stdout);
}

double dp[1005][1005];
int main()
{
    fre();
    int kase=0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,kk;
        scanf("%d%d",&n,&kk);
        for(int i=0;i<n;i++)
        {
            scanf("%lf%lf",&a[i].r,&a[i].h);
        }
        sort(a,a+n,cmp);
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++)
        {
            dp[i][1]=PI*a[i].r*a[i].r+2*PI*a[i].r*a[i].h;
        }
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                for(int k=2;k<=kk;k++)
                {
                    if(dp[j][k-1]>0)
                    {
                        dp[i][k]=max(dp[i][k],2*PI*a[i].r*a[i].h+dp[j][k-1]);
                    }
                }
            }
        }
        double output=0;
        for(int i=0;i<n;i++)output=max(output,dp[i][kk]);
        printf("Case #%d: ",++kase);
        printf("%.9lf\n",output);
    }
}
