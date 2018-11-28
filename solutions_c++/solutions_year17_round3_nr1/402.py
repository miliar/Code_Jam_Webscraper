#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const double pi=acos(-1.0);
int t,n,k;
struct pan {
    double r,h;
} cake[1005];
bool cmp1(pan p1,pan p2) {
    return p1.r>p2.r;
}
bool cmp2(pan p1,pan p2) {
    return p1.r*p1.h>p2.r*p2.h;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%d%d",&n,&k);
        for (int i=0;i<n;++i)
            scanf("%lf%lf",&cake[i].r,&cake[i].h);
        double res=0;
        for (int i=0;i<=n-k;++i) {
            sort(cake+i,cake+n,cmp1);
            double temp=cake[i].r*cake[i].r*pi+2.0*pi*cake[i].r*cake[i].h;
            sort(cake+1+i,cake+n,cmp2);
            for (int j=i+1;j<k+i;++j)
                temp+=2.0*pi*cake[j].r*cake[j].h;
            res=max(res,temp);
        }
        printf("Case #%d: %.12f\n",cas,res);
    }
    return 0;
}
