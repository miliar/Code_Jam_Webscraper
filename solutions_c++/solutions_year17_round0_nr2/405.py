#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

int inc(ll n){
    ll prev = 10;
    while(n){
        if(n%10 > prev)return 0;
        prev = n%10;
        n/=10;
    }
    return 1;
}
ll f(ll n){
    if(n==0)return n;
    ll x = f(n/10);
    ll ans;
    if(x!=n/10)ans = x*10+9;
    else if(n%10 < n/10%10)ans =(n/10-1)*10+9;
    else ans = n;
    
    if(!inc(ans))return f(ans);
    return ans;
}
int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ",tc);
        ll n;
        scanf("%lld",&n);
        

        printf("%lld\n",f(n));
    }
}
