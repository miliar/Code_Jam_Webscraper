#include<bits/stdc++.h>

using namespace std;
const double eps=1e-9;
double p[60];
int v[60];
int n,k;
double u,ans;
bool check(double m)
{
    ans=1;
    double s=u;
    for (int i=1; i<=n; i++)
    {
        if (p[i]>=m) ans*=p[i];
        else {
            ans*=m;
            s-=(m-p[i]);
            if (s<-eps) return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("C-small-1-attempt1.in","r",stdin);
    freopen("c.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        double s=u,l=0;
        for (int i=1; i<=n; i++)
        {
            scanf("%lf",&p[i]);
            l=min(l,p[i]);
            s+=p[i];
        }
        memset(v,0,sizeof(v));
        if (n==k)
        {
            double r=1;
            while (r-l>eps)
            {
                double m=(l+r)/2;
                if (check(m)) l=m;
                else r=m;
            }
            check(l);
            printf("Case #%d: %.8lf\n",tt,ans);
        }
    }
}
