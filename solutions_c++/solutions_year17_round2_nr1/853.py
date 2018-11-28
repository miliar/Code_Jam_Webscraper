#include <stdio.h>
main()
{
    freopen("A-large.in","r",stdin);
    freopen("Al.txt","w",stdout);
    int t; scanf("%d",&t);
    int d,n,k,s;
    double ans,tp;
    for(int tt = 1;tt <= t;tt++)
    {
        scanf("%d %d %d %d",&d,&n,&k,&s);
        ans = ((double)(d-k))/s;
        while(--n)
        {
            scanf("%d %d",&k,&s);
            tp = ((double)(d-k))/s;
            if(tp > ans) ans = tp;
        }
        ans = 1/ans;
        printf("Case #%d: %.6f\n",tt,d*ans);
    }
}
