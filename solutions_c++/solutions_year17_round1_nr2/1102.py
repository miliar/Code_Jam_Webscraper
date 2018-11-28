#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#pragma GCC optimize ("O3")

using namespace std;

using LL = long long;
using vi = vector<int>;
using pii = pair<int, int>;
using vpii = vector<pair<int, int>>;
using vll = vector<LL>;
using LD = long double;

#define ALL(v) v.begin(), v.end()
#define endl '\n'
#define SYNC ios_base::sync_with_stdio(false); cin.tie(NULL); cerr.tie(NULL);
#define REP(i , n) for(int i =0 ; i < n ;i++)
#define REPN(i , n) for(int i = 1; i <= n ; i++)
#define cot(x) cerr << #x << " " << x << " ";
#define cotd(x) cerr << #x << " " << x << endl;
#define her 	cerr << " here \n"; 
#define pp push_back
#define fi first 
#define se second
#define un(x) x.erase(unique(ALL(x)), x.end())

template<typename T > void check(T & a, const T & b) { if (a >= b) { a %= b; } }
template<typename T>T gcd(T u, T v) { if (u == v)return u; if (u == 0)return v; if (v == 0)return u; if (~u & 1) { if (v & 1) return gcd(u >> 1, v); else return gcd(u >> 1, v >> 1) << 1; }if (~v & 1)return gcd(u, v >> 1); if (u > v)return gcd((u - v) >> 1, v); return gcd((v - u) >> 1, u); }
LL mulmod(LL a, LL b, const LL & m) { LL q = (LL)(((LD)a*(LD)b) / (LD)m); LL r = a*b - q*m; if (r>m)r %= m; if (r<0)r += m; return r; }
template <typename T, typename S>T expo(T e, S n) { T x = 1, p = e; while (n) { if (n & 1)x = x*p; p = p*p; n >>= 1; }return x; }
template <typename T>T powerL(T e, T n, const T & m) { T x = 1, p = e; while (n) { if (n & 1)x = mulmod(x, p, m); p = mulmod(p, p, m); n >>= 1; }return x; }

int q[51][51]; 
int n, p; 
int r[51], dp[1 << 8][1 << 8]; 

bool ch(int ii, vi x){
	REP(i, 2){
		int a = ii * 10 * r[i];
		int b = 9 * q[i][x[i]]; 
		int c = 11 * q[i][x[i]]; 
		if(a < b || a > c) return false; 
	}
	return true; 
}

int solve(int i, int j){
	if(i == ((1 << p) - 1) || j == (1 << p) - 1 ) return 0; 
	int & ans = dp[i][j]; 
	if(ans != -1) return ans; 
	ans = 0; 
	REP(x, p){
		if((i >> x) & 1)continue;
		int a = (10 * q[0][x])/(9 * r[0]); 
		int b = (10 * q[0][x] + (11* r[0]) - 1)/(11 * r[0]);
//		if(a == 0)a++; 
//		if(b == 0)b++; 
		REP(y, p){
			if((j >> y) & 1) continue; 
			int a1 = (10 * q[1][y])/(9 * r[1]); 
			int b1 = (10 * q[1][y] + (11* r[1]) - 1)/(11 * r[1]);
//			if(a1 == 0)a1++; 
//			if(b1 == 0)b1++;  
			int l = min(a1, a), r = max(b1, b); 
			bool can = false; 
			//cerr << l << " " << r << endl; 
			if((r == 0 && l - r + 1 >= 2) || (r != 0 && r <= l)){
				ans = max(ans, 1 + solve(i | (1 << x), j | (1 << y))); 
			}
		}
	}
	return ans; 
}

int main(){
	SYNC;
	cerr << fixed << setprecision(10); 
	double c1 = clock();  
	int T; int caseno = 1; 
	cin >> T; 

	while(T--){
		cout << "Case #" << caseno++ << ": "; 
		memset(dp, -1, sizeof dp); 
		cin >> n >> p; 
		REP(i, n) cin >> r[i]; 
		REP(i, n) REP(j, p) cin >> q[i][j]; 
		int ans = 0; 
		if(n == 1){
			REP(x, p){
				int a = (10 * q[0][x])/(9 * r[0]); 
				int b = (10 * q[0][x] + (11* r[0]) - 1)/(11 * r[0]);
				int l = a, r = b; 
				if((r == 0 && l - r + 1 >= 2) || (r != 0 && r <= l)){
					ans++; 
				} 		
			}
			cout << ans << endl;
			continue; 
		}
		cout << solve(0, 0) << endl; 
	}
	cerr << (clock() - c1) / CLOCKS_PER_SEC << endl; 
}