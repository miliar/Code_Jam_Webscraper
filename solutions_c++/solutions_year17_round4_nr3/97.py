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

const int N=5050;
vector<int> S,B,xx[N+N],*e=xx+N;
bool ass[N];
int xI[N+N],*I=xI+N,C;
bool scc(int v) {
	S.pb(v);
	B.pb(I[v] = (int)S.size());
	for(int w:e[v]) {
		if(I[w]) while (I[w]<B.back()) B.pop_back();
		else if(!scc(w)) return 0;
	}
	if(I[v] == B.back()) {
		for(B.pop_back(), ++C; I[v] <= (int)S.size(); S.pop_back()) {
			int w = S.back();
			if(I[~w] == C) return 0;
			if(I[~w] < N) ass[w<0?~w:w] = w>=0;
			I[w] = C;
		}
	}
	return 1;
}
bool go(int n) {
	S.clear(), B.clear();
	for(int i=0;i<N+N;i++) xI[i]=0;
	for(int i=0;i<N;i++) ass[i]=0;
	C=N;
	for(int i=-n;i<n;i++) if(!I[i] && !scc(i)) return 0;
	return 1;
}

const int DEF=3842934;
int r,c;
char grid[64][64];
void die() {
	printf("IMPOSSIBLE\n");
}
void add_edge(int x,int y) { e[x].pb(y); }
void OR(int a,int b) { add_edge(~a,b); add_edge(~b,a); }
int enc(int x,int y) {
	return x*(c+1)+y;
}
const int dx[]={1,0,-1,0};
const int dy[]={0,1,0,-1,0};
int gun(int x,int y,int k) {
	for(;;) {
		// cerr<<"trace: "<<x<<","<<y<<" "<<k<<endl;
		x+=dx[k];
		y+=dy[k];
		char Q=grid[x][y];
		if(Q=='#') return DEF;
		if(Q=='/') k^=3;
		if(Q=='\\') k^=1;
		if(Q=='-') {
			if(k&1) return enc(x,y);
			else return ~enc(x,y);
		}
		if(Q=='|') {
			if(k&1) return ~enc(x,y);
			else return enc(x,y);
		}
	}
}
void _m(int t) {
	printf("Case #%d: ",t);
	for(int i=0;i<N+N;i++) xx[i].clear();
	scanf("%d%d",&r,&c);
	for(int i=0;i<=r+1;i++) for(int j=0;j<=c+1;j++) grid[i][j]='#';
	for(int i=1;i<=r;i++) scanf("%s",grid[i]+1);
	for(int i=1;i<=r;i++) grid[i][c+1]='#', grid[i][c+2]=0;
	for(int i=1;i<=r;i++) for(int j=1;j<=c;j++) {
		char Q=grid[i][j];
		int A=gun(i,j,0);
		int B=gun(i,j,1);
		int C=gun(i,j,2);
		int D=gun(i,j,3);
		if(Q=='-' || Q=='|') {
			int y=enc(i,j);
			if(Q=='|') swap(A,B), swap(C,D);
			if(A!=DEF || C!=DEF) add_edge(~y,y);
			if(B!=DEF || D!=DEF) add_edge(y,~y);
		}
		if(Q=='.') {
			if(A!=DEF && C!=DEF) OR(~A,~C);
			if(B!=DEF && D!=DEF) OR(~B,~D);
			if(A==DEF) A=C;
			if(B==DEF) B=D;
			if(A==DEF && B==DEF) return die();
			if(A==DEF) swap(A,B);
			if(B==DEF) add_edge(~A,A);
			else OR(A,B);
		}
	}
	if(!go((r+1)*(c+1))) return die();
	for(int i=1;i<=r;i++) for(int j=1;j<=c;j++) {
		char Q=grid[i][j];
		if(Q!='-' && Q!='|') continue;
		if(!ass[enc(i,j)]) Q^='-', Q^='|', grid[i][j]=Q;
	}
	for(int i=1;i<=r;i++) grid[i][c+1]=0;
	printf("POSSIBLE\n");
	for(int i=1;i<=r;i++) printf("%s\n",grid[i]+1);
}





int32_t main() {
	int T; scanf("%d",&T); for(int t=1;t<=T;t++) _m(t);
}










