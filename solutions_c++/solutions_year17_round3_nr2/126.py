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

const int INF=1001001001;

int luz[1440];
int dp[2][1000][2];
void solve(){
    memset(luz,-1,sizeof(luz));
    int N,M;
    cin>>N>>M;
    rep(i,N){
        int a,b;
        cin>>a>>b;
        for(int j=a;j<b;j++)luz[j]=0;
    }
    rep(i,M){
        int a,b;
        cin>>a>>b;
        for(int j=a;j<b;j++)luz[j]=1;
    }

    int ans=INF;

    rep(s,2){
        fill_n(**dp,2*1000*2,INF);
        dp[0][0][s]=0;
        for(int i=0;i<1440;i++){
            for(int j=0;j<=720;j++){
                for(int k=0;k<2;k++){
                    for(int l=0;l<2;l++){
                        if(luz[i]!=-1&&luz[i]!=l)continue;
                        chmin(dp[(i+1)&1][j+l][l],dp[i&1][j][k]+(k!=l));
                    }
                    dp[i&1][j][k]=INF;
                }
            }
        }
        chmin(ans,dp[0][720][s]);
    }
    cout<<ans<<endl;

}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%lld: ",i);
        solve();
    }
    return 0;
}
