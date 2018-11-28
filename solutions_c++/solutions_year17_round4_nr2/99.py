// ayy
// ' lamo
#include <bits/stdc++.h>
#include <bits/extc++.h>
using namespace std;
using namespace __gnu_pbds;
typedef long long ll;
typedef long double ld; //CARE
typedef complex<ld> pt;
#define fi first
#define se second
#define pb push_back
const ld eps=1e-8;
const int inf=1e9+99;
const ll linf=1e18+99;
const int P=1e9+7;




int good(const vector<int> &tix,int A) {
	int lvl=0,ex=0,on=0;
	int Z=0;
	for(int x:tix) {
		for(;lvl<x;) ++lvl, ex+=on, on=A;
		assert(lvl==x);
		if(on) { --on; continue; }
		if(ex) { --ex; ++Z; continue; }
		return -1;
	}
	return Z;
}


void _m(int t) {
	int n,c,m; scanf("%d%d%d",&n,&c,&m);
	vector<int> tix;
	vector<int> cc(1024,0);
	for(int i=0;i<m;i++) {
		int p,b; scanf("%d%d",&p,&b);
		tix.pb(p);
		cc[b]++;
	}
	sort(tix.begin(),tix.end());
	int L=0,R=1024;
	for(int x:cc) L=max(L,x);
	for(;L!=R;) {
		int M=(L+R)/2;
		if(~good(tix,M)) R=M;
		else L=M+1;
	}

	int Y=L;
	int Z=good(tix,Y);
	printf("Case #%d: %d %d\n",t,Y,Z);
}



int32_t main() {
	int T; scanf("%d",&T); for(int t=1;t<=T;t++) _m(t);
}










