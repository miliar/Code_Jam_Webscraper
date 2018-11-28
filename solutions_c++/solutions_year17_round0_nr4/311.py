#include <bits/stdc++.h>


#define puba push_back
#define ff first
#define ss second
#define pii pair <int, int>


using namespace std;


typedef long long LL;


const int MAXN = 110;
const int MAXV = 2 * MAXN * MAXN + 6 * MAXN;
const int MAXE = 8 * MAXN * MAXN + 12 * MAXN;
const int INF = (int) 1e9;


char mat[MAXN][MAXN];
bool col_f[MAXN], row_f[MAXN], inc_d[2 * MAXN], dec_d[2 * MAXN];
int sz;
int cap[MAXE], f[MAXE], fr[MAXE], to[MAXE], label[MAXV], q[MAXV];
int dist[MAXV], anses[MAXN][MAXN];
vector < int > g[MAXV];

void init() {
	memset(mat, 0, sizeof(mat));
	memset(row_f, 0, sizeof(row_f));
	memset(col_f, 0, sizeof(col_f));
	memset(inc_d, 0, sizeof(inc_d));
	memset(dec_d, 0, sizeof(dec_d));
	memset(anses, 0, sizeof(anses));
	sz = 0;
	for (int i = 0; i < MAXV; ++i) g[i].clear();
}


void add_edge(int _fr, int _to, int c) {
	fr[sz] = _fr;
	to[sz] = _to;
	cap[sz] = c;
	f[sz] = 0;
	g[_fr].puba(sz++);

	fr[sz] = _to;
	to[sz] = _fr;
	cap[sz] = 0;
	f[sz] = 0;
	g[_to].puba(sz++);
}


int n, m;


int num(int x, int y) {
	return x * n + y;
}


int dfs(int v, int flow, int ed) {
	if (v == ed) return flow;

	for (; label[v] < (int) g[v].size(); ++label[v]) {
		int e = g[v][label[v]];
		if (dist[v] + 1 == dist[to[e]] && cap[e] != f[e]) {
			int pushed = dfs(to[e], min(flow, cap[e] - f[e]), ed);
			if (pushed) {
				f[e] += pushed;
				f[e ^ 1] -= pushed;
				return pushed;
			}
		}
	}
	return 0;
}


bool bfs() {
	memset(label, 0, sizeof(label));
	fill(dist, dist + MAXV, INF);
	dist[0] = 0;
	int qsz = 1;
	q[0] = 0;

	for (int l = 0; l < qsz; ++l) {
		int v = q[l];
		for (int e : g[v]) {
			if (dist[to[e]] == INF && cap[e] != f[e]) {
				dist[to[e]] = dist[v] + 1;
				q[qsz++] = to[e];
			}
		}
	}
	return dist[1] != INF;
}


int in_flow(int x, int y) {
	int ans = 0;

	int v = 2 + num(x, y);
	for (int e : g[v]) {
		if (f[e] > 0) {
			ans += 2 * f[e];
		}
	}
	v = n * n + 2 * n + 2 + num(x, y);

	for (int e : g[v]) {
		if (f[e] > 0) {
			ans += f[e];
		}
	}
	return ans;
}


int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";

		init();

		cin >> n >> m;
		for (int i = 0; i < m; ++i) {
			char c;
			int x, y;
			cin >> c >> x >> y;
			--x, --y;
			mat[x][y] = c;
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] == 'o' || mat[i][j] == 'x') {
					row_f[i] = true;
					col_f[j] = true;
				}
				add_edge(2 + num(i, j), n * n + n + 2 + j, 1);
				add_edge(n * n + 2 + i, 2 + num(i, j), 1);
			}
		}

		for (int i = 0; i < n; ++i) {
			if (!row_f[i]) {
				add_edge(0, n * n + 2 + i, 1);
			}
			if (!col_f[i]) {
				add_edge(n * n + n + 2 + i, 1, 1);
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] == '+' || mat[i][j] == 'o') {
					inc_d[i + j] = true;
					dec_d[i - j + n - 1] = true;
				}

				add_edge(n * n + 2 * n + 2 + num(i, j), 2 * n * n + 4 * n + 1 + (i - j + n - 1), 1);
				add_edge(2 * n * n + 2 * n + 2 + (i + j), n * n + 2 * n + 2 + num(i, j), 1);
			}
		}

		for (int i = 0; i < 2 * n - 1; ++i) {
			if (!inc_d[i]) {
				add_edge(0, 2 * n * n + 2 * n + 2 + i, 1);
			}
			if (!dec_d[i]) {
				add_edge(2 * n * n + 4 * n + 1 + i, 1, 1);
			}
		}

		while (bfs()) {
			while (dfs(0, INF, 1));
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				anses[i][j] = in_flow(i, j);					
			}
		}

		vector < pii > as;
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (anses[i][j] != 0) {
					if (mat[i][j] != 0) {
						mat[i][j] = 'o';
					}
					else {
						if (anses[i][j] == 1) mat[i][j] = '+';
						if (anses[i][j] == 2) mat[i][j] = 'x';
						if (anses[i][j] == 3) mat[i][j] = 'o';
					}
					as.puba({i, j});
				}

				if (mat[i][j] == 'x' || mat[i][j] == '+') ans += 1;
				if (mat[i][j] == 'o') ans += 2;
			}
		}

		cout << ans << " " << as.size() << endl;
		for (int i = 0; i < (int) as.size(); ++i) {
			int x = as[i].ff + 1;
			int y = as[i].ss + 1;
			cout << mat[x - 1][y - 1] << " " << x << " " << y << endl; 
		}

	}
	return 0;
}