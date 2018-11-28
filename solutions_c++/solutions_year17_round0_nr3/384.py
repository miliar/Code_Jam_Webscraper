#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
#ifdef LOCAL
    #define D(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
    #define D(...) ;
    #define cerr if(0)cout
#endif
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=','){cerr<<*sdbg++;}cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

void read_data() {

}

slong go(slong P1, slong I1, slong P2, slong I2, slong k) {
	
	//D(P1, I1, P2, I2, k);

	map<slong, slong> W;
	if(k <= I1) return P1;
	k -= I1;
	if(k <= I2) return P2;
	k -= I2;
	W[(P1-1)/2] += I1;
	W[(P2-1)/2] += I2;
	W[(P1)/2] += I1;
	W[(P2)/2] += I2;
	
	assert(W.size() == 2);
	vector<slong> A;
	for(auto x : W ) A.PB(x.X);
	reverse(ALL(A));
	return go(A[0], W[A[0]], A[1], W[A[1]], k);
}

int T;
void solve() {
	slong n,k;
	scanf("%lld%lld", &n,&k);

	auto a = go(n,1,n-1,0,k);
	printf("Case #%d: %lld %lld\n", ++T, a/2, (a-1)/2);
}

int main() {
	int t;
	scanf("%d", &t);
	while(t--)
    solve();
}
