#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
map<ll,ll,greater<ll>> U;
int main(){
    freopen("C-large.in","rt",stdin);
    freopen("C-large-out.out","wt",stdout);
    int T;
    ll K, N;
    cin>>T;
    for(int f=1;f<=T;f++){
        cin>>N>>K;
        U.clear();
        pll h;
        U[N]=1;
        while(1){
            h=*U.begin();
            if(h.second>=K){
                goto prt;
            }
            K-=h.second;
            U[(h.first-1)/2] += h.second;
            U[(h.first-1)-(h.first-1)/2] +=h.second;
            U.erase(U.begin());
        }
        prt:
        printf("Case #%d: %lld %lld\n",f,h.first-1-(h.first-1)/2,(h.first-1)/2);
    }
}
