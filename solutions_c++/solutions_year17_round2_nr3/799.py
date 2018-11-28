#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;

using pll = pair<ll, ll>;
using vll = vector<ll>;
using vpll = vector<pll>;

#define pb push_back
#define FOR(i, m, n) for (ll i(m); i < n; i++)
#define REP(i, n) FOR(i, 0, n)
#define F(n) REP(i, n)
#define FF(n) REP(j, n)
struct d_ {
    template<typename T> d_ & operator ,(const T & x) { cerr << ' ' <<  x; return *this;}
    template<typename T> d_ & operator ,(const vector<T> & x) { for(auto x: x) cerr << ' ' <<  x; return *this;}
} d_t;
#define D(args ...) { d_t,"|",__LINE__,"|",#args,":",args,"\n"; }
#define dbg(args ...) D(args)
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second

#define MX 107

ll n,q;
ll E[MX], S[MX];
ll D[MX][MX];

map<ll,double> DP[MX][MX];

double dp(ll pos, ll h, ll e) {
    if(pos==n) return 0;
    if(DP[pos][h].count(e)) return DP[pos][h][e];
    double ret=INF;
    if(D[pos][pos+1]<=e) ret=min(ret, dp(pos+1,h,e-D[pos][pos+1])+double(D[pos][pos+1])/S[h]);
    if(D[pos][pos+1]<=E[pos]) ret=min(ret, dp(pos+1,pos,E[pos]-D[pos][pos+1])+double(D[pos][pos+1])/S[pos]);
    DP[pos][h][e] = ret;
    return ret;
}

void solve() {
    F(MX)FF(MX)DP[i][j].clear();
    CL(E,0);
    CL(S,0);
    CL(D,0);
    cin>>n>>q;
    F(n) cin>>E[i]>>S[i];
    F(n)FF(n) cin>>D[i][j];
    F(q) {
        ll u,v; cin>>u>>v; u--;v--;
        cout<<fixed<<setprecision(8)<<dp(0,0,E[0])<<endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    ll t;cin>>t;
    for(int i=0; i<t; i++) {
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}
