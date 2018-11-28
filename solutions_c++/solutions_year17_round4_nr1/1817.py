#include<cstdio>
#include<iostream>
using namespace std;
typedef long long ll;
ll T,n,p,a[101];
int main() {
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("outputA_1.out","w",stdout);
    scanf("%lld",&T);
    for(ll t=1;t<=T;t++) {
        scanf("%lld%lld",&n,&p);
        printf("Case #%lld: ",t);
        for(ll i=0;i<n;i++) scanf("%lld",a+i);
        if(p == 2) {
            ll even = 0;
            for(ll i=0;i<n;i++) even += a[i]%2==0;
            printf("%lld\n", even+(n-even+1)/2);
        }
        if(p == 3) {
            ll b[3] = {0};
            for(ll i=0;i<n;i++) b[a[i]%3]++;
            printf("%lld\n", b[0]+min(b[1],b[2])+(max(b[1],b[2])-min(b[1],b[2])+2)/3);
        }
    }
    return 0;
}
