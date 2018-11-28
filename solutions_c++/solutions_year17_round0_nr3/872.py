#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int T,cas = 1;
    ll n,k;
    cin>>T;
    while(T--){
        scanf("%I64d%I64d",&n,&k);
        ll tmp = k,ans;
        int l = 0;
        while(tmp){
            tmp>>=1;
            l++;
        }
        n -= (1ll<<(l-1)) - 1;
        ll x = n/(1ll<<(l-1));
        ll m = n-x*(1ll<<(l-1));
        //printf("k=%I64d\n",k);
        k -= (1ll<<(l-1)) - 1;
        //printf("l=%d k=%I64d m=%I64d\n",l,k,m);
        if(k > m) ans = x;
        else ans = x+1;
        //printf("ans=%d\n",ans);
        ans--;
        printf("Case #%d: %I64d %I64d\n",cas++,ans/2+(ans&1),ans/2);
    }
    return 0;
}
