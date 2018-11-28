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

char S[1111];
int K;

int inc[1111];

void read() {
	cin>>S>>K;
}

void process() {
	int ans=0,at=0;
	int n = strlen(S);
	
	for(int i=0;i<=n;i++) inc[i]=0;

	for(int i=0;i<n;i++) { 
		at += inc[i];

		int b=(S[i]=='+'?0:1) + at;

		if(b&1) {
			if(i+K<=n) {
				ans++;
				at += 1;
				inc[i+K]=-1;
			} else {
				ans=-1;
			}
		}
	}

	if(ans==-1) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main() {
	int T;
#ifdef GENERATE
	unsigned int seed=time(0);
	dbg(seed);
	srand(seed);
	T=50;
	for(int testcase=1;testcase<=T;++testcase) {
		fprintf(stderr,"Case #%d:",testcase);
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
