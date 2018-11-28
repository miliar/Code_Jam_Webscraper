#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
#include <cassert>

#if __cplusplus >= 201103L
#include <array>
#include <tuple>
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <forward_list>

#define cauto const auto&
#endif

using namespace std;


namespace{

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T, class U=T>
void initvv(vector<vector<T> > &v, int a, int b, const U &t = U()){
	v.assign(a, vector<T>(b, t));
}
template <class T> inline T &chmin(T &x, const T &y){ return x = min(x, y); }
template <class T> inline T &chmax(T &x, const T &y){ return x = max(x, y); }
template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}

template <class Con>
string concat(const Con &c, string spl){
	stringstream ss;
	typename Con::const_iterator it = c.begin(), en = c.end();
	bool fst = true;
	for(; it != en; ++it){
		if(!fst){ ss << spl; }
		fst = false;
		ss << *it;
	}
	return ss.str();
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back


#define MOD 1000000007LL
#define EPS 1e-8

const int INF = 1010101010;
const int Z = 106;
int dps[5][Z][Z][Z];

typedef tuple<int,int,int> ti3;

void init(int p){
	auto dp = dps[p];
	for(int i = 0; i < Z; ++i)
	for(int j = 0; j < Z; ++j)
	for(int k = 0; k < Z; ++k){
		dp[i][j][k] = -INF;
	}
	
	vector<ti3> cmb;
	for(int a = 0; a <= p; ++a)
	for(int b = 0; b <= (p > 2 ? p : 0); ++b)
	for(int c = 0; c <= (p > 3 ? p : 0); ++c){
		if(a + b + c > 0 && (a + 2 * b + 3 * c) % p == 0){
			cmb.emplace_back(a, b, c);
		}
	}
	
	dp[0][0][0] = 0;
	for(int i = 0; i < Z - p; ++i)
	for(int j = 0; j < Z - p; ++j)
	for(int k = 0; k < Z - p; ++k){
		if(dp[i][j][k] < 0){ continue; }
		for(cauto t : cmb){
			int a = i + get<0>(t);
			int b = j + get<1>(t);
			int c = k + get<2>(t);
			chmax(dp[a][b][c], dp[i][j][k] + 1);
		}
	}
}

void prepare(){
//	ios::sync_with_stdio(false);
	for(int p = 2; p <= 4; ++p){
		init(p);
	}
}


LL solve(){
	int n, p;
	cin >> n >> p;
	int cnt[4] = {};
	for(int i = 0; i < n; ++i){
		int g;
		cin >> g;
		++cnt[g % p];
	}
	
	auto dp = dps[p];
	int ans = 0;
	for(int i = 0; i <= cnt[1]; ++i)
	for(int j = 0; j <= cnt[2]; ++j)
	for(int k = 0; k <= cnt[3]; ++k){
		int t = dp[i][j][k];
		if(i < cnt[1] || j < cnt[2] || k < cnt[3]){ ++t; }
		chmax(ans, t);
	}
	
	ans += cnt[0];
	return ans;
}


}
int main(){
	cout << fixed << setprecision(15);
	cerr << fixed << setprecision(6);
	prepare();

	string str = "_";
	getline(cin, str);
	int T = strtol(str.c_str(), 0, 10);
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans << endl;
	}
}
