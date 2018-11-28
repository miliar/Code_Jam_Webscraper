#include<stdio.h>
#include<algorithm>
using namespace std;

double D;
int n,T;
double K[1011],S[1011];
double OFF;
double f() {

    int i,j,k;
    double maxx = -1.0;
    double p,q,r;
    for(i=n-1;i>=0;i--) {
        p = D - K[i];
        p /= S[i];
        if(p > maxx) maxx = p;
    }
    p = D / maxx;
    return p;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    int i,j,k;
    double p,q,r;

    scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%lf %d",&D,&n);
    for(i=0;i<n;i++) {
        scanf("%lf %lf",&K[i],&S[i]);
    }
    for(i=0;i<n;i++) {
        for(j=0;j<n-1;j++) {
            if(K[j] > K[j+1]) {
                swap(K[j],K[j+1]);
                swap(S[j],S[j+1]);
            }
        }
    }
    /*
    double left,right,mid;
    left = 0.0;
    right = 1.0;
    r = 1.0;
    OFF = 1.0;
    for(i=0;i<10;i++)right*=r;
    for(i=0;i<7;i++)OFF /= r;
    while(left < right) {
        mid = (left + right) / (double(2.0));
        if(right - mid <= OFF) break;
        if(f(mid)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    */
    printf("Case #%d: %lf\n",ii+1,f());
}

    return 0;
}
