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
#define dbg(args ...) { d_t,"|",__LINE__,"|",":",args,"\n"; }
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second

void solve() {
    unordered_map<ll,ll> mp;
    ll n,k; cin>>n>>k;
    priority_queue<ll> q;
    ll act = 0;
    mp[n]=1; q.push(n);
    while(q.size()) {
        ll cur=q.top(); q.pop();
        ll l=(cur-1)/2, r=cur/2;
//        dbg(cur,mp[cur],l,r,k);
        if(mp[cur] >= k) {
            cout<<r<<' '<<l<<endl;
            break;
        }
        k-=mp[cur];
        if(!mp[l])q.push(l);
        mp[l]+=mp[cur];
        if(!mp[r])q.push(r);
        mp[r]+=mp[cur];
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

