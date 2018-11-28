#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

void solve(){
    int N,D;scanf("%lld%lld",&D,&N);
    vint K(N),S(N);
    rep(i,N)scanf("%lld%lld",&K[i],&S[i]);

    double mi=1e15;
    rep(i,N){
        double t=(D-K[i])*1.0/S[i];
        chmin(mi,D/t);
    }
    printf("%.20f\n",mi);
}

signed main(){
    int T;scanf("%lld",&T);
    rep(i,T){
        printf("Case #%lld: ",i+1);
        solve();
    }
    return 0;
}
