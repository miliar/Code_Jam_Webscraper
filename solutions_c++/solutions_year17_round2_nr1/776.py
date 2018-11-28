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

void solve() {
    ll d,n; cin>>d>>n;
    vpll v;
    F(n) {
        ll k,s; cin>>k>>s;
        v.pb({k,s});
    }
    sort(all(v));
    double mt=0;
    for(ll i=v.size()-1; i>=0; i--) {
        mt=max(mt, double(d-v[i].x)/v[i].y);
    }
//    dbg(mt);
    cout << fixed << setprecision(8) << double(d)/mt <<endl;
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
