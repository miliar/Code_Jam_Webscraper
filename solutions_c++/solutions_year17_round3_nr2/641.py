#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#pragma GCC optimize ("O3")

using namespace std;

using LL = long long;
template<typename T> using V = vector<T>; 
template<typename T, typename S> using P = pair<T, S>; 
using LD = long double;

#define ALL(v) v.begin(), v.end()
#define endl '\n'
#define SYNC ios_base::sync_with_stdio(false); cin.tie(NULL); cerr.tie(NULL);
#define REP(i , n) for(int i =0 ; i < n ;i++)
#define REPN(i , n) for(int i = 1; i <= n ; i++)
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

const int N = 25 * 60; 
int x[25 * 61], dp[N][N][3]; // j is for jameron
//1 for cam, 2 for jamie

const int INF = (int)1e9 + 7; 

int get(int X){
	if(X == 1) return 1; 
	return 2;
}

int cur; 

int solve(int i, int j, int last){
	if(j > 720 || (i - j) > 720) return INF; 
	if(i >= 24 * 60){
		if(j == 720) {
			if(last == cur) return 0; 
			else return 1; 
		} 
		return INF; 
	}
	int & ans = dp[i][j][last]; 
	if(ans != -1) return ans; 

	ans = INF; 

	if(x[i] == -1){
		if(last == 1){
			ans = min(1 + solve(i + 1, j + 1, 2), solve(i + 1, j, 1)); 
		}
		else ans = min(solve(i + 1, j + 1, 2), 1 + solve(i + 1, j, 1)); 
	}
	else{
		if(last != x[i]){
			ans = 1 + solve(i + 1, j + (x[i] == 2), x[i]); 
		}
		else ans = solve(i + 1, j + (x[i] == 2), x[i]); 
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
		int a, b; 
		cin >> a >> b;
		V<P<int,int>> c, j; 
		memset(x, -1, sizeof x); 
		memset(dp, -1, sizeof dp); 

		REP(i, a){
			int l, r; 
			cin >> l >> r; 
			c.pp({l, r}); 
			for(int j = l; j < r; j++){
				x[j] = 2; 
			}
		}
		REP(i, b){
			int l, r; 
			cin >> l >> r; 
			j.pp({l, r}); 
			for(int j = l; j < r; j++){
				x[j] = 1; 
			}
		}

		int ans = (int)1e9; 
		cur = 1; 
		ans = solve(1, 0, 1); 
		memset(dp, -1, sizeof dp); 
		cur = 2; 
		ans = min(ans, solve(1, 1, 2)); 
		cout << ans << endl; 
	}

	cerr << (clock() - c1) / CLOCKS_PER_SEC << endl; 
}