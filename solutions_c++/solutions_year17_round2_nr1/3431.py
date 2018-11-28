#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,n,cases=1;
   double mx;
    scanf("%d",&t);

    while(t--)
    {
        int n,m;
          mx=-1.0;
        scanf("%d %d",&n,&m);

        for(int i=0;i<m;i++)
        {
            int u,v;
            scanf("%d %d",&u,&v);
            double more = (double)n-(double)u;
            more/=(double)v;
            mx=max(more,mx);
        }
         printf("Case #%d: %.6lf\n",cases++,(double)n/mx);
    }

    return 0;
}
