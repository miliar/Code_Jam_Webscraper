#include<cstdio>
#include<algorithm>
using namespace std;
int main () {
    int T;scanf("%d",&T);
    for(int t=0;t<T;t++) {
        double d,n,mx=0;
        scanf("%lf%lf",&d,&n);
        for(int i=0;i<n;i++) {
            double a,b;
            scanf("%lf%lf",&a,&b);
            double x=(d-a)/b;
            mx=max(mx,x);
        }
        double ans=d/mx;
        printf("Case #%d: %lf\n",t+1,ans);
    }
    return 0;
}