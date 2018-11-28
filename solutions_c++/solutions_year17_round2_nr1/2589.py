#include<stdio.h>
#include <iostream>
#include<string.h>
struct horse
{
    int k,s;
    double time;
}h[1010];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t,icase=0;
    scanf("%d",&t);
    while(t--)
    {
        memset(h,0,sizeof(h));
        int d,n;
        scanf("%d%d",&d,&n);
        double maxt=0;
        int k,s;
        double ti;
        for(int i = 0; i < n ; i++)
        {
            scanf("%d%d",&k,&s);
            ti=((d-k)*1.0)/s;
            if(ti>maxt)
                maxt=ti;
        }
        printf("Case #%d: %.6lf\n",++icase,d*1.0/maxt);
    }
    return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
