#include<cstdio>
#include<vector>
int n, m;
const int dir[4][2] = {
	{0,1},
	{1,0},
	{0,-1},
	{-1,0}
};
const int slash[4] = {
	3,2,1,0
};
const int bslash[4] = {
	1,0,3,2
};
char smap[55][55];
char map[55][55];
char lr[55][55][2];
char p;
int nodes[3000][2];
int nn;
int eg[10000][2];
int en;
int scc[6010];
std::vector<int> el[6010];
std::vector<int> bel[6010];
int chk[6010];
int pord[6010];
int tm;
int sccn;
int search(int px, int py, int pz, int pn) {
	int x, y, z;
	x = px;
	y = py;
	z = pz;
	int res = 0;
	while (1) {
		x += dir[z][0];
		y += dir[z][1];
		if (map[x][y] == '#')return res;
		if (map[x][y] == '-') {
			res++;
		}
		if (map[x][y] == '/') {
			z = slash[z];
		}
		if (map[x][y] == '\\') {
			z = bslash[z];
		}
		lr[x][y][z % 2] = pn;
		if (x == px&&y == py&&z == pz)return res;
	}
}
void addeg(int a, int b) {
	eg[en][0] = a;
	eg[en][1] = b;
	en++;
}
void dfs(int x) {
	if (chk[x] == 1)return;
	chk[x] = 1;
	for (int i = 0; i < el[x].size(); i++) {
		dfs(el[x][i]);
	}
	pord[tm] = x;
	tm++;
}
void grp(int x, int gn) {
	if (scc[x] != -1)return;
	scc[x] = gn;
	for (int i = 0; i < bel[x].size(); i++) {
		grp(bel[x][i], gn);
	}
}
void sccdecomp(int sn, int sm) {
	for (int i = 0; i < sn; i++) {
		el[i].clear();
		bel[i].clear();
		chk[i] = 0;
	}
	tm = 0;
	for (int i = 0; i < sm; i++) {
		el[eg[i][0]].push_back(eg[i][1]);
		bel[eg[i][1]].push_back(eg[i][0]);
	}
	for (int i = 0; i < sn; i++) {
		if (chk[i] == 0) {
			dfs(i);
		}
	}
	for (int i = 0; i < sn; i++) {
		scc[i] = -1;
	}
	sccn = 0;
	for (int i = sn - 1; i >= 0; i--) {
		if (scc[pord[i]] == -1) {
			grp(pord[i], sccn);
			sccn++;
		}
	}
	for (int i = 0; i < sn; i++) {
		el[i].clear();
		bel[i].clear();
	}
}
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", smap[i]);
		}
		n += 2;
		m += 2;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				map[i][j] = '#';
			}
		}
		for (int i = 0; i < n - 2; i++) {
			for (int j = 0; j < m - 2; j++) {
				map[i + 1][j + 1] = smap[i][j];
			}
		}
		nn = 0;
		en = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				lr[i][j][0] = -1;
				lr[i][j][1] = -1;
				if (map[i][j] == '|')map[i][j] = '-';
				if (map[i][j] == '-') {
					nodes[nn][0] = i;
					nodes[nn][1] = j;
					nn++;
				}
			}
		}
		int pn = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == '-') {
					if (lr[i][j][0] == -1) {
						int p = search(i, j, 0, pn) + search(i, j, 2, pn);
						if (p > 0) {
							addeg(pn, pn + nn);
						}
					}
					else addeg(pn, pn + nn);
					if (lr[i][j][1] == -1) {
						int p = search(i, j, 1, pn + nn) + search(i, j, 3, pn + nn);
						if (p > 0) {
							addeg(pn + nn, pn);
						}
					}
					else addeg(pn + nn, pn);
					pn++;
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == '.') {
					if (lr[i][j][0] == -1 && lr[i][j][1] == -1) {
						flag = false;
					}
					else if (lr[i][j][0] == -1) {
						addeg((lr[i][j][1] + nn) % (2 * nn), lr[i][j][1]);
					}
					else if (lr[i][j][1] == -1) {
						addeg((lr[i][j][0] + nn) % (2 * nn), lr[i][j][0]);
					}
					else {
						addeg((lr[i][j][1] + nn) % (2 * nn), lr[i][j][0]);
						addeg((lr[i][j][0] + nn) % (2 * nn), lr[i][j][1]);
					}
				}
			}
		}
		sccdecomp(2 * nn, en);
		for (int i = 0; i < nn; i++) {
			if (scc[i] > scc[i + nn]) {
				map[nodes[i][0]][nodes[i][1]] = '-';
			}
			else if (scc[i] < scc[i + nn]) {
				map[nodes[i][0]][nodes[i][1]] = '|';
			}
			else {
				flag = false;
			}
		}
		if (flag) {
			printf("Case #%d: POSSIBLE\n", tc);
			for (int i = 0; i < n - 2; i++) {
				for (int j = 0; j < m - 2; j++) {
					printf("%c", map[i + 1][j + 1]);
				}
				printf("\n");
			}
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
	}
	return 0;
}
