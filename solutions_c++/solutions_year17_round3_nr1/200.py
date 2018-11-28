#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<double,int> P;
const double pi=acos(-1.0);
int n,k;
double b[1009];
P a[1009];
int main(){
//    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;++i){
            int r,h;
            scanf("%d%d",&r,&h);
            b[i]=pi*r*r+2*pi*r*h;
            a[i]=P(2*pi*r*h,i);
        }
        sort(a,a+n);
        double ans=0;
        for(int i=0;i<n;++i){
            double now=b[i];
            for(int j=n-1,l=1;l<k;--j){
                if(a[j].second==i)continue;
                now+=a[j].first;
                ++l;
            }
            ans=max(ans,now);
        }
//        for(int i=0;i<k;++i)ans+=a[n-i-1];
        printf("Case #%d: ",ca);
        printf("%.8f\n",ans);
    }
    return 0;
}
