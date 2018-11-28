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

const double PI=acos(-1);

double dp[1111][1111];
void solve(){
    int N,K;cin>>N>>K;
    vpint vec(N);
    rep(i,N)cin>>vec[i].fi>>vec[i].se;
    sort(all(vec));
    fill_n(*dp,1111*1111,-(1e18));
    dp[0][0]=0;
    double ans=0;
    for(int i=0;i<N;i++){
        chmax(ans,dp[i][K-1]+vec[i].fi*2*PI*vec[i].se+vec[i].fi*vec[i].fi*PI);
        for(int j=0;j<=K;j++){
            chmax(dp[i+1][j],dp[i][j]);
            chmax(dp[i+1][j+1],dp[i][j]+vec[i].fi*2*PI*vec[i].se);
        }
    }
    printf("%.20f\n",ans);
    return;
}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%lld: ",i);
        solve();
    }
    return 0;
}
