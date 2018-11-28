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
// int U;
// int P[55];

// char tmp[111];

// int readInt() {
// 	cin >> tmp;
// 	int a = 0, b = 0, i = 0;
// 	while (tmp[i]) {
// 		if (tmp[i] == '.') break;
// 		a = a * 10 + (tmp[i] - '0');
// 		i++;
// 	}
// 	i++;
// 	for(int j=0;j<4;j++) {
// 		if(tmp[i]) {
// 			b = b * 10 + (tmp[i] - '0');
// 			++i;
// 		} else {
// 			b = b * 10;
// 		}
// 	}
// 	return a*10000 + b;
// }
double u;
double p[55];

void read() {
	cin>>N>>K;
	// U = readInt();
	// for(int i=0;i<N;i++) {
	// 	P[i] = readInt();
	// }
	cin>>u;
	for(int i=0;i<N;i++) cin>>p[i];
}


void process() {

	int n = N;
	// dbg(U);
	// for(int i=0;i<N;i++) {
	// 	dbg(i _ P[i]);
	// }

	sort(p,p+n);

	double at=0, add=1.0;
	for(int r=0;r<1111;r++) {
		double nat = at + add;
		double need=0;
		for(int i=0;i<n;i++) {
			need += max(nat - p[i],0.0);
		}
		if(need<=u) {
			at=nat;
		} else {
			add /= 2;
		}
	}

	double ans=1.0;
	for(int i=0;i<n;i++) {
		double need = max(at - p[i],0.0);
		ans *= (p[i] + need);
	}

	printf("%.6lf\n", ans);
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
