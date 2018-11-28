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
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;


#define yes(x) (2*(x))
#define no(x) (2*(x)+1)
struct two_sat {
    int n;
    vector<vector<int>> G;
    vector<int> v_value;
    vector<bool> v_visited;
    vector<int> order;
    bool conflict;

    two_sat(int _n) :
        n(_n),
        G(2*n),
        v_value(2*n, -1),
        v_visited(2*n, false),
        conflict(false)
        {}

    /* use macros yes&no to pass parameters */
    inline void add(int a, int b){
	 	D(a,b);
        G[a^1].PB(b);
        G[b^1].PB(a);
    }

    void dfs1(int v) {
        v_visited[v] = true;
        for(auto u: G[v^1]) if(!v_visited[u^1]) dfs1(u^1);
        order.PB(v);
    }

    void dfs2(int v) {
        v_visited[v] = true; 
        v_value[v] = (v_value[v^1] == -1);
        for(auto u: G[v]) if(!v_visited[u]) dfs2(u);
    }
    
    void run() {
        FORW(v,0,2*n) if(!v_visited[v]) dfs1(v);
        FORW(v,0,2*n) v_visited[v] = false;
        reverse(ALL(order));
        for(int v: order) if(!v_visited[v]) dfs2(v);
        FORW(v,0,2*n) if(v_value[v]) {
            for(auto u: G[v]) if(!v_value[u]) {
                conflict = true;
                return;
            }
        }
        FORW(v,0,n) v_value[v] = v_value[2*v];
    }
};

char M[55][55];
bool BS;
map<pair<int,int>, int> Var;
map<pair<int,int>, set<int>> PS;

void GO(int x, int y, int dx, int dy, int var, int pierwsza_wolna) {
	if(M[x][y] == '#') return;
	if(M[x][y] == '.') PS[MP(x,y)].insert(var);
	if((M[x][y] == '-' or M[x][y] == '|' )and (!pierwsza_wolna)) {
		D(x,y, M[x][y], var, var/2);
		BS = true;
		return;
	}
	
	if(M[x][y] == '\\') {
		swap(dx,dy);
		//dx*=-1; dy*=-1;
	}

	if(M[x][y] == '/') {
		swap(dx,dy);
		dx*=-1; dy*=-1;
	}

	GO(x+dx,y+dy,dx,dy,var,0);
}

void solve() {
	int r,c;
	cin >> r >> c;
	Var.clear();
	PS.clear();
	BS = false;
	FOR(i,0,r+1) FOR(j,0,c+1) {
		M[i][j] = '#';
		M[i][j+1] = 0;
	}
	FOR(i,1,r) FOR(j,1,c) {
		cin >> M[i][j];
		if(M[i][j] == '-' or M[i][j] == '|') Var[MP(i,j)] = SIZE(Var);
		if(M[i][j] == '.') PS[MP(i,j)] = {};
	}
	D(Var);
	two_sat S2(SIZE(Var)+2);
	D(SIZE(Var));
	D(PS);

	for(auto var : Var) {
		BS = false;
		GO(var.X.X, var.X.Y, 1, 0, yes(var.Y),1);
		GO(var.X.X, var.X.Y, -1, 0, yes(var.Y),1);
		D(BS, var);
		if(BS) S2.add(no(var.Y), no(var.Y));
		
		BS = false;
		GO(var.X.X, var.X.Y, 0, -1, no(var.Y),1);
		GO(var.X.X, var.X.Y, 0, 1, no(var.Y),1);
		D(BS, var);
		if(BS) S2.add(yes(var.Y), yes(var.Y));
	}

	D(PS);

#define NOPE {cout << "IMPOSSIBLE\n"; return;}

	for(auto ps : PS) {
		if(ps.Y.empty()) NOPE;
		if(ps.Y.size() == 1) {
			int x = *ps.Y.begin();
			S2.add(x,x);
		} if(ps.Y.size() == 2) {
			int x = *ps.Y.begin();
			int y = *ps.Y.rbegin();
			S2.add(x,y);
		}
		if(ps.Y.size() > 2) NOPE;	
	}

	S2.run();

	if(S2.conflict) NOPE;

	cout << "POSSIBLE\n";

	FOR(i,1,r) {
		FOR(j,1,c) {
			if(Var.find(MP(i,j)) == Var.end()) cout << M[i][j];
			else {
				if(S2.v_value[Var[MP(i,j)]]) cout << "|";
				else cout << "-";
			}
		}
		cout << "\n";
	}
	
	//printf("\n");FOR(i,0,r+1) printf("%s\n", M[i]);
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(i,1,T) {
		cout << "Case #" << i <<": ";
		solve();
	}
}
