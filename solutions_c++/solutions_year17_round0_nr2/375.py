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

slong MN[19];

slong getL(slong n) {
	slong l = 0;
	while(n) {
		n /= 10;
		l++;
	}
	return l;
}

slong filll(slong x, int d, int dl) {
	while(x < MN[dl]) x = x*10+d;
	return x;
}

slong go(slong n) {
	int d = getL(n);
	if(filll(0,1,d) > n) return filll(0,9,d-1);
	if(filll(0,9,d) == n) return n;

	slong ret = 0;
	int D = 1;
	FOR(i,1,d){
		while(D < 9 and filll(ret, D+1, d) <= n) D++;
		ret = ret*10+D;
	}
	return ret;
}

int T;
void solve() {
	slong ans = 1;
	slong n;
	scanf("%lld", &n);
	ans = go(n);

	printf("Case #%d: %lld\n", ++T, ans);
}

int main() {
	MN[0] = 1;
	MN[1] = 1;
	FOR(i,2, 18) MN[i] = MN[i-1]*10;
	int t;
	scanf("%d", &t);
	while(t--)
    solve();
}
