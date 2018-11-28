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

#define MX 100007

void imp() { cout<<"IMPOSSIBLE"<<endl; }

void solve() {
    IN(n);
    ll nx=n;
    IN(R); IN(O); IN(Y); IN(G); IN(B); IN(V);
    if(B+O==n && B==O) { F(B) cout<<"BO"; cout<<endl; return ; }
    if(Y+V==n && Y==V) { F(Y) cout<<"YV"; cout<<endl; return ; }
    if(R+G==n && R==G) { F(R) cout<<"RG"; cout<<endl; return ; }
    if((G&&R<=G) || (O&&B<=O) || (V&&Y<=V)) { imp(); return ;}
    if(G) { n-=2*G; R-=G; }
    if(O) { n-=2*O; B-=O; }
    if(V) { n-=2*V; Y-=V; }
    vector<pair<ll,char>> v = {{R,'R'},{Y,'Y'},{B,'B'}};
    dbg(R,Y,B);
    sort(all(v));
    string s(n,0);
    auto a=v[2],b=v[1],c=v[0];
    if(a.x>n/2) { imp(); return ; }
    for(ll i=0; i<a.x; i++) s[i*2]=a.y;
    bool o=1;
    for(ll i=n-1; i>=0; i--) {
        if(s[i])continue;
        if(o || !c.x) { s[i]=b.y; b.x--; }
        else { s[i]=c.y; c.x--; }
        o=!o;
    }
    bool ok=1;
    F(n-1) ok&=s[i]!=s[i+1];
    if(!ok) {imp(); return ;}
    bool ig = G, io=O, iv=V;
    F(n) {
        cout<<s[i];
        nx--;
        if(s[i]=='R' && ig) { F(G) {nx-=2;cout<<"GR";} ig=0; }
        if(s[i]=='B' && io) { F(O) {nx-=2;cout<<"OB";} io=0; }
        if(s[i]=='Y' && iv) { F(V) {nx-=2;cout<<"VY";} iv=0; }
    }
    assert(nx==0);
    cout<<endl;
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
