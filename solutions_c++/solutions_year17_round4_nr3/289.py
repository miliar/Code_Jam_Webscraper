#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FIL(a,b) memset((a),(b),sizeof(a))
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a),end(a)
#define PB push_back
#define FI first
#define SE second
typedef long long LL;
typedef pair<int,int> PT;
typedef complex<double> PX;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<PT> VPT;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; FOR(i,0,v.size()) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T> const& p)
{ return s << '(' << p.first << ',' << p.second << ')'; }

VVI adj;
VI dfsLow, dfsNum, sccNum, sccStack;
vector<char> vis;
int cnt, numScc;

void dfs(int i) {
	if (dfsNum[i] != -1) return;
	dfsLow[i] = dfsNum[i] = cnt++;
	sccStack.push_back(i);
	vis[i] = true;
	for (int j : adj[i]) {
		dfs(j);
		if (vis[j])
			dfsLow[i] = min(dfsLow[i], dfsLow[j]);
	}
	if (dfsLow[i] == dfsNum[i]) {
		int j;
		do {
			j = sccStack.back();
			sccStack.pop_back();
			vis[j] = false;
			sccNum[j] = numScc;
		} while (i != j);
		numScc++;
	}
}

void scc() {
	int N = adj.size();
	cnt = numScc = 0;
	dfsLow.resize(N); // init not necessary
	dfsNum.assign(N, -1);
	sccNum.resize(N); // init not necessary
	vis.assign(N, false);
	for (int n = 0; n < N; n++) dfs(n);
}

vector<char> truthValues;

int VAR(int i) {return 2*i;}
int NOT(int i) {return i^1;}
int NVAR(int i) {return NOT(VAR(i));}

void addCond(int c1, int c2) {
	adj[NOT(c1)].push_back(c2);
	adj[NOT(c2)].push_back(c1);
}
void init2SAT(int numVars) {
	adj.assign(2*numVars, VI());
	truthValues.resize(numVars); // init not necessary
}
bool run2SAT() {
	scc();
	for (int i = 0; i < adj.size(); i += 2) {
		if (sccNum[i] == sccNum[i+1]) return false;
		// If SCC is computed with Kosaraju's, use > instead
		truthValues[i/2] = sccNum[i] < sccNum[i+1];
	}
	return true;
}

// True is horiz
const int DR[]={0,0,-1,1}, DC[]={-1,1,0,0};

int TC, R, C;
char gd[55][55];

int main() {
	scanf("%d", &TC);
	FOR(tc,1,TC+1) {
		scanf("%d%d", &R, &C);
		FOR(r,0,R) scanf("%s", gd[r]);
		init2SAT(R*C);
		FOR(r,0,R) FOR(c,0,C) {
			bool gotd[4] = {};
			int gotr[4], gotc[4];
			FOR(i,0,4) {
				int r2 = r, c2 = c;
				for (;;) {
					r2 += DR[i]; c2 += DC[i];
					if (r2 < 0 || r2 >= R || c2 < 0 || c2 >= C) break;
					if (gd[r2][c2] == '#') break;
					if (gd[r2][c2] == '|' || gd[r2][c2] == '-') {
						gotd[i]=true; gotr[i]=r2; gotc[i]=c2;
					}
				}
			}
			if (gd[r][c] == '|' || gd[r][c] == '-') {
				if (gotd[0] || gotd[1]) addCond(NVAR(r*C+c), NVAR(r*C+c));
				if (gotd[2] || gotd[3]) addCond(VAR(r*C+c), VAR(r*C+c));
			} else if (gd[r][c] == '.') {
				bool h1 = false;
				FOR(i,0,4) FOR(j,i+1,4) if (gotd[i] && gotd[j]) {
					int v1 = i < 2 ? VAR(gotr[i]*C+gotc[i]) : NVAR(gotr[i]*C+gotc[i]);
					int v2 = j < 2 ? VAR(gotr[j]*C+gotc[j]) : NVAR(gotr[j]*C+gotc[j]);
					addCond(v1, v2);
					h1 = true;
				}
				if (!h1) {
					FOR(i,0,4) if (gotd[i]) {
						int v1 = i < 2 ? VAR(gotr[i]*C+gotc[i]) : NVAR(gotr[i]*C+gotc[i]);
						addCond(v1, v1);
						h1 = true;
					}
				}
				if (!h1) {
					addCond(VAR(0), VAR(0));
					addCond(NVAR(0), NVAR(0));
				}
			}
		}
		printf("Case #%d: ", tc);
		if (run2SAT()) {
			printf("POSSIBLE\n");
			FOR(r,0,R) {
				FOR(c,0,C) {
					char x = gd[r][c];
					if (x == '|' || x == '-') x = truthValues[r*C+c] ? '-' : '|';
					putchar(x);
				}
				putchar('\n');
			}
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
}
