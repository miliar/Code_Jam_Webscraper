#include <bits/stdc++.h>
using namespace std;

namespace {
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define len(x) (int)((x).size())
#define X first
#define Y second

#define FOR(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#ifndef ONLINE_JUDGE
#include "debug.h"
#else
#define DEBUG(...) 
#define DEBUG_2D(...)
#endif  // ONLINE_JUDGE
  
typedef long long int ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
template<typename T> using minpq = priority_queue<T, vector<T>, greater<T>>;

ll expmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
template<typename T> T sqr(const T& x) { return x*x; }
ll flog(const ll x) { return 63 - __builtin_clzll(x); }
template<typename T> void sort(T& t) { sort(all(t)); }
template<typename T> void undupe(vector<T>& v) { sort(v); v.erase(unique(all(v)), v.end()); }

struct _IOS { _IOS() { ios::sync_with_stdio(0); cin.tie(0); } } _IOS;
}

const ll MOD = 1e9 + 9;
const ll INF = 1e15;
const double EPS = 1e-8;

void solve_small() {
    ll N, K; cin >> N >> K;
   
    priority_queue<ll> pq;
    pq.emplace(N);
    
    ll L, R;
    
    while (K--) {
        ll top = pq.top();  pq.pop();
        L = (top-1)/2, R = top/2;
        pq.emplace(L), pq.emplace(R);
    }
    cout << max(L,R) << ' ' << min(L,R) << '\n';
}

set<pair<ll, ll>> q;

void insert(ll x, ll n) {
    auto lb = q.lower_bound({x,0});
    if (lb != q.end() && lb->X == x) {
        n += lb->Y;
        q.erase(lb);
        q.emplace(x, n);
    } else q.emplace(x, n);
}

void solve() {
    ll N, K; cin >> N >> K;
    
    q = {{N,1}};
    ll L, R;

    while (K > 0) {
        auto cur = *q.rbegin();
        L = (cur.X-1)/2, R = cur.X/2;
        K -= cur.Y;
        q.erase(cur);
        insert(L, cur.Y);
        insert(R, cur.Y);
    }
    cout << max(L,R) << ' ' << min(L,R) << '\n';
}

int main() {
	int T; cin >> T;
	for (int t=1; t<=T; t++) {
	    cerr << "Solving case " << t << endl;
		cout << "Case #" << t << ": ";
		solve();
	}
}

