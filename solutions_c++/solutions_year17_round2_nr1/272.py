#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;


void work()
{
    int tc; scanf("%d",&tc);
    int T_T=0;
    while(tc--)
    {
        int n;
        double dis;
        scanf("%lf%d",&dis,&n);
        double ti=0.0;
        for(int i=1;i<=n;i++)
        {
            double k,s;
            scanf("%lf%lf",&k,&s);
            ti=max(ti,(dis-k)/s);
        }
        double ans=dis/ti;
        printf("Case #%d: ",++T_T);
        printf("%.12lf\n",ans);
    }
}

int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
