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

int N, K;
pair<ll,ll> p[1111];

void read() {
	cin>>N>>K;
	// Ri , Hi
	for(int i=0;i<N;i++){
		cin>> p[i].x >> p[i].y;
	}
}

bool comp(pair<ll,ll> a, pair<ll,ll> b) {
	if (a.x != b.x) return a.x > b.x;
	else return a.x * a.y > b.x * b.y;
}

bool sy(pair<ll,ll> a, pair<ll,ll> b) {
	return a.x * a.y > b.x * b.y;
}

void process() {
	sort(p,p+N, comp);
	double ans = 0;
	for(int i=N-K;i>=0;i--) {
		double nans = (M_PI * pow(p[i].x, 2.0));
		sort(p+i+1, p+N, sy);
		//dbg(i);
		for(int j=0;j<K;j++) {
			//dbg(p[i+j].x _ p[i+j].y);
			nans += (2.0 * M_PI * p[i+j].x) * p[i+j].y;
		}
		if(nans > ans) ans = nans;
	}
	printf("%.6lf\n",ans);
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
