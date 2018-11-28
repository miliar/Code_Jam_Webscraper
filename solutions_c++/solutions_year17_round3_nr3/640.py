#include<stdio.h>
#include<algorithm>
using namespace std;
int n,m,T;
double u;
double a[55];
int main() {
   freopen("C-small-1-attempt0 (1).in","r",stdin);
    freopen("C-small-1-out.txt","w",stdout);
    int i,j,k;
    double p,q,r;
    double t,tt,ttt;
scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%d %d",&n,&m);
    scanf("%lf",&u);
    for(i=0;i<n;i++) scanf("%lf",&a[i]);
    a[n] = 1.0;
    n++;m++;
    sort(a,a+n);
    ttt = -1.0;
    for(i=n-1;i>0;i--) {
        p = 0;
        for(j=0;j<i;j++) p += a[j];
        q = (double)i;
        t = (p + u) / q;
        if(a[i-1] <= t && t <= a[i]) {
            ttt = 1.0;
            for(k=0;k<=i-1;k++) {
                ttt *= t;
            }
            for(;k<n;k++) {
                ttt *= a[k];
            }
            break;
        }
    }
    printf("Case #%d: %lf\n",ii+1,ttt);
}


    return 0;
}
