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

int D[101][101];
int E[101];
ldouble S[101];

int n;
vector<slong> dijkstra(int a) {
	vector<slong> O{0};
	FOR(i,1,n) O.PB(INF*n*n);
	O[a] = 0;
	priority_queue<pair<slong,slong>, vector<pair<slong,slong>>, greater<pair<slong,slong>>> Q;
	Q.push({0,a});
	while(!Q.empty()) {
		slong o,g;
		tie(o,g) = Q.top(); Q.pop();
		if(O[g] != o) continue;
		FOR(i,1,n) if(D[g][i] != -1 and o+D[g][i] < O[i]) {
			O[i] = o+D[g][i];
			Q.push({O[i],i});
		}
	}
	return O;
}

ldouble GO[101][101];
vector<slong> SO[101];

void go(int a) {
	GO[a][a] = 0;
	priority_queue<pair<ldouble,int>, vector<pair<ldouble,int>>, greater<pair<ldouble,int>>> Q1;
	Q1.push({GO[a][a], a});
	while(!Q1.empty()) {
		ldouble g;
		int v;
		tie(g,v) = Q1.top(); Q1.pop();
		if(GO[a][v]-EPS > g) continue;
		if(SO[v].empty()) SO[v] = dijkstra(v);
		FOR(i,1,n) if(i != v and SO[v][i] <= E[i]) {	
			if(GO[a][i] > g + SO[v][i]*1.0/S[i]) {
				GO[a][i] = g+SO[v][i]*1.0/S[i];
				Q1.push({GO[a][i], i});
			}
		}
	}
}

int T;
void solve() {
	int q;
	scanf("%d%d", &n,&q);
	FOR(i,1,n) scanf("%d%Lf", &E[i], &S[i]);
	FOR(j,1,n) FOR(i,1,n) scanf("%d", &D[i][j]);
	FOR(i,0,n) FOR(j,0,n) FOR(k,0,n) GO[i][j] = INF*123;
	FOR(i,1,n) SO[i].clear();

	FOR(i,1,n) {
		go(i);
	}

	printf("Case #%d: ", ++T);
	FOR(i,1,q) {
		int a,b;
		scanf("%d%d",&a,&b);
		printf("%Lf ", GO[b][a]);
	}
	printf("\n");
}

int main() {
	int t;
	scanf("%d", &t);
	while(t--) solve();

}
