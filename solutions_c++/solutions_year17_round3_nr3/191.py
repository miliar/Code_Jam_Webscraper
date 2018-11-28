#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t,n,k;
    double u,p[55];
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d%lf",&n,&k,&u);
        for (int i=1;i<=n;++i) scanf("%lf",p+i);
        sort(p+1,p+n+1);
        p[n+1]=1;
        while (u>0)
        {
            int idx;
            for (idx=2;idx<=n&&p[idx]==p[idx-1];++idx);
            if (idx>n&&p[idx-1]==1) break;
            if (u>(p[idx]-p[idx-1])*(idx-1))
            {
                u-=(p[idx]-p[idx-1])*(idx-1);
                for (int i=1;i<idx;++i) p[i]=p[idx];
            }
            else
            {
                for (int i=1;i<idx;++i) p[i]+=u/(idx-1);
                u=0;
                break;
            }
        }
        double ans=1;
        for (int i=1;i<=n;++i) ans*=p[i];
        printf("Case #%d: %.9f\n",cas,ans);
    }
    return 0;
}
