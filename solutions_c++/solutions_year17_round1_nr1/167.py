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
	int R, C; cin >> R >> C;
	vector<string> grid(R);
	for (auto& x : grid) cin >> x;
	
	vi good;
	
	for (int c=0; c<C; c++) {
		int f=-1;
		for (int r=0; r<R; r++) {
			if (grid[r][c] != '?') { f = r; break; }
		}
		if (f != -1) {
			for (int r=0; r<R; r++) {
				if (grid[r][c] != '?') f = r;
				else grid[r][c] = grid[r][c] = grid[f][c];
			}
			good.push_back(c);
		}
	}
	
	for (int c=0; c<C; c++) {
		if (grid[0][c] == '?') {
			int cpy=-1;
			auto it = lower_bound(good.begin(), good.end(), c);
			if (it != good.end()) cpy = *it;
			else cpy = *prev(it);
			
			for (int r=0; r<R; r++) grid[r][c] = grid[r][cpy];
		}
	}

	for (int r=0; r<R; r++) {
		cout << endl;
		for (int c=0; c<C; c++) {
			cout << grid[r][c];
		}
	}
	cout << endl;
}

int main() {
	int T=0; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ":";
		solve();
	}
}



















