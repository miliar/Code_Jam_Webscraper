#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<double,int> P;
const double pi=acos(-1.0);
int n,k;
double U;
double p[59];
bool che(double x){
    double s=0;
    for(int i=0;i<n;++i)if(p[i]<x)s+=x-p[i];
    return s<=U;
}
int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
//    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d%lf",&n,&k,&U);
        for(int i=0;i<n;++i){
            scanf("%lf",&p[i]);
        }
        double l=0,r=1;
        for(int i=0;i<100;++i){
            double mid=(l+r)/2;
            if(che(mid))l=mid;
            else r=mid;
        }
        double ans=1;
        for(int i=0;i<n;++i){
            if(p[i]>=l)ans*=p[i];
            else ans*=l;
        }
        printf("Case #%d: ",ca);
        printf("%.6f\n",ans);
    }
    return 0;
}
