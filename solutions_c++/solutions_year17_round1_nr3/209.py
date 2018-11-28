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


void prepare(){
//	ios::sync_with_stdio(false);
	
}

LL encode(int hd, int ad, int hk, int ak){
	chmax(hd, 0);
	chmax(hk, 0);
	chmax(ak, 0);
	chmin(ad, hk);
	return (LL)hd << 48 | (LL)ad << 32 | (LL)hk << 16 | (LL)ak;
}

void decode(LL e, int &hd, int &ad, int &hk, int &ak){
	const LL mask = 0xffff;
	hd = e >> 48 & mask;
	ad = e >> 32 & mask;
	hk = e >> 16 & mask;
	ak = e & mask;
}

void add(set<LL> &st, queue<LL> &q, int hd, int ad, int hk, int ak){
	if(hd <= 0 || hk <= 0){ return; }
	LL e = encode(hd, ad, hk, ak);
	if(st.insert(e).second){
		q.push(e);
//cerr<<"insert "<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;
	}
}

LL solve1(){
	int hd, ad, hk, ak, b, d;
	cin >> hd >> ad >> hk >> ak >> b >> d;
	int hd0 = hd;
	set<LL> st;
	queue<LL> q;
	add(st, q, hd, ad, hk, ak);
	q.push(-1);
	int ans = 1;
	while(1){
		if(q.size() <= 1){ return -1; }
		LL e = q.front();
		q.pop();
		if(e == -1){
			q.push(-1);
			++ans;
			continue;
		}
		decode(e, hd, ad, hk, ak);

		if(ad >= hk){ break; }
		int nak = max(ak - d, 0);
		add(st, q, hd - ak, ad, hk - ad, ak);
		add(st, q, hd - ak, ad + b, hk, ak);
		add(st, q, hd0 - ak, ad, hk, ak);
		add(st, q, hd - nak, ad, hk, nak);
	}
	return ans;
}

string solve(){
	LL res = solve1();
	if(res < 0){ return "IMPOSSIBLE"; }
	string s;
	convert(res, s);
	return s;
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
