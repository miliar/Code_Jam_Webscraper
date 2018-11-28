#include <bits/stdc++.h>
using namespace std;
int t,i,j,n;
double ans,d,k,s;
int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
    for(scanf("%d",&t);i<t;i++)
    {
        ans=1e308;
        scanf("%lf%d",&d,&n);
        for(j=0;j<n;j++)
        {
            scanf("%lf%lf",&k,&s);
            ans=min(ans,d*s/(d-k));
        }
        printf("Case #%d: %f\n",i+1,ans);
    }
}
