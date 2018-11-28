#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t,d,n,x,y;
    double ans;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&d,&n);
        ans=0;
        for (int i=1;i<=n;++i)
        {
            scanf("%d%d",&x,&y);
            ans=max(ans,(d-x)*1./y);
        }
        printf("Case #%d: %.9f\n",cas,d/ans);
    }
    return 0;
}
