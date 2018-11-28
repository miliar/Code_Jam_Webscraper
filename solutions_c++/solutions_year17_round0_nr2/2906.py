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

long long N;

void read() {
	cin>>N;
}

char dig[111];

long long func(int at, long long p10, char last) {
	if(!dig[at]) return 0;

	//dbg(at _ p10 _ last);

	if (last > dig[at]) return -1; // bad!

	if (last <= dig[at]) { // just go?
		long long f = func(at + 1, p10 / 10, dig[at]);
		if (f >= 0) return (dig[at]-'0') * p10 + f;
	}

	// decrease and fill with 9's ?
	if (last < dig[at]) {
		return (dig[at]-'1') * p10 + p10 - 1;
	} else {
		// impossible
		return -1;
	}
}

void process() {
	stringstream ss; ss << N; ss >> dig;
	
	long long p10 = 1;
	for(int i=1; dig[i]; i++) p10 *= 10;

	//dbg(p10);

	cout<< func(0, p10, '0') << endl;
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
		N = rand();
		//N *= rand();
		dbg(N);
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
