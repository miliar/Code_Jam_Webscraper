#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int T;
ll n,k;
map<ll,ll> mapp[100];
int main(){
//    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",ca);
        mapp[0].clear();
        mapp[0][n]=1;
        ll ma,mi;
        for(int i=0;;++i){
            mapp[i+1].clear();
            for(auto e=mapp[i].end();e!=mapp[i].begin();){
                --e;
                ll nn=e->first-1,q=nn/2,w=nn-q;
                k-=e->second;
                if(k<=0){
                    ma=w;
                    mi=q;
                    break;
                }
                if(q)mapp[i+1][q]+=e->second;
                if(w)mapp[i+1][w]+=e->second;
            }
            if(k<=0)break;
        }
        printf("%lld %lld\n",ma,mi);
    }
    return 0;
}
