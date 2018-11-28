#include<bits/stdc++.h>
using namespace std;
int t,tc=0,n;
double dist,slowest;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(++tc<=t){
        slowest=0.0;
        scanf("%lf%d",&dist,&n);
        for(int x=0;x<n;x++){
            double a,b;
            scanf("%lf%lf",&a,&b);
            double time=(dist-a)/b;
            //printf("%f",time);
            slowest=max(slowest,time);
        }
        printf("Case #%d: %f\n",tc,dist/slowest);
    }
}
