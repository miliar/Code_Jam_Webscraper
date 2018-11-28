#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
#ifdef LOCAL
    #define D(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
    #define D(...) ;
    #define cerr if(0)cout
#endif
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=','){cerr<<*sdbg++;}cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

void read_data() {
}

struct MC{
	vector<int> G[311];
	map<int,int> P,S;

	int N;
	void init(int n) {
		N = n;
		FOR(i,1,N*2) G[i].clear();
		P.clear();
		FOR(i,1,N*2) P[i] = -123456;
		S.clear();
	}
	void addEdge(int a, int b) {
		G[a].PB(b);
	}

	int D[311];
	bool bfs() {
		FOR(i,0,N*2) D[i] = -1;
		queue<int> Q;
		FOR(i,1,N*2) if(P[i] == -123456) {
			Q.push(i);
			D[i] = 0;
		}
		while(!Q.empty()){
			int q = Q.front(); Q.pop();
			for(int gg : G[q]) if(D[S[gg]] == -1) {
				int g = S[gg];
				D[g] = D[q]+1;	
				Q.push(g);
			}
		}
		return D[0] != -1;
	}

	int O[311];
	bool dfs(int a) {
		O[a] = 1;
		for(int gg : G[a]) {
			if(S[gg] == 0) {
				P[a] = gg;
				S[gg] = a;
				return true;
			}
			int g = S[gg];
			if(!O[g] and dfs(g)) {
				P[a] = gg;
				S[gg] = a;
				return true;
			}
		}
		return false;
	}

	vector<pair<int,int>> MCG() {
		while(true) {
			if(!bfs()) break;
			FOR(i,1,N*2) O[i] = 0;
			FOR(i,1,N*2) if(P[i] == -123456) {
				dfs(i);
			}
		}
		vector<pair<int,int>> R;
		for(auto p : P ){
			if(p.Y != -123456) {
				int sm, df;
				tie(sm, df) = p;
				int x = (sm+df)/2;
				int y = sm-x;
				R.PB(MP(x,y));
			}
		}
		return R;
	}


}G;

int T;
void solve() {
	set<int> Wu,Ws,Wa,Wd;
	int n;
	scanf("%d", &n);
	FOR(i,1,n) {
		Wu.insert(i);
		Ws.insert(i);
		FOR(j,1,n) {
			Wa.insert(i+j);
			Wd.insert(i-j);
		}
	}
	G.init(n);
	int e;
	scanf("%d", &e);
	map<pair<int,int>, int> M;
	int ans = 0;
	FOR(i,1,e) {
		char p;
		int x;
		int y;
		scanf(" %c %d %d", &p, &x, &y);
		if(p != '+') {
			Wu.erase(x);
			Ws.erase(y);
			M[MP(x,y)] += 1;
			ans++;
		}
		if(p != 'x') {
			Wa.erase(x+y);
			Wd.erase(x-y);
			M[MP(x,y)] += 2;
			ans++;
		}
	}
	set<pair<int,int>> S;
	while(!Wu.empty() and !Ws.empty()) {
		int x = *Wu.begin(); Wu.erase(x);
		int y = *Ws.begin(); Ws.erase(y);
		S.insert(MP(x,y));
		M[MP(x,y)] += 1;
		ans++;
	}
	FOR(x,1,n) FOR(y,1,n){
		if(Wa.find(x+y) != Wa.end() and Wd.find(x-y) != Wd.end()) {
			G.addEdge(x+y, x-y);	
		}
	}
	for(auto ed : G.MCG()) {
		S.insert(ed);
		M[ed] += 2;
		ans++;
	}
	printf("Case #%d: %d %d\n", ++T, ans, SIZE(S));

	vector<char> R = {'_', 'x', '+', 'o'};
	for(auto s : S){
		printf("%c %d %d\n", R[M[s]], s.X, s.Y);
	}



}

int main() {
	int t;
	scanf("%d", &t);
	while(t--)
    solve();
}
