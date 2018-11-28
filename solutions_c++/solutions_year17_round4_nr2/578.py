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
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

void read_data() {

}

void solve() {
	int n,c,m;
	cin >> n >> c >> m;
	vector<int> C(c+3);
	vector<int> P(n+3);
	int st = 0;
	FOR(i,1,m) {
		int a,b;
		cin >> a >> b;
		C[b]++;
		P[a]++;
		st = max(st, C[b]);
	}
	
	int p = st-1;
	int k = m+1;
	int cost=0;
	while(p+1 < k) {
		int mid = (p+k)/2;
		cost = 0;
		int pop = 0;
		FORD(i,n,1) {
			if(P[i] >= mid) {
				pop += P[i]-mid;
				cost += P[i]-mid;
			}
			else {
				pop = max(0, pop - (mid-P[i]));
			}
		}
		if(pop > 0) p = mid;
		else k = mid;
	}
	cout << k << " " << cost << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(i,1,T) {
		cout << "Case #" << i <<": ";
		solve();
	}
}
