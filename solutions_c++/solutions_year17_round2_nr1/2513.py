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
	cout << fixed << setprecision(10); 
	double c1 = clock();  
	int T; int caseno = 1; 
	cin >> T; 

	while(T--){
		cout << "Case #" << caseno++ << ": "; 
		int d, n; 
		cin >> d >> n; 
		vector<pair<long double,long double>> v(n); 
		vector<bool> same(n + 1, 0); 
		vector<long double> ti(n); 

		REP(i, n){
			cin >> v[i].fi >> v[i].se; 
		}

		sort(ALL(v)); 
		ti[n - 1] = (d - v[n - 1].fi)/v[n - 1].se; 

		cerr << ti[n - 1] << endl; 

		for(int i = n - 2; i >= 0; i--){
			LD t = (d - v[i].fi) / (v[i].se); 
			if(t < ti[i + 1]){
				v[i].fi = v[i + 1].fi;
				ti[i] = ti[i + 1]; 
			}
			else{
				ti[i] = (d - v[i].fi)/ v[i].se; 
			}
		}

		LD ans = d/ ti[0];
		cout << ans << endl;  
	}
	cerr << (clock() - c1) / CLOCKS_PER_SEC << endl; 
}