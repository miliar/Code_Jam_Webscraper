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

unordered_map<slong, int> A[5][5];

slong get(slong a, int b, int c, int d) {
	return (((a*101+b)*101+c)*101+d);
}

int GO(int p, int r, int a, int b, int c, int d) {
	if(a < 0 or b < 0 or c < 0 or d < 0) return 1234;
	if(a == 0 and b == 0 and c == 0 and d == 0) return 0;
	if(A[p][r].find(get(a,b,c,d)) != A[p][r].end()) return A[p][r][get(a,b,c,d)];

	int ans = 1234;
	ans = min(ans, GO(p, r, a-1,b,c,d));
	ans = min(ans, GO(p, (r+p-1)%p, a,b-1,c,d));
	ans = min(ans, GO(p, (r+p-2)%p, a,b,c-1,d));
	ans = min(ans, GO(p, (r+p-3)%p, a,b,c,d-1));
	if(r > 0) ans++;
	A[p][r][get(a,b,c,d)] = ans;
	return ans;
}

void solve() {
	int n,p;
	cin >> n >> p;
	vector<int> G;
	FOR(i,0,3) G.PB(0);
	FOR(i,1,n) {
		int g;
		cin >> g;
		G[g%p]++;
	}
	cout << n-GO(p,0,G[0], G[1], G[2], G[3]) << "\n";;
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
