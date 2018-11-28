#include <bits/stdc++.h>
using namespace std;
const int inf=109;
typedef long long ll;
typedef long double ld;
const ld MAX=999999999999;
int dis[inf][inf];
ld dp[inf][inf];
ld sol[inf][inf];
int speed[inf];
int space[inf];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for (int test=1;test<=t;++test)
    {
        scanf("%d%d",&n,&m);
        for (int i=0; i<n; ++i)
            scanf("%d%d",&space[i],&speed[i]);
        for (int i=0; i<n; ++i)
            for (int j=0; j<n; ++j)
            {
                int a;
                scanf("%d",&a);
                if (i==j)
                    dp[i][j]=0;
                else if (a==-1)
                    dp[i][j]=MAX;
                else
                    dp[i][j]=a;
            }
        for (int k=0;k<n;++k)
            for (int i=0;i<n;++i)
                for (int j=0;j<n;++j)
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]);
        for (int i=0;i<n;++i)
            for (int j=0;j<n;++j)
                sol[i][j]=(dp[i][j]<=space[i]?dp[i][j]/speed[i]:MAX);
        for (int k=0;k<n;++k)
            for (int i=0;i<n;++i)
                for (int j=0;j<n;++j)
                    sol[i][j]=min(sol[i][j],sol[i][k]+sol[k][j]);
        int a,b;
        printf("Case #%d:",test);
        while(m--)
        {
            scanf("%d%d",&a,&b);
            printf(" %.9lf",sol[a-1][b-1]);
        }
        printf("\n");

    }
}
