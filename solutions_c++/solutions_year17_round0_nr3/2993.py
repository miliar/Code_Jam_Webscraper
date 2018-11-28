#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>
#define _ << " _ " <<
#define dbg(x) cerr << #x << " == " << x << endl
#define mp(x,y) make_pair((x),(y))
#define pv(x,y) {for(typeof(y) z=(x);z!=(y);z++)cerr<<*z<<" ";cerr<<endl;}
#define rep(x,y) for(int(x)=(0);(x)<int(y);++(x))
#define x first
#define y second
using namespace std;

typedef long long ll;
typedef pair<int,int> pt;

#if 0
#define GENERATE 1
#endif

ll N, K;

void read() {
	cin>>N>>K;

	//dbg("?");
}


ll go(ll L, ll f, ll g, ll x) {

	//dbg(L _ f _ g _ x);

	if (f >= x) {
		return L;
	}
	if (f + g >= x) {
		return L-1;
	}

	if (L&1) {
		ll nL = L/2;
		ll nf = f * 2 + g;
		ll ng = g;
		ll nx = x - f - g;
		return go(nL, nf, ng, nx);
	} else {
		ll nL = L/2;
		ll nf = f;
		ll ng = 2 * g + f;
		ll nx = x - f - g;
		return go(nL, nf, ng, nx);
	}
}

pair<ll,ll> func(ll L, ll x) {
	ll e = go(L, 1, 0, x);
	if(e&1) return mp(e/2,e/2);
	else return mp(e/2, e/2-1);
}

void process() {

	//dbg(N _ K);

	pair<ll,ll> p = func(N, K);

	//dbg(p.x _ p.y);

	cout << p.x << " " << p.y << endl;
}

int main() {
	int T;
#ifdef GENERATE
	unsigned int seed=time(0);
	dbg(seed);
	srand(seed);
	T=50;
	for(int testcase=1;testcase<=T;++testcase) {
		fprintf(stderr,"Case #%d: ",testcase);
		// *generate input!
		// BEGIN
		// END
#else
		cin>>T;
		for(int testcase=1;testcase<=T;++testcase) {
			fprintf(stdout,"Case #%d: ",testcase);
			read();
#endif
		try {
			process();
		} catch(char const*exception) {
			puts(exception);
		}
	}
	return 0;
}
