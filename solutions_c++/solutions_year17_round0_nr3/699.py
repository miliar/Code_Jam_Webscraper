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

int caseno;

pair<LL,LL> solve(LL &n, LL &k){
	set<pair<LL,LL>> s = {{n, 1LL}}; 

	REP(i, 64){
		if(!k) break; 
		if(k - (1LL << i) <= 0){
			//cerr << caseno - 1 << " " << n << " " << k << " " << s.size() << endl; 
			auto it = s.end();
			it--;  
			if(it->se >= k) return {(it->fi >> 1LL), {it->fi - 1 - (it->fi >> 1LL)}};
			it--; 
			return {(it->fi >> 1LL), {it->fi - 1 - (it->fi >> 1LL)}};
		}
		else{
			vector<pair<LL,LL>> temp; 
			while(!s.empty()){
				auto x = *(s.begin());
				LL a = x.fi, b = x.se; 
				temp.pp({a >> 1LL, b}); 
				temp.pp({a - 1 - (a >> 1LL), b}); 
				s.erase(s.begin()); 
			}
			map<LL,LL> m; 
			for(auto & i : temp){
				if(i.fi > 0) m[i.fi] += i.se; 
			}
			for(auto & i : m) s.insert(i); 
				k -= (1LL << i); 
		} 
	}
}

void find(LL n){
	set<LL> s = {n}; 
	
	while(!s.empty()){
		vi temp; 
		while(!s.empty()){
			LL a = *(s.begin());
			temp.pp(a >> 1); 
			temp.pp(a - 1 - (a >> 1LL)); 
			s.erase(s.begin()); 
			cerr << a << " "; 
		}
		cerr << endl; 
		for(auto & i : temp)
			if(i > 0) s.insert(i); 
		cerr << "Case NO " << caseno - 1 << " " << s.size() << endl; 
	}
	return;
}

int main(){
	SYNC; 
	int T;  
	cin >> T; 
	caseno = 1; 

	while(T--){
		cout << "Case #" << caseno++ << ": "; 
		LL n, k; 
		cin >> n >> k;

		auto x = solve(n, k); 
		cout << x.fi << " " << x.se << endl; 
		//find(n); 
	}
	return 0; 
}