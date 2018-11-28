#include<bits/stdc++.h>
using namespace std;


int main(){

    long long t,i,j,n;
    double d,a,b,h,m,sp,dis;

    scanf("%lld",&t);
    for(i=0;i<t;i++){
        m = 0.0;
        scanf("%lf",&d);
        //printf("%lf\n",d);
        scanf("%lld",&n);
        for( j=0;j<n;j++ ){
            scanf("%lf %lf",&a,&b);

            dis = d-a;
            h = dis/b;
            //printf("%lf\n",h);
            if( h>m ){
                m = h;
            }
        }
        sp = d/m;
        sp += 0.000000001;
        printf("Case #%lld: %.6lf\n",i+1,sp);

    }


    return 0;
}
