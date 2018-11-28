#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;

//double pi = 3.14159265358;
int n,m,T;
double a[1011];
double b[1011];
double c[1011];
int main() {
   freopen("A-large (3).in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    int i,j,k;
    double p,q,r,t;
    double R,H;
    double ans1,ans2,ans;
scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%d %d",&n,&m);
    ans1 = -1.0;
    for(i=0;i<n;i++) {
        scanf("%lf %lf",&R,&H);
        p = M_PI * R * R;
        b[i] = p;
        //if(p > ans1) ans1 = p;
        a[i] = 2 * M_PI * R * H;
    }
    ans = -1.0;
    for(i=0;i<n;i++) {
        k = 0;
        t = b[i] + a[i];
        for(j=0;j<n;j++) {
            if(i != j) {
                c[k] = a[j];
                k++;
            }
        }
        sort(c,c+n-1);
        for(j=0;j<m - 1;j++) {
            k = n - 2 - j;
            t += c[k];
        }
        if(t > ans) ans = t;
    }
   // printf(">>>%lf %lf\n",ans1,ans2);
    printf("Case #%d: %.7lf\n",ii+1,ans);
}


    return 0;
}
/*
surface + border
border = 2 pi r for each
surface = S1 + (s2 - s1) + (s3 - s2) + (s4 - s3) = S4
*/
