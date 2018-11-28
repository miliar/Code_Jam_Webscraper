#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;

ll n,k;

pii get(ll n){
    ll a=(n-1)/2;
    ll b=n-a-1;
    return pii(b,a);
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%lld%lld",&n,&k);
        map<ll,ll> cnt;
        set<ll,greater<ll>> mys;
        mys.insert(n); cnt[n]++;
        printf("Case #%d: ",tt);
        while(k>0){
            ll x=*mys.begin(); mys.erase(mys.begin());
            pii val=get(x);
            ll total=cnt[x];
            if(total>=k){
                printf("%lld %lld\n",val.first,val.second);
                break;
            }else{
                cnt[val.first]+=total;
                cnt[val.second]+=total;
                cnt.erase(x);
                mys.insert(val.first);
                mys.insert(val.second);
                k-=total;
            }
        }
    }
}
