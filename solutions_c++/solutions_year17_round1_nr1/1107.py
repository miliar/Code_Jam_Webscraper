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

int main(){
	SYNC;
	cerr << fixed << setprecision(10); 
	double c1 = clock();  
	int T; int caseno = 1; 
	cin >> T; 

	while(T--){
		cout << "Case #" << caseno++ << ":\n";
		int r, c; 
		cin >> r >> c; 
		string s[25], f[26]; 
		int vis[26]; 
		REP(i, r) cin >> s[i];  

		REP(i, r){
			bool ans = false; 
			REP(j, c){
				if(s[i][j] != '?'){
					ans = true; 
					char x = s[i][j];
					int j1 = j - 1; 
					while(j1 >= 0 && s[i][j1] == '?'){
						s[i][j1] = x; 
						//cerr << s[i][j1] << endl; 
						j1--; 
					}
					j1 = j + 1; 
					while(j1 < c && s[i][j1] == '?'){
						s[i][j1] = x; 
						j1++; 
					}
				}
			}
			if(!ans && i > 0) s[i] = s[i-1]; 
		}

		for(int i = r - 1; i >= 0; i--){
			bool ans = false; 
			for(int j = 0; j < c; j++){
				if(s[i][j] != '?'){
					ans = true; 
					break; 
				}
			}
			if(!ans && i != r - 1) s[i] = s[i+1]; 
		}

		REP(i, r) cout << s[i] << endl; 
	}
	cerr << (clock() - c1) / CLOCKS_PER_SEC << endl; 
}