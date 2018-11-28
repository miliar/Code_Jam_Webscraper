#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define CIN_ONLY if(1)
struct cww{cww(){
    CIN_ONLY{
        ios::sync_with_stdio(false);cin.tie(0);
    }
}}star;
#define fin "\n"
#define FOR(i,bg,ed) for(int i=(bg);i<(ed);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define fi first
#define se second
#define pb push_back
#define DEBUG if(0)
#define REC(ret, ...) std::function<ret (__VA_ARGS__)>
template <typename T>inline bool chmin(T &l,T r)
{bool a=l>r;if(a)l=r;return a;}
template <typename T>inline bool chmax(T &l,T r)
{bool a=l<r;if(a)l=r;return a;}
template <typename T>
istream& operator>>(istream &is,vector<T> &v){
    for(auto &it:v)is>>it;
    return is;
}
typedef vector<int> V;
typedef vector<V> VV;
typedef vector<VV> VVV;
const int INF=1e5;
void solve(){
    int N,P;
    cin>>N>>P;
    VVV dp(N+1,VV(N+1,V(N+1,-INF)));
    dp[0][0][0]=0;
    vector<int> G(N);
    cin>>G;
    for(auto g:G){
        g%=P;
        if(g==0)for(auto &a:dp)for(auto &b:a)for(auto &c:b)c++;
        else{
            auto nxt=dp;
            if(P==2){
                chmax(nxt[0][0][1],dp[0][0][0]);
                chmax(nxt[0][0][0],dp[0][0][1]+1);
            }
            if(P==3){
                if(g==1){
                    REP(i,N)REP(j,N){
                        chmax(nxt[i+1][j][0],dp[i][j][0]);
                        if(j>0)chmax(nxt[i][j-1][0],dp[i][j][0]+1);
                        if(i>0)chmax(nxt[i-1][j+1][0],dp[i][j][0]);
                    }
                }
                if(g==2){
                    REP(i,N)REP(j,N){
                        chmax(nxt[i][j+1][0],dp[i][j][0]);
                        if(j>0)chmax(nxt[i+1][j-1][0],dp[i][j][0]);
                        if(i>0)chmax(nxt[i-1][j][0],dp[i][j][0]+1);
                    }
                }

            }
            if(P==4){
                if(g==1){
                    REP(i,N)REP(j,N)REP(k,N){
                        chmax(nxt[i+1][j][k],dp[i][j][k]);
                        if(i>0)chmax(nxt[i-1][j+1][k],dp[i][j][k]);
                        if(j>0)chmax(nxt[i][j-1][k+1],dp[i][j][k]);
                        if(k>0)chmax(nxt[i][j][k-1],dp[i][j][k]+1);

                    }
                }
                if(g==2){
                    REP(i,N)REP(j,N)REP(k,N){
                        chmax(nxt[i][j+1][k],dp[i][j][k]);
                        if(i>0)chmax(nxt[i-1][j][k+1],dp[i][j][k]);
                        if(j>0)chmax(nxt[i][j-1][k],dp[i][j][k]+1);
                        if(k>0)chmax(nxt[i+1][j][k-1],dp[i][j][k]);

                    }
                }
                if(g==3){
                    REP(i,N)REP(j,N)REP(k,N){
                        chmax(nxt[i][j][k+1],dp[i][j][k]);
                        if(i>0)chmax(nxt[i-1][j][k],dp[i][j][k]+1);
                        if(j>0)chmax(nxt[i+1][j-1][k],dp[i][j][k]);
                        if(k>0)chmax(nxt[i][j+1][k-1],dp[i][j][k]);
                    }
                }

            }
            swap(dp,nxt);
        }
    }
    int res=0;
    REP(i,N+1)REP(j,N+1)REP(k,N+1){
        if(i+j+k>0)chmax(res,dp[i][j][k]+1);
        else chmax(res,dp[i][j][k]);
    }
    cout<<res<<endl;
    /*
    if(N<=8){
        int ans=0;
        vector<int> o(N);
        iota(ALL(o),0);
        do{
            int rest=0;
            int p=0;
            REP(i,N){
                if(rest==0)p++;
                rest+=G[o[i]];
                rest%=P;
            }
            chmax(ans,p);
        }while(next_permutation(ALL(o)));
        cout<<ans<<endl;
        assert(res==ans);
    }
    */
}
int main(){
    int T;
    cin>>T;
    FOR(i,1,T+1){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
