#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int n,t,d;
int main()
{
    scanf("%d",&t);
    for(int tt=1;tt<=t;++tt)
    {
        scanf("%d%d",&d,&n);
        double ans=1e100,time=0;
        while(n--)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            time=max(time,1.0*(d-a)/b);
        }
        ans=d/time;
        printf("Case #%d: %.10f\n",tt,ans);
    }
    return 0;
}
