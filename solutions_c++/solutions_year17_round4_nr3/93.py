#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

#define N 100007
int n,       // input
ind[N],    // temp
lowlink[N],  // temp
onstack[N],  // temp
last,        // temp
n2,          // output
t[N];        // output
vi adj[N],   // input
st;          // temp

void go (int v) {
   ind[v] = lowlink[v] = ++last;
   st.pb(v);
   onstack[v] = 1;
   FOREACH(w,adj[v]) {
      if (!ind[*w]) {
         go(*w);
         lowlink[v] = min(lowlink[v], lowlink[*w]);
      } else if (onstack[*w]) {
         lowlink[v] = min(lowlink[v], lowlink[*w]);
      }
   }
   if (lowlink[v] == ind[v]) { // v is a root node
      ++n2;
      for (int w = -1; w != v; ) {
         w = st.back();
         st.pop_back();
         onstack[w] = 0;
         t[w] = n2;
      }
   }
}

void scc() {
   last = n2 = 0;
   FORI(i,n) ind[i] = onstack[i] = 0;
   FORI(i,n) if (!ind[i]) go(i);
   FORI(i,n) t[i] = n2 + 1 - t[i]; // zeby byl zwykly porzadek topologiczny
}

int k,               // input
val[N];              // output
vector<pii> clauses; // input
vi adjtr[N];

void dwasat_dfs(int v, bool wart, vi *adja) {
   if (val[v] != -1) return;
   val[v] = wart;
   FOREACH(it,adja[v]) dwasat_dfs(*it,wart,adja);
}
bool dwasat() {
   // konstrukcja grafu
   n = 2*k;
   FORI(i,n) adj[i].clear(), adjtr[i].clear();
   FOR(i,SZ(clauses)) {
      int a = clauses[i].fi, b = clauses[i].se;
      if (a < 0) a = n+1+a; // negacja
      if (b < 0) b = n+1+b;
      adj[n+1-a].pb(b);
      adj[n+1-b].pb(a);
      adjtr[b].pb(n+1-a);
      adjtr[a].pb(n+1-b);
   }
   // silnie spojne skladowe (+ sort. top.)
   scc();
   // spr czy formula jest spelnialna
   FORI(i,k) if (t[i] == t[n+1-i]) return 0;
   // konstrukcja wartosciowania
   FORI(i,n) val[i] = -1;
   FORI(i,k) if (val[i] == -1) {
      int v = (t[i] > t[n+1-i]) ? i : n+1-i;
      // z v do ~v nie ma sciezki
      dwasat_dfs(v,1,adj);
      dwasat_dfs(n+1-v,0,adjtr);
   }
   return 1;
}

int r,c;
char s[55][55];
int vis[55][55][5], dp[55][55][4];
map<pii,int> num;

int dx[4] = {0,1,0,-1}, dy[4] = {1,0,-1,0};

int shoot(int x, int y, int q) {
	if (vis[x][y][q]) return dp[x][y][q];
	vis[x][y][q] = 1;
	dp[x][y][q] = 0;
	if (s[x][y] == '|' || s[x][y] == '-') dp[x][y][q] = 1;
	int qq = q;
	if (s[x][y] == '/') {
		qq = 3-qq;
	}
	if (s[x][y] == '\\') {
		qq = 1^qq;
	}
	int xx = x+dx[qq], yy=y+dy[qq];
	if (xx<0 || yy<0 || xx>=r || yy>=c) return 0;
	if (s[xx][yy] == '#') return 0;
	if (s[xx][yy] == '|' || s[xx][yy] == '-') {
		if (q&1) dp[x][y][q] = num[mp(xx,yy)];
		else dp[x][y][q] = -num[mp(xx,yy)];
	} else dp[x][y][q] = shoot(xx, yy, qq);
	//printf("shoot %d %d %d = %d\n", x, y, q, dp[x][y][q]);
	return dp[x][y][q];
}

void test() {
	scanf("%d%d", &r, &c);
	FOR(i,r) FOR(j,c) FOR(q,4) vis[i][j][q] = 0;
	FOR(i,r) scanf("%s", s[i]);
	k = 0;
	clauses.clear();
	num.clear();
	FOR(i,r) FOR(j,c) {
		if (s[i][j] == '|' || s[i][j] == '-') num[mp(i,j)] = ++k;
	}
	k++;
	FOR(i,r) FOR(j,c) if (s[i][j] == '|' || s[i][j] == '-') {
		int ok=0;
		FOR(q,2) {
			int w1 = shoot(i,j,q);
			int w2 = shoot(i,j,q+2);
			if (w1==0 && w2==0) ok |= 1<<q;
		}
		//printf("ok %d %d = %d\n", i, j, ok);
		if (ok==0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		if (ok == 3) continue;
		if (ok == 1) {
			clauses.pb(mp(-num[mp(i,j)], -k));
		} else {
			clauses.pb(mp(num[mp(i,j)], -k));
		}
	}
	FOR(i,r) FOR(j,c) FOR(q,4) vis[i][j][q] = 0;
	FOR(i,r) FOR(j,c) if (s[i][j] == '.') {
		int who[4];
		FOR(q,4) {
			who[q] = shoot(i,j,q);
		}
		pii need(-1, -1);
		FOR(q,2) {
			if (who[q]!=0 && who[2+q]!=0) {
				printf("IMPOSSIBLE\n");
				return;
			}
			int ww = who[q]+who[q+2];
			if (q==0) need.fi = ww;
			else need.se = ww;
		}
		if (need.fi==0) need.fi = -k;
		if (need.se==0) need.se = -k;
		clauses.pb(need);
	}
	clauses.pb(mp(k,k));
	if (!dwasat()) {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("POSSIBLE\n");
	FOR(i,r) FOR(j,c) if (s[i][j]=='|' || s[i][j]=='-') {
		if (val[num[mp(i,j)]]) s[i][j] = '|';
		else s[i][j] = '-';
	}
	FOR(i,r) printf("%s\n", s[i]);
		
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
