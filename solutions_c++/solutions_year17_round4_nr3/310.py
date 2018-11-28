#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAXN = 500;

//#define debug(...) fprintf(stderr, __VA_ARGS__)
#define debug(...)
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()

int R, C;
char A[6][51];	//- 0 | 1
int N;
int mirr[6][51];
int mirx[MAXN], miry[MAXN];
vector<int> adj[MAXN], radj[MAXN];

void _add (int x, int y) {
	adj[x].push_back(y);
	radj[y].push_back(x);
}

void addedge (int x, int y) {
	_add(x, y);
	_add(y ^ 1, x ^ 1);
}

void must (int x) {
	//says that x MUST happen
	addedge(x ^ 1, x);
}

void cannot (int x) {
	must(x ^ 1);
}

//SCC stuff
vector<int> nodes[MAXN], cadj[MAXN];
int bel[MAXN];
bool vis[MAXN];
int indeg[MAXN];
stack<int> stk;

void reset() {
	N = R = C = 0;
	memset(A, 0, sizeof(A));
	memset(mirr, -1, sizeof(mirr));
	for (int i = 0; i < MAXN; i++) {
		nodes[i].clear();
		cadj[i].clear();
		vis[i] = false;
		indeg[i] = 0;
		adj[i].clear();
		radj[i].clear();
		mirx[i] = miry[i] = -1;
	}
}

void dfs1 (int x) {
	vis[x] = true;
	for (int t : adj[x]) {
		if (!vis[t]) {
			dfs1(t);
		}
	}
	stk.push(x);
}

void dfs2 (int x) {
	vis[x] = false;
	bel[x] = C;
	nodes[C].push_back(x);
	for (int t : radj[x]) {
		if (vis[t]) {
			dfs2(t);
		}
	}
}

void find_scc() {
	//find strongly connected comps
	for (int i = 0; i < N; i++) {
		if (!vis[i]) {
			dfs1(i);
		}
	}
	while (!stk.empty()) {
		int x = stk.top();
		stk.pop();
		if (vis[x]) {
			//new group
			dfs2(x);
			C++;
		}
	}
	//toposort the comps...
	for (int i = 0; i < N; i++) {
		for (int t : adj[i]) {
			if (bel[i] != bel[t]) {
				cadj[bel[i]].push_back(bel[t]);
				indeg[t]++;
			}
		}
	}
	//ok now toposort them
	for (int i = 0; i < N; i++) {
		if (!indeg[i]) {
			stk.push(i);
		}
	}
	while (!stk.empty()) {
		int x = stk.top();
		stk.pop();
		for (int t : adj[x]) {
			if (!--indeg[t]) {
				stk.push(t);
			}
		}
	}
}

void go() {
	reset();
	scanf("%d %d", &R, &C);
	memset(mirr, -1, sizeof(mirr));
	for (int i = 0; i < R; i++) {
		scanf("%s", A[i]);
		for (int j = 0; j < C; j++) {
			if (A[i][j] == '-' || A[i][j] == '|') {
				mirr[i][j] = N;
				mirx[N] = i;
				miry[N] = j;
				debug("mirr %d %d\n", i, j);
				N++;
			}
		}
	}

	//if you want x to happen then !x -> x.
	//if one mirror hits itself then 
	for (int i = 0; i < R; i++) {
		int cur = 0;
		while (cur < C) {
			if (A[i][cur] == '#') {
				cur++;
				continue;
			}
			int ncur = cur;
			vector<int> mirrs;
			while (ncur < C && A[i][ncur] != '#') {
				if (mirr[i][ncur] >= 0) {
					mirrs.push_back(mirr[i][ncur]);
				}
				ncur++;
			}
			if (mirrs.size() >= 2) {
				//can't be horiz, any of them
				for (int m : mirrs) {
					must(2 * m + 1);
				}
			}
			cur = ncur;
		}
	}

	for (int j = 0; j < C; j++) {
		int cur = 0;
		while (cur < R) {
			if (A[cur][j] == '#') {
				cur++;
				continue;
			}

			int ncur = cur;
			vector<int> mirrs;
			while (ncur < R && A[ncur][j] != '#') {
				if (mirr[ncur][j] >= 0) {
					mirrs.push_back(mirr[ncur][j]);
				}
				ncur++;
			}

			if (mirrs.size() >= 2) {
				for (int m : mirrs) {
					must(2 * m);
				}
			}
			cur = ncur;
		}
	}

	//second part: where every place must hit by at least 1 mirr
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (A[i][j] != '.') {
				continue;
			}
			vector<int> vmirr;	//mirr on same vert line
			vector<int> hmirr;	//mirr on same horiz line
			for (int x = i; x < R && A[x][j] != '#'; x++) {
				if (mirr[x][j] >= 0) {
					vmirr.push_back(mirr[x][j]);
				}
			}
			for (int x = i; x >= 0 && A[x][j] != '#'; x--) {
				if (mirr[x][j] >= 0) {
					vmirr.push_back(mirr[x][j]);
				}
			}

			for (int y = j; y < C && A[i][y] != '#'; y++) {
				if (mirr[i][y] >= 0) {
					hmirr.push_back(mirr[i][y]);
				}
			}
			for (int y = j; y >= 0 && A[i][y] != '#'; y--) {
				if (mirr[i][y] >= 0) {
					hmirr.push_back(mirr[i][y]);
				}
			}

			if (hmirr.size() >= 2 && vmirr.size() >= 2) {
				//can't!
				debug("donald\n");
				puts("IMPOSSIBLE");
				return;
			}

			if (hmirr.size() >= 2) {
				//can only have vertical
				if (vmirr.empty()) {
					debug("trump\n");
					puts("IMPOSSIBLE");
					return;
				}
				must(2 * vmirr[0] + 1);
			} else if (vmirr.size() >= 2) {
				//can only have horizontal
				if (hmirr.empty()) {
					debug("elected\n");
					puts("IMPOSSIBLE");
					return;
				}

				must(2 * hmirr[0]);
			} else {
				//none of them! so one of them has to be
				if (vmirr.empty()) {
					if (hmirr.empty()) {
						debug("president\n");
						puts("IMPOSSIBLE");
						return;
					}
					must(2 * hmirr[0]);
				} else if (hmirr.empty()) {
					must(2 * vmirr[0] + 1);
				} else {
					addedge(2 * vmirr[0], 2 * hmirr[0]);
				}
			}
		}
	}

#warning N *= 2;
	N *= 2;
	find_scc();

	for (int i = 0; i < N; i += 2) {
		if (bel[i] == bel[i + 1]) {
			puts("IMPOSSIBLE");
			return;
		}
	}

	puts("POSSIBLE");
	for (int i = 0; i < C; i++) {
		for (int j : nodes[i]) {
			int mirid = j / 2, st = j % 2;
			A[mirx[mirid]][miry[mirid]] = (st ? '|' : '-');
		}
	}
	for (int i = 0; i < R; i++) {
		puts(A[i]);
	}
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int i = 1; i <= nt; i++) {
		printf("Case #%d: ", i);
		go();
		debug("--------------------------------\n");
	}
}
