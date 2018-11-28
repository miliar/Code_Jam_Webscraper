#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

const int oo = 0x3f3f3f3f;

#define C 59
#define N 2*C*C
#define E N*N

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int r1[] = {3, 2, 1, 0};
int r2[] = {1, 0, 3, 2};

int r, c;
char grid[C][C];
int id[C][C];

int m;
vi adj2[N];

int n, rx[N], ry[N];

bool fora(int x, int y) {
	return x < 0 || x >= r ||
			y < 0 || y >= c;
}

int cur;
bool link;
bool go(int x, int y, int d) {
	//db(x _ y _ d);
	if (fora(x, y) || grid[x][y] == '#') return 1;
	if (grid[x][y] == '-' || grid[x][y] == '|') return 0;
	
	if (grid[x][y] == '.') {
		bool r = go(x+dx[d], y + dy[d], d);
		if (r && link) adj2[id[x][y]].pb(cur);
		return r;
	}
	
	if (grid[x][y] == '\\') d = r1[d];
	else d = r2[d];
	return go(x+dx[d], y + dy[d], d);
}

bool go(int i, int d) {
	//db(d);
	return go(rx[i] + dx[d], ry[i] + dy[d], d);
}



int adj[N], to[E], ant[E], z;

int st[N], idx[N], low[N], ind, stp = 0, nn, ncomp = 0, comp[N];
int dfs(int x) {
  if (~idx[x]) return idx[x] ? idx[x] : ind;
  low[x] = idx[x] = ind++;
  st[stp++] = x;
  for (int w = adj[x] ; ~w ; w = ant[w])
    low[x] = min(low[x], dfs(to[w]));
  if (idx[x] == low[x]) {
    ++ncomp;
    while (idx[st[--stp]] = 0, st[stp] != x) {
      low[st[stp]] = low[x], comp[st[stp]] = ncomp; }
      comp[x] = ncomp; }
  return low[x];
}
bool tarjan() {
  fr(i,0,nn) dfs(i);
  // no final, low[v] indica qual o componente de v
  fr(i,0,nn) if (low[i] == low[i^1]) return 0;
  return 1;
}


void add(int a, int b) {
	to[z] = b; ant[z] = adj[a]; adj[a] = z++;
}
// Operações comuns de 2-sat
// traduz de forma que se possa escrever "não v" como "~v"
#define trad(v) (v<0?((~v)*2)^1:v*2)
void addImp(int a, int b){ add(trad(a), trad(b)); }
void addOr(int a,int b) {
	//db(a _ b);
	addImp(~a,b); addImp(~b,a);
}
void addEqual(int a, int b) { addOr(a,~b); addOr(~a,b); }
void addDiff(int a, int b) { addEqual(a,~b); }
// valoração: value[i] = (comp[i] < comp[i + 1]) ? 0 : 1;


bool val[N];

bool proc() {
	memset(adj,-1,sizeof adj); z = 0;
	memset(idx,-1,sizeof idx); ind = 1;
	
	rp(i, n) {
		int q = 0;
		
		cur = i; link = 0;
		bool ver = go(i, 0) && go(i, 2);
		if (ver) {
			link = 1;
			go(i, 0); go(i, 2);
			q++;
		} else addOr(~i, ~i);
		
		cur = ~i; link = 0;
		bool hor = go(i, 1) && go(i, 3);
		if (hor) {
			link = 1;
			go(i, 1); go(i, 3);
			q++;
		} else addOr(i, i);
		
		if (q == 0) return 0;
	}
	
	rp(i, m) {
		int sz = adj2[i].size();
		assert(sz <= 2);
		if (sz == 0) return 0;
		else if (sz == 1) {
			int u = adj2[i][0];
			addOr(u, u);
		} else {
			int u = adj2[i][0];
			int v = adj2[i][1];
			addOr(u, v);
		}
	}
	
	nn = n+n;
	if (!tarjan()) return 0;
	rp(i, n) val[i] = (comp[i+i] < comp[i+i+1])? 1: 0;
	return 1;
}

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		sc2(r, c);
		n = m = 0;
		rp(i, r) {
			scs(grid[i]);
			rp(j, c) if (grid[i][j] == '.') {
				adj2[m].clear();
				id[i][j] = m++;
			} else if (grid[i][j] == '-' || grid[i][j] == '|') {
				rx[n] = i; ry[n] = j;
				id[i][j] = n++;
			}
		}
		
		bool ans = proc();
		printf("Case #%d: %s\n", cn++, ans? "POSSIBLE": "IMPOSSIBLE");
		if (ans) {
			rp(i, r) {
				rp(j, c) if (grid[i][j] == '-' || grid[i][j] == '|') {
					int u = id[i][j];
					putchar(val[u]? '|': '-');
				} else putchar(grid[i][j]);
				puts("");
			}
		}
	}
	return 0;
}




































