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

int N,P;
int A[111];

int dp[111][111][111][4];
void solve(){
    cin>>N>>P;
    rep(i,N)cin>>A[i];
    int cnt[4]={};
    rep(i,N)cnt[A[i]%P]++;

    fill_n(***dp,111*111*111*4,INT_MIN);
    dp[cnt[1]][cnt[2]][cnt[3]][0]=0;

    for(int i=100;i>=0;i--){
        for(int j=100;j>=0;j--){
            for(int k=100;k>=0;k--){
                for(int l=0;l<P;l++){
                    if(i)chmax(dp[i-1][j][k][(l+1)%P],dp[i][j][k][l]+(l==0));
                    if(j)chmax(dp[i][j-1][k][(l+2)%P],dp[i][j][k][l]+(l==0));
                    if(k)chmax(dp[i][j][k-1][(l+3)%P],dp[i][j][k][l]+(l==0));
                }
            }
        }
    }
    int ans=0;
    rep(i,P)chmax(ans,dp[0][0][0][i]);
    cout<<ans+cnt[0]<<endl;
}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
