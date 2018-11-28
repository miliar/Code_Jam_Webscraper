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

int N, P;
int G[111];

void read() {
	cin>>N>>P;
	rep(i,N) cin>>G[i];
}

int f2[5][111];//[111];
int f3[5][111][111];//[111];
int f4[5][111][111][111];
int g[1111];

int go2(int left, int f0, int f1) {
	if(f0+f1<=0) return 0;

	int&res = f2[left][f1];//[f1];

	if(res>=0) return res;
	else res = 0;

	int ans0 = f0 > 0 ? go2( g[left+0], f0 - 1, f1 ) : 0;
	int ans1 = f1 > 0 ? go2( g[left+1], f0, f1 - 1 ) : 0;

	res = max(res, ans0);
	res = max(res, ans1);

	if(left==0) res++;

	return res;
}

int go3(int left, int f0, int f1, int f2) {
	if(f0+f1+f2<=0) return 0;

	int&res = f3[left][f1][f2];//[f2];

	if(res>=0) return res;
	else res = 0;

	int ans0 = f0 > 0 ? go3( g[left+0], f0 - 1, f1, f2 ) : 0;
	int ans1 = f1 > 0 ? go3( g[left+1], f0, f1 - 1, f2 ) : 0;
	int ans2 = f2 > 0 ? go3( g[left+2], f0, f1, f2 - 1 ) : 0;

	res = max(res, ans0);
	res = max(res, ans1);
	res = max(res, ans2);

	if(left==0) res++;

	return res;
}

int go4(int left, int f0, int f1, int f2, int f3) {
	if(f0+f1+f2+f3<=0) return 0;

	int&res = f4[left][f1][f2][f3];

	if(res>=0) return res;
	else res = 0;

	int ans0 = f0 > 0 ? go4( g[left+0], f0 - 1, f1, f2, f3 ) : 0;
	int ans1 = f1 > 0 ? go4( g[left+1], f0, f1 - 1, f2, f3 ) : 0;
	int ans2 = f2 > 0 ? go4( g[left+2], f0, f1, f2 - 1, f3 ) : 0;
	int ans3 = f3 > 0 ? go4( g[left+3], f0, f1, f2, f3 - 1 ) : 0;

	res = max(res, ans0);
	res = max(res, ans1);
	res = max(res, ans2);
	res = max(res, ans3);

	if(left==0) res++;

	return res;
}

void process() {
	int b[5]={0};

	rep(i,1111) g[i] = i % P;

	rep(i,N) b[g[G[i]]]++;

	int ans=0;

	//cout<<"\n";
	//pv(b,b+5); //cout<<"\n";

	if(P==2) {
		memset(f2,-1,sizeof f2);
		ans += b[0]; b[0]=0;
		ans += go2(0, b[0], b[1]);
	} else if(P==3) {
		memset(f3,-1,sizeof f3);
		ans += b[0]; b[0]=0;
		ans += go3(0, b[0], b[1], b[2]);
	} else if (P==4) {
		memset(f4,-1,sizeof f4);
		ans += b[0]; b[0]=0;
		ans += go4(0, b[0], b[1], b[2], b[3]);
	} else {
		assert(false);
	}

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
		P=4;
		N=100;
		rep(i,N) G[i] = rand()%100 + 1;
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
