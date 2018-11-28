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

int C, J;
pair<int,int> ct[222];
pair<int,int> jt[222];

void read() {
	cin >> C >> J;
	for(int i = 0; i < C; i++) {
		cin >> ct[i].x >> ct[i].y;
	}
	for(int i = 0; i < J; i++) {
		cin >> jt[i].x >> jt[i].y;
	}
}

int f[2][2][2222][777];
int dt[2][7777];

int go(int vf, int w, int t, int tw, int another) {
	if (tw > 720 || another > 720) return 1e9;
	if (t >= 1440) return (vf == w ? 0 : 1);
	if (dt[w][t] == 1) return 1e9;


	int &r = f[vf][w][t][(w == 0 ? tw : another)];

	if(r != -1) return r;
	
	// keep w
	int keep = go(vf,w, t+1, tw+1, another);

	// change
	int change = 1 + go(vf,w^1, t+1, another+1, tw);

	r = min(keep, change);

	return r;
}

void process() {
	memset(dt,0,sizeof dt);
	for(int i=0;i<C;i++){
		for(int j=ct[i].x;j<ct[i].y;j++) {
			dt[0][j]=1;
		}
	}
	for(int i=0;i<J;i++) {
		for(int j=jt[i].x;j<jt[i].y;j++) {
			dt[1][j]=1;
		}
	}
	memset(f,-1,sizeof f);

	int ans = min( go(0,0,0,0,0), go(1,1,0,0,0) );

	printf("%d\n", ans);
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
