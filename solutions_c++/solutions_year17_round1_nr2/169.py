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

const ll MOD = 1000000009;
const ll INF = 1e15;
const double EPS = 1e-8;

void solve() {
	int N, P; cin >> N >> P;
	vi R(N);
	for (auto& x : R) cin >> x;
	vvi Q(N, vi(P));
	for (auto& y : Q) for (auto& x : y) cin >> x;
	
	// Compute min and max # servings for each packet
	vvi lo_servings(N, vi(P)), hi_servings(N, vi(P));
	for (int i=0; i<N; i++) for (int j=0; j<P; j++) {
		
		int lo = (int)((10LL * Q[i][j] + 11LL * R[i] - 1) / (11LL * R[i]));
		int hi = (int)((10LL * Q[i][j]) / (9LL * R[i]));
		
		lo_servings[i][j] = lo;
		hi_servings[i][j] = hi;
	}
	
	// Sort the intervals
	vector<vector<pii>> servings(N, vector<pii>(P));
	for (int i=0; i<N; i++) for (int j=0; j<P; j++)
		servings[i][j] = {lo_servings[i][j], hi_servings[i][j]};
	for (int i=0; i<N; i++) sort(servings[i].begin(), servings[i].end());
	
	// Greedy
	int ans = 0;
	vi current(N, 0);
	
	while (*max_element(current.begin(), current.end()) < P) {
		vi kit(N, -1);
		kit[0] = current[0];
	
		// Can we use the current column?
		int l, r; tie(l,r) = servings[0][current[0]];
		for (int i=1; i<N; i++) {
			l = max(l, servings[i][current[i]].X);
			r = min(r, servings[i][current[i]].Y);
		}
		if (l <= r) {  // Yes we can!
			ans++;
			for (int i=0; i<N; i++) current[i]++;
		}
		else {  // No we can't :(
			for (int i=0; i<N; i++) {
				if (servings[i][current[i]].Y < l) current[i]++;
			}
		}
	}
	
	
	cout << ans << endl;
}

int main() {
	int T=0; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cerr << "Solved test case " << t << endl;
	}
}



















