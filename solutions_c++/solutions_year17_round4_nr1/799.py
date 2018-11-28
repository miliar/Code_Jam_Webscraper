#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

using namespace std;

template<class T>bool chmax(T &a, const T &b) { return (a < b) ? (a = b, 1) : 0;}
template<class T>bool chmin(T &a, const T &b) { return (b < a) ? (a = b, 1) : 0;}

using ll = long long;
using R = long double;
const R EPS = 1e-9L; // [-1000,1000]->EPS=1e-8 [-10000,10000]->EPS=1e-7
inline int sgn(const R& r) {return (r > EPS) - (r < -EPS);}
inline R sq(R x) {return sqrt(max(x, 0.0L));}

const int dx[8] = {1, 0, -1, 0, 1, -1, -1, 1};
const int dy[8] = {0, 1, 0, -1, 1, 1, -1, -1};

// Problem Specific Parameter:

int n, p;
int memo[110][110][110][4];


int rec(int g1, int g2, int g3, int cur) {
	if (g1 == 0 and g2 == 0 and g3 == 0) return 0;
	int &ret = memo[g1][g2][g3][cur];
	if (ret >= 0) return ret;

	ret = 0;
	const int add = (cur == 0);
	if (g1 > 0) chmax(ret, add + rec(g1 - 1, g2, g3, (cur + 1) % p));
	if (g2 > 0) chmax(ret, add + rec(g1 , g2 - 1, g3, (cur + 2) % p));
	if (g3 > 0) chmax(ret, add + rec(g1 , g2, g3 - 1, (cur + 3) % p));
	return ret;
}

int main(void) {
	// GCJ Template
	int T;
	cin >> T;
	rep(testcase, 1, T + 1) {
		cin >> n >> p;

		vector<int> g(4, 0);

		rep(i, n) {
			int in;
			cin >> in;
			g[in % p]++;
		}

		rep(i, g[1] + 1)rep(j, g[2] + 1)rep(k, g[3] + 1)rep(l, p + 1) memo[i][j][k][l] = -1;


		int ans = g[0] + rec(g[1], g[2], g[3], 0);


		cout << "Case #" << testcase << ": " << ans << endl;
		cerr << "Case #" << testcase << ": Done!"  << endl;
	}
	return 0;
}