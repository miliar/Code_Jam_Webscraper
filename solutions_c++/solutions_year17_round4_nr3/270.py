#include <bits/stdc++.h>

#define x first
#define y second
#define X first
#define Y second

#ifdef ONLINE_JUDGE
#define DEBUG(x)
#else
#define DEBUG(x) cerr << #x << ": " << x << endl;
#endif

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const int mod=1000000000+7;

int addm(int& a,int b) {return (a+=b)<mod?a:a-=mod;}

template<class T,class U> bool smin(T& a,U b) {return a>b?(a=b,1):0;}
template<class T,class U> bool smax(T& a,U b) {return a<b?(a=b,1):0;}

// ====================== SCC ===========================
class SCC {
private:
    int n, comp;
    vvi g, gt;
    vi seq, vis;
    void dfs(int u, const vvi &adj){
	for (int v : adj[u]){
            if (vis[v] == -1){
                vis[v] = comp;
                dfs(v, adj);
            }
        }
        seq.push_back(u);
    }
public:
    SCC() {}
    SCC(int _n){
        n = _n;
        g.assign(n, vi()); gt.assign(n, vi());
    }
    void add_edge(int u, int v){
        g[u].push_back(v); gt[v].push_back(u);
    }
    pair<int, vi> find_SCC(){
        vis.assign(n, -1); comp = 0;
        for (int i = 0; i < n; i++){
            if (vis[i] == -1){
                vis[i] = comp;
                dfs(i, g);
            }
        }
        vis.assign(n, -1); comp = 0;
        for (int i = n-1; i >= 0; i--){
            int u = seq[i];
            if (vis[u] == -1){
                vis[u] = comp;
                dfs(u, gt);
                comp++;
            }
        }
        return {comp, vis};
    }
};
// ====================== SCC ===========================

//listings:twosat
// 2-SAT solver. Include SCC code from graph algorithms. VAR(x) is variable x,
// NOT(VAR(x)) is the negation of variable x. Complexity: O(n + m)
int VAR(int x) { return 2*x; }
int NOT(int x) { return x^1; }

struct TwoSAT {
	int n;  SCC scc;
	// Create a 2-SAT equation with n variables
	TwoSAT(int n) : n(n), scc(2 * n) { }
	void add_or(int u, int v) {
		if (u == NOT(v)) return;
		scc.add_edge(NOT(u), v);  scc.add_edge(NOT(v), u);
	}
	void add_true(int u){ add_or(u, u); }
	void add_false(int u) { add_or(NOT(u), NOT(u)); }
	void add_xor(int u, int v) { add_or(u, v); add_or(NOT(u), NOT(v)); }
	pair<bool, vector<bool>> solve() {
		vi comp = scc.find_SCC().Y;  vector<bool> val(n);
		for (int i = 0; i < 2 * n; i += 2){
			if (comp[i] == comp[i + 1]) return {false, val};
			val[i/2] = (comp[i] > comp[i + 1]);
		}
		return {true, val};
	}
};

int T,R,C,ct;
int id[50][50];
pii pos[2500];
string bd[50];
int vert[50][50],vdir[50][50],horiz[50][50],hdir[50][50];
int io[]{0,0,-1,1};
int jo[]{-1,1,0,0};
int f[]{3,2,1,0};
int b[]{2,3,0,1};
int odir;

bool dfs(int i,int j,int dir,int cid) {
	if (i<0 || i>=R || j<0 || j>=C) return 0;
	if (bd[i][j]=='-' || bd[i][j]=='|') return 1;
	if (bd[i][j]=='/') {
		dir=f[dir];
		return dfs(i+io[dir],j+jo[dir],dir,cid);
	}
	if (bd[i][j]=='\\') {//help
		dir=b[dir];
		return dfs(i+io[dir],j+jo[dir],dir,cid);
	}
	if (bd[i][j]=='#') return 0;
	
	if (dir<2) {//horiz
		horiz[i][j]=cid;
		hdir[i][j]=odir;
	}
	else {
		vert[i][j]=cid;
		vdir[i][j]=odir;
	}

	return dfs(i+io[dir],j+jo[dir],dir,cid);
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> R >> C;
		ct=0;
		for (int i=0;i<R;i++) {
			cin >> bd[i];
			for (int j=0;j<C;j++) if (bd[i][j]=='|' || bd[i][j]=='-') {
				id[i][j]=ct;
				pos[ct++]={i,j};
			}
			for (int j=0;j<C;j++) horiz[i][j]=vert[i][j]=-1;
		}

		TwoSAT cc(ct);

		for (int i=0;i<R;i++) for (int j=0;j<C;j++) if (bd[i][j]=='|' || bd[i][j]=='-') {
			for (int dir=0;dir<4;dir++) if (odir=dir,dfs(i+io[dir],j+jo[dir],dir,id[i][j])) {
				cc.add_false(VAR(id[i][j])^(dir/2));
			}
		}

		bool succ=1;
		for (int i=0;i<R;i++) for (int j=0;j<C;j++) if (bd[i][j]=='.') {
			if (horiz[i][j]==-1 && vert[i][j]==-1) succ=0;
			else if (vert[i][j]==-1) cc.add_true(VAR(horiz[i][j])^(hdir[i][j]/2));
			else if (horiz[i][j]==-1) cc.add_true(VAR(vert[i][j])^(vdir[i][j]/2));
			else cc.add_or(VAR(horiz[i][j])^(hdir[i][j]/2),VAR(vert[i][j])^(vdir[i][j]/2));
		}

		cout << "Case #" << cas << ": ";
		auto res=cc.solve();
		if (!succ || !res.X) {
			cout << "IMPOSSIBLE\n";
			continue;
		}

		cout << "POSSIBLE\n";
		for (int i=0;i<ct;i++) {
			if (res.Y[i]) {
				pii aa=pos[i];
				bd[aa.X][aa.Y]='-';
			}
			else {
				pii aa=pos[i];
				bd[aa.X][aa.Y]='|';
			}
		}
		for (int i=0;i<R;i++) cout << bd[i] << '\n';
	}

}
