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

bool check(vector<int> M, vector<int> S, ldouble m, int d) {
	FORW(i,0,SIZE(M)) {
		if(m > S[i]+EPS) {
			if(M[i]*1LL*S[i]/(m-S[i]) + M[i] < d+EPS) {
				return false;
			}
		}
	}
	return true;
}

int T;
void solve() {
	vector<int> M,S;
	ldouble p = 0;
	ldouble k = 50000000000000.0;

	int n,d;
	scanf("%d%d", &d, &n);
	FOR(i,1,n) {
		int m,s;
		scanf("%d%d",&m,&s);
		M.PB(m);
		S.PB(s);
	}

	FOR(_,1,120) {
		ldouble m = (p+k)/2;
		if(check(M,S,m,d)) p = m;
		else k = m;
	}

	printf("Case #%d: %Lf\n", ++T, p);
}

int main() {
	int t;
	scanf("%d",&t);
	while(t--) solve();
}
