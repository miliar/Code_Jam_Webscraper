#include<bits/stdc++.h>
using namespace std;
double bg[1005];
double v[1005];
double D;
int n;
bool check(double val)
{
    for(int i=0; i<n; i++)
    {
        if(D*v[i]<val*(D-bg[i]))
            return false;
    }
    return true;
}
int main()
{
//    freopen("A-small-attempt2.in","r",stdin);
//    freopen("A-small-attempt2.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%lf%d",&D,&n);
        for(int i=0; i<n; i++)
        {
            scanf("%lf%lf",&bg[i],&v[i]);
        }
        double l=0.0,r=1e16;
        for(int i=0; i<100; i++)
        {
            double mid=(l+r)/2.0;
            if(check(mid))
                l=mid;
            else
                r=mid;
        }
        printf("Case #%d: %.10f\n",cas,l);
    }
    return 0;
}
