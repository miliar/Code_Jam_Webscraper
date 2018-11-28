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
	vi G(N);
	for (auto& x : G) cin >> x;

	vi rem(P);
	for (int x : G) rem[x % P]++;
	
	int res = rem[0];

	if (P == 2) res += (rem[1] + 1) / 2;
	
	if (P == 3) {
		int mm = min(rem[1], rem[2]);
		res += mm;
		rem[1] -= mm;
		rem[2] -= mm;
		res += (rem[1] + 2) / 3;
		res += (rem[2] + 2) / 3;
	}
	
	if (P == 4) {
		int mm = min(rem[1], rem[3]);
		res += mm;
		rem[1] -= mm;
		rem[3] -= mm;
		if (rem[3] == 0) {
			mm = min(rem[1], rem[2]);
			res += mm;
			rem[1] -= mm;
			rem[2] -= mm;
			res += (rem[1] + 2) / 3;
			res += (rem[2] + 2) / 3;
		} else {
			res += rem[2] / 2;
			rem[2] = rem[2] % 2;
			if (rem[2] && rem[3] >= 2) {
				res += 1;
				rem[2]--;
				rem[3] -= 2;
				res += (rem[3] + 3) / 4;
			}
			else res += (rem[3] + 3) / 4;
		}
	}

	cout << res << endl;
}

int main() {
	int T=0; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cerr << "Solved test case " << t << endl;
	}
}



















