#include <cstdio>
const int maxn=1005;
const long double eps=1e-15;
int t,n;
double kk[maxn],ss[maxn],dd;
long double K[maxn],D,S[maxn];
bool check(long double mid) {
    for (int i=0;i<n;++i)
        if (S[i]>mid-eps)
            continue;
        else if (K[i]*S[i]<=(mid-S[i])*(D-K[i]))
            return false;
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%lf%d",&dd,&n);
        D=dd;
        for (int i=0;i<n;++i) {
            scanf("%lf%lf",&kk[i],&ss[i]);
            K[i]=kk[i];
            S[i]=ss[i];
        }
        long double left=0,right=1e30;
        int cnt=0;
        while (cnt<=600) {
            ++cnt;
            long double mid=(left+right)/2.0;
            if (check(mid))
                left=mid;
            else
                right=mid;
        }
        double res=left;
        printf("Case #%d: %.12f\n",cas,res);
    }
    return 0;
}
