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

ll Hd, Ad, Hk, Ak, B, D;

int simulate(int num_buffs, int num_debuffs) {
	int turns = 0;

	ll my_health = Hd, enemy_health = Hk;
	ll my_attack = Ad, enemy_attack = Ak;
	
	while (my_health > 0 && enemy_health > 0) {
		if (turns > 250) return INT_MAX;
		if (my_attack >= enemy_health) enemy_health = 0;  		// Secure the kill
		else if (my_health <= enemy_attack										// About to die
			&& (my_health <= (enemy_attack - D) || num_debuffs == 0)) { 								
			my_health = Hd;  						// Heal
			my_health -= enemy_attack;  // Get hit
		}
		else {
			if (num_debuffs)
				enemy_attack = max(enemy_attack - D, 0LL), num_debuffs--;		// Cast debuff
			else if (num_buffs)
				my_attack += B, num_buffs--;		// Cast buff
			else
				enemy_health -= my_attack;		// Hit the cunt
			
			my_health -= enemy_attack;		// Get hit
		}
		turns++;
	}
	
	if (my_health <= 0) return INT_MAX;
	else return turns;
}

void solve() {
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	
	int ans = INT_MAX;
	
	for (int num_buffs = 0; num_buffs <= 100; num_buffs++) {
		for (int num_debuffs = 0; num_debuffs <= 100; num_debuffs++) {
			ans = min(ans, simulate(num_buffs, num_debuffs));
		}
	}
	
	if (ans == INT_MAX) cout << "IMPOSSIBLE" << endl;
	else cout << ans << endl;
}

int main() {
	int T=0; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cerr << "Solved test case " << t << endl;
	}
}



















