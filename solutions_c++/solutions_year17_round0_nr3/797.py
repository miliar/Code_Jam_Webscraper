#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

ull N,K;
int T;

unordered_map<ull,ull> f_val,g_val;
ull g(ull n);
ull f(ull n){
	if(f_val.count(n)) return f_val[n];
	if(n==1) {f_val[1] = N/2; return f_val[1];}
	int ld_zr = __builtin_clzll(n);
	int msd = 63 - ld_zr;
	ull m = n&(~ (1ULL << msd));
	m |= (1ULL << (msd-1));
	if( (n >> (msd-1)) & 1){
		f_val[n] = g(m)/2;
		return f_val[n];
	}else{
		f_val[n] = f(m)/2;
		return f_val[n];
	}
}
ull g(ull n){
	if(g_val.count(n)) return g_val[n];
	if(n==1) {g_val[1] = (N-1)/2;return g_val[1];}
	int ld_zr = __builtin_clzll(n);
	int msd = 63 - ld_zr;
	ull m = n&(~ (1ULL << msd));
	m |= (1ULL << (msd-1));
	if( (n >> (msd-1)) & 1 ){
		g_val[n] = (g(m)-1)/2;
		return g_val[n];
	}else{
		g_val[n] = (f(m)-1)/2;
		return g_val[n];
	}
}

int main(){
	cin >> T;
	for(int t=1;t<=T;++t) {
		f_val.clear(),g_val.clear();
		cin >> N >> K;
		cout << "Case #" << t << ": ";
		cout << f(K) << " " << g(K) << endl;
	}
}