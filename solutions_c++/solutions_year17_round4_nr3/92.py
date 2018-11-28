#include <bits/stdc++.h>

using namespace std;

const int MX = 50, UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3;

const int dx[4] = {-1, 1,  0, 0};
const int dy[4] = { 0, 0, -1, 1};

vector<tuple<int, int, int>> f[MX][MX], G[MX][MX][3];
int g[MX][MX], gg[MX][MX], n, m;
char s[MX][MX + 1];

map<pair<int, char>, int> nextDir;
bool dfs(int x, int y, int dir, bool add = false, tuple<int, int, int> v = make_tuple(0, 0, 0), bool first = true) {
	if (x < 0 || x == n || y < 0 || y == m) return true;
	if (s[x][y] == '#') return true;
	if (first == false && (s[x][y] == '-' || s[x][y] == '|')) return false;
	
	if (add) f[x][y].push_back(v);
	
	if (s[x][y] == '/' || s[x][y] == '\\') dir = nextDir[make_pair(dir, s[x][y])];
	return dfs(x + dx[dir], y + dy[dir], dir, add, v, false);
}

bool dfs2sat(int x, int y, int v, bool add, bool first = true) {
	if (first) memcpy(gg, g, sizeof g);
	
	if (gg[x][y] == (v ^ 3)) return false;
	if (gg[x][y] == v) return true;
	gg[x][y] = v;
	if (add) g[x][y] = v;
	
	for (auto& e : G[x][y][v]) {
		int xx, yy, vv;
		tie(xx, yy, vv) = e;
		
		if (dfs2sat(xx, yy, vv, add, false) == false) return false;
	}
	
	return true;
}

int main() {
	nextDir[make_pair(UP, '/')] = RIGHT;
	nextDir[make_pair(UP, '\\')] = LEFT;
	nextDir[make_pair(DOWN, '/')] = LEFT;
	nextDir[make_pair(DOWN, '\\')] = RIGHT;
	nextDir[make_pair(LEFT, '/')] = DOWN;
	nextDir[make_pair(LEFT, '\\')] = UP;
	nextDir[make_pair(RIGHT, '/')] = UP;
	nextDir[make_pair(RIGHT, '\\')] = DOWN;
	
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) scanf(" %s", s[i]);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				f[i][j].clear();
				g[i][j] = 0;
			}
		
		bool ok = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] == '-' || s[i][j] == '|') {
					bool up = false, left = false;
					if (dfs(i, j, UP) && dfs(i, j, DOWN)) {
						dfs(i, j, UP, true, make_tuple(i, j, 1));
						dfs(i, j, DOWN, true, make_tuple(i, j, 1));
						
						up = true;
					}
					
					if (dfs(i, j, LEFT) && dfs(i, j, RIGHT)) {
						dfs(i, j, LEFT, true, make_tuple(i, j, 2));
						dfs(i, j, RIGHT, true, make_tuple(i, j, 2));
						
						left = true;
					}
					
					if (up == false && left == false) ok = false;
					if (up && left) continue;
					if (up) g[i][j] = 1;
					if (left) g[i][j] = 2;
				}
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				if (s[i][j] != '.') continue;
				
				if (f[i][j].size() == 0u) ok = false;
				else if (f[i][j].size() == 1u) {
					int x, y, kind;
					tie(x, y, kind) = f[i][j].back();
					
					if (g[x][y] == (kind ^ 3)) ok = false;
					g[x][y] = kind;
				}
				else {
					assert(f[i][j].size() == 2u);
					
					int x1, y1, kind1;
					tie(x1, y1, kind1) = f[i][j][0];
					
					int x2, y2, kind2;
					tie(x2, y2, kind2) = f[i][j][1];
					
					G[x1][y1][kind1 ^ 3].emplace_back(x2, y2, kind2);
					G[x2][y2][kind2 ^ 3].emplace_back(x1, y1, kind1);
				}
			}
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if ((s[i][j] == '-' || s[i][j] == '|') && g[i][j] != 0)
					ok = ok && dfs2sat(i, j, g[i][j], true);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if ((s[i][j] == '-' || s[i][j] == '|') && g[i][j] == 0) {
					if (dfs2sat(i, j, 1, false)) dfs2sat(i, j, 1, true);
					else if (dfs2sat(i, j, 2, false)) dfs2sat(i, j, 2, true);
					else ok = false;
				}
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] == '-' || s[i][j] == '|')
					s[i][j] = (g[i][j] == 1 ? '|' : '-');
		
		printf("Case #%d: %s\n", t, ok ? "POSSIBLE" : "IMPOSSIBLE");
		if (ok) for (int i = 0; i < n; i++) printf("%s\n", s[i]);
	}

	return 0;
}
