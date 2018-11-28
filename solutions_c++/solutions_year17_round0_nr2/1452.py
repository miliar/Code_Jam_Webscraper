#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ull = unsigned long long;
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

void solve() {
    vll a;
    ull n;cin>>n;
    for(ull cur=n; cur>0; cur/=10) a.pb(cur%10);
    ull len=a.size();
    reverse(all(a));
    ll firstdown=-1;
    FOR(i,1,len) if(a[i-1]>a[i]) { firstdown=i-1; break; }
    while(firstdown>0 && a[firstdown]==a[firstdown-1]) firstdown--;
    if(~firstdown) {
        a[firstdown]--;
        FOR(i,firstdown+1,len) a[i]=9;
    }
    ll ret=0;
    for(auto i: a) ret=10*ret+i;
    cout<<ret<<endl;
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

