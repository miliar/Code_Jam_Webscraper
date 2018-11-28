#include <bits/stdc++.h>
using namespace std;

int TC, R, C, dir[4][2] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
char g[55][55], tmpg[55][55];
bool fail = 0;

void dfs(int x, int y, int d) {
	if (x < 0 || x >= R) return;
	if (y < 0 || y >= C) return;
	if (g[x][y] == '|' || g[x][y] == '-') {
		fail = 1;
		return;
	}
	if (g[x][y] == '#') return;
	if (g[x][y] == '.') g[x][y] = 'x';
	if (g[x][y] == '/') {
		if (d == 0) d = 3;
		else if (d == 1) d = 2;
		else if (d == 2) d = 1;
		else d = 0;
	}
	if (g[x][y] == '\\') {
		if (d == 0) d = 2;
		else if (d == 1) d = 3;
		else if (d == 2) d = 0;
		else d = 1;
	}
	dfs(x + dir[d][0], y + dir[d][1], d);
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++) scanf("%s", &g[i]);
		vector< pair<int, int> > V;
		for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (g[i][j] == '-' || g[i][j] == '|') V.push_back(make_pair(i, j));
		int ans = 0;
		bool flag= 0;
		for (int bm = 0; bm < (1 << V.size()); bm++) {
			for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) tmpg[i][j]= g[i][j];
			int cur = 0;
			fail = 0;
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (g[i][j] == '-' || g[i][j] == '|') {
						// try horizontal
						if (!(bm & (1 << cur))) {
							dfs(i, j + 1, 1);
							dfs(i, j - 1, 0);
							g[i][j] = '-';
						}
						// vert
						else {
							dfs(i - 1, j, 2);
							dfs(i + 1, j, 3);
							g[i][j] = '|';
						}
						cur++;
					}
				}
			}
			ans = 0;
			for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (g[i][j] == '.') ans++;
			if (ans == 0 && !fail) {
				printf("Case #%d: POSSIBLE\n", tc);
				for (int i = 0; i < R; i++) {
					for (int j = 0; j < C; j++) {
						printf("%c", (g[i][j] == 'x') ? '.' : g[i][j]);
					}
					printf("\n");
				}
				flag = 1;
				break;
			}
			for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) g[i][j] = tmpg[i][j];
		}
		if (!flag) printf("Case #%d: IMPOSSIBLE\n", tc);
	}
}
