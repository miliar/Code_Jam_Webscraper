#include <bits/stdc++.h>

using namespace std;


typedef long long ll;

map<ll,ll>m;

int main(){

    freopen("out.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        ll n,k,a,b;
        scanf("%lld%lld",&n,&k);
        m.clear();
        m[n]=1;
        while(k>0){
            map<ll,ll>::reverse_iterator rit=m.rbegin();
            ll v=(rit->first)-1,cnt=rit->second;
            a=(v>>1),b=v-a;
            m.erase(v+1);
            m[a]+=cnt;
            m[b]+=cnt;
            k-=cnt;
        }
        printf("Case #%d: ",cas);
        printf("%lld %lld\n",b,a);
    }

    return 0;
}
