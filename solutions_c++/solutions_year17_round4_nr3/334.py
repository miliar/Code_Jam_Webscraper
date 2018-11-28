#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

#define MAX_V 210

int V; 
vector<int> G[MAX_V], rG[MAX_V];
vector<int> vs; 

bool vis[MAX_V];
int cmp[MAX_V]; 

void add_edge(int from, int to)
{
	//cout << from << " --- " << to << endl;
	G[from].pb(to);
	rG[to].pb(from);
}

void dfs(int v)
{
	vis[v] = true;

	for (int to : G[v]) {
		if (!vis[to]) dfs(to);
	}

	vs.push_back(v);
}

void rdfs(int v, int k)
{
	vis[v] = true;
	cmp[v] = k;

	for (int to : rG[v]) {
		if (!vis[to]) rdfs(to, k);
	}
}

int scc()
{
	memset(vis, 0, sizeof(vis));
	vs.clear();

	rep(v, V) if (!vis[v]) dfs(v);

	memset(vis, 0, sizeof(vis));

	int k = 0;
	reverse(ALL(vs));

	for (int v : vs) {
		if (!vis[v]) rdfs(v, k++);
	}

	return k;
}

int TC;
int R, C;
char c[60][60];
int id[60][60];

bool us[60][60][4];
vi hl[60][60];

vi cand;
int cur;

bool go(int y, int x, int dir, bool em) {
	if (!(y >= 0 && y < R && x >= 0 && x < C) || c[y][x] == '#') {
		return true;
	}

	if (us[y][x][dir]) return true;
	us[y][x][dir] = 1;

	if (em && c[y][x] == '.') {
		hl[y][x].pb(cur);
	}

	if (c[y][x] == '|' || c[y][x] == '-') {
		return false;
	}

	if (c[y][x] == '/') {
		dir = 3 - dir;
	} else if (c[y][x] == '/') {
		dir ^= 1;
	}

	y += dy[dir];
	x += dx[dir];
	return go(y, x, dir, em);
}

void solve(int tc) {
	printf("Case #%d: ", tc + 1);
	scanf("%d%d", &R, &C);

	rep(i, R) {
		rep(j, C) {
			hl[i][j].clear();
		}
	}

	int now = 0;

	rep(i, R) {
		scanf("%s", c[i]);
		rep(j, C) {
			if (c[i][j] == '|' || c[i][j] == '-') {
				id[i][j] = now++;
			}
		}
	}

	V = now * 2;

	rep(i, V) {
		G[i].clear();
		rG[i].clear();
	}

	rep(i, R) {
		rep(j, C) {
			if (c[i][j] == '|' || c[i][j] == '-') {
				memset(us, 0, sizeof(us));
				bool f = go(i, j-1, 0, 0) && go(i, j+1, 2, 0);

				if (f) {
					cur = id[i][j] * 2;
					memset(us, 0, sizeof(us));					
					go(i, j-1, 0, 1);
					go(i, j+1, 2, 1);
				} else {
					add_edge(id[i][j] * 2, id[i][j] * 2 + 1);
				}

				memset(us, 0, sizeof(us));
				f = go(i-1, j, 3, 0) && go(i+1, j, 1, 0);

				if (f) {
					cur = id[i][j] * 2 + 1;
					memset(us, 0, sizeof(us));
					go(i-1, j, 3, 1);
					go(i+1, j, 1, 1);
				} else {
					add_edge(id[i][j] * 2 + 1, id[i][j] * 2);
				}
			}
		}
	}

	rep(i, R) {
		rep(j, C) {
			if (c[i][j] == '.') {/*
				printf("DEBUG %d %d\n", i, j);
				for (int x : hl[i][j]) {
					cout << x << " ";
				}
				cout << endl;*/

				assert(hl[i][j].size() <= 2);

				if (hl[i][j].size() == 0) {
					puts("IMPOSSIBLE");
					return ;
				} else if (hl[i][j].size() == 1) {
					add_edge(hl[i][j][0] ^ 1, hl[i][j][0]);
				} else {
					add_edge(hl[i][j][1] ^ 1, hl[i][j][0]);
					add_edge(hl[i][j][0] ^ 1, hl[i][j][1]);
				}
			}
		}
	}

	scc();
	rep(i, now) {
		if (cmp[i*2] == cmp[i*2+1]) {
			puts("IMPOSSIBLE");
			return ;			
		}
	}
	puts("POSSIBLE");

	rep(i, R) {
		rep(j, C) {
			if (c[i][j] == '|' || c[i][j] == '-') {
				if (cmp[id[i][j] * 2] < cmp[id[i][j] * 2 + 1]) {
					c[i][j] = '|';
				} else {
					c[i][j] = '-';
				}
			}
		}
		puts(c[i]);
	}
}

int main() {
	scanf("%d", &TC);

	rep(tc, TC) {
		solve(tc);
	}

	return 0;
}