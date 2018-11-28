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

const int INF=1001001001001001001ll;

int N,Q;
int E[111],S[111];
int D[111][111];
double d[111][111];

void solve(){
    scanf("%lld%lld",&N,&Q);
    rep(i,N)scanf("%lld%lld",&E[i],&S[i]);

    rep(i,N){
        rep(j,N){
            scanf("%lld",&D[i][j]);
            if(D[i][j]==-1)D[i][j]=INF;
            if(i==j)D[i][j]=0;
        }
    }

    rep(k,N)rep(i,N)rep(j,N)chmin(D[i][j],D[i][k]+D[k][j]);

    fill_n(*d,111*111,INF);
    rep(i,N)rep(j,N){
        if(D[i][j]<=E[i]){
            d[i][j]=1.0*D[i][j]/S[i];
        }
    }
    rep(k,N)rep(i,N)rep(j,N)chmin(d[i][j],d[i][k]+d[k][j]);

    rep(i,Q){
        int u,v;
        scanf("%lld%lld",&u,&v);
        u--;v--;

        if(i)printf(" ");
        printf("%.20f",d[u][v]);
    }
    puts("");
}

signed main(){
    int T;scanf("%lld",&T);
    rep(i,T){
        printf("Case #%lld: ",i+1);
        solve();
    }
    return 0;
}
