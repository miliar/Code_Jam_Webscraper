#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    freopen("/Users/zty/Downloads/C-large.in","r",stdin);
    freopen("/Users/zty/Downloads/C-large.txt","w",stdout);
    long long N, K, t, ans, x, tmp, num, Max, Min;
    scanf("%lld",&t);
    for(int cas=1;cas<=t;cas++) {
        ans=1;
        scanf("%lld%lld",&N,&K);
        while (K>ans*2-1) {
            ans*=2;
        }
        N-=ans-1;
        x=N/ans;
        num=N-x*ans;
        tmp=ans-num;
        if(x&1) {
            Min=x/2;
            if(K-ans+1<=num)Max=Min+1;
            else Max=Min;
        } else {
            Max=x/2;
            if(K-ans+1>num)Min=Max-1;
            else Min=Max;
        }
        printf("Case #%d: %lld %lld\n",cas,Max,Min);
    }
    return 0;
}