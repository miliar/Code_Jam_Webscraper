/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define err(...) fprintf(stderr, "%.2f : ", 1. * clock() / CLOCKS_PER_SEC), fprintf(stderr, __VA_ARGS__), fflush(stderr)

const int N = 103, VN = N * N;

typedef pair<int, int> pii;

char s[N][N];
int w, h, m, id[VN];
int cc, qst, qen, u[VN], d[VN];
pii q[VN], fr[N][N];
vector<int> c[VN];
set<int> can_go[VN];
vector<pii> fire[VN];
vector<pii> cells[N][N];
vector<int> killing[N][N];
vector<int> path[VN];
int pa[VN], has[VN], goal[VN], to_kill[VN], is_killed[VN];

int F( int x, int y ) {
	return y * w + x;
}

void push( int j, int i, int D, pii from ) {
	int v = F(j, i);
	if (u[v] != cc) {
		u[v] = cc, d[v] = D;
		fr[i][j] = from;
		q[qen++] = {j, i};
	}
}

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void add( int a, int b, pii fireCell ) {
	// err("add %d --> %d\n", a, b);
	c[a].push_back(b);
	can_go[a].insert(b);
	fire[a].push_back(fireCell);
}

bool good( int j1, int i1 ) {
	return 0 <= j1 && j1 < w && 0 <= i1 && i1 < h && s[i1][j1] != '#';
}

void bfs( int j, int i ) {
	int from = F(j, i);
	// err("start from %d %d\n", j, i);
	qst = qen = 0, cc++;
	push(j, i, 0, pii(-1, -1));
	while (qst < qen) {
		j = q[qst].first, i = q[qst++].second;
		int D = d[F(j, i)];
		// err("d[%d,%d] = %d (m=%d)\n", j, i, D, m);
		forn(k, 4) {
			int j1 = j + dx[k], i1 = i + dy[k];
			if (good(j1, i1))
				push(j1, i1, D + 1, pii(j, i));
		}
	}
}

bool dfs( int v ) {
	u[v] = cc;
	for (int x : c[v])
		if (pa[x] == -1 || (u[pa[x]] != cc && dfs(pa[x]))) {
			pa[x] = v;
			return 1;
		}
	return 0;
}

bool visited( pii p ) {
	// err("visited: u=%d, %d <= %d\n", u[F(p.first, p.second)] == cc, d[F(p.first, p.second)], m);
	return u[F(p.first, p.second)] == cc && d[F(p.first, p.second)] <= m;
}

vector<int> getPath( int a, int b ) {
	qst = qen = 0, cc++;
	push(a % w, a / w, 0, pii(-1, -1));
	while (qst < qen) {
		int j = q[qst].first, i = q[qst++].second;
		int D = d[F(j, i)];
		forn(k, 4) {
			int j1 = j + dx[k], i1 = i + dy[k];
			if (good(j1, i1))
				push(j1, i1, D + 1, pii(j, i));
		}
	}
	int j = b % w, i = b / w;
	assert(u[b] == cc);
	cc++;
	// printf("dist %d --> %d : %d\n", a, b, d[b]);
	vector<int> res;
	while (j != -1) {
		for (int p : killing[i][j])
			if (u[p] != cc) 
				res.push_back(p), u[p] = cc;
		pii f = fr[i][j];
		j = f.first, i = f.second;
	}
	return res;
}

void out( int a, int b ) {
	printf("%d %d\n", id[a] + 1, id[b] + 1);
}

void solve() {
	scanf("%d%d%d", &w, &h, &m);
	int numS = 0, numT = 0;
	forn(i, h) {
		scanf("%s", s[i]);
		forn(j, w) {
			if (s[i][j] == 'S') id[F(j, i)] = numS++;
			if (s[i][j] == 'T') id[F(j, i)] = numT++;
		}
	}
	int vn = h * w;
	forn(i, h)
		forn(j, w) {
			cells[i][j].clear();
			killing[i][j].clear();
		}
	forn(i, h)
		forn(j, w) 
			if (s[i][j] == 'T') 
				forn(k, 4) 
					for (int j1 = j, i1 = i; good(j1, i1); j1 += dx[k], i1 += dy[k]) {
						cells[i][j].push_back(pii {j1, i1});
						killing[i1][j1].push_back(F(j, i));
					}
	forn(i, vn) {
		can_go[i].clear();
		c[i].clear();
		fire[i].clear();
	}
	forn(i, h)
		forn(j, w) 
			if (s[i][j] == 'S') {
				bfs(j, i);
				forn(i1, h)
					forn(j1, w) 
						if (s[i1][j1] == 'T') {
							// err("%d,%d : check %d,%d\n", j, i, j1, i1);
							bool good = 0;
							pii fireCell(-1, -1);
							for (auto cell : cells[i1][j1])
								if (visited(cell)) {
									good = 1;
									fireCell = cell;
									break;
								}
							if (good)
								add(F(j, i), F(j1, i1), fireCell);
						}
			}

	int ans = 0;
	forn(i, vn)
		pa[i] = -1, has[i] = 0;
	for (int good = 1; good; ) {
		cc++, good = 0;
		forn(i, vn)
			if (!has[i] && dfs(i))
				ans++, good = 1, has[i] = 1;
	}
	printf("%d\n", ans);
	forn(i, vn)
		path[i].clear(), goal[i] = -1;
	forn(i, vn)
		if (pa[i] != -1) {
			int a = pa[i], pos = 0;
			while (c[a][pos] != i) 
				pos++;
			pii fireCell = fire[a][pos];
			// printf("%d,%d kills %d,%d, firing from cell %d,%d\n", a % w, a / w, i % w, i / w, fireCell.first, fireCell.second);
			path[a] = getPath(F(fireCell.first, fireCell.second), pa[i]);
			assert(path[a].size());
			goal[a] = i;
			// printf("%d %d\n", id[pa[i]] + 1, id[i] + 1);
			// printf("path = ");
			// for (int x : path) printf("%d ", x);
			// puts("");
		}
	cc++;
	bool run = 1;
	int cnt = 0;
	forn(i, vn)
		is_killed[i] = 0;
	while (cnt < ans) {
		run = 0;
		// printf("cnt = %d, ans = %d\n", cnt, ans);
		// forn(i, vn) if (goal[i] != -1) printf("%d wants %d\n", i, goal[i]);
		forn(i, vn) 
			if (goal[i] != -1) {
				int j = 0;
				while (is_killed[path[i][j]])
					j++;
				int need = path[i][j];
				if (pa[need] == i || pa[need] == -1) {
					run = 1;
					out(i, need), cnt++;
					is_killed[need] = cc;
					pa[goal[i]] = -1;
					goal[i] = -1;
				}
				to_kill[i] = need;
			}
		if (!run && cnt != ans) {
			forn(i, vn)
				if (goal[i] != -1) {
					// printf("%d --> kill=%d --> pair=%d\n", i, to_kill[i], pa[to_kill[i]]);
					assert(pa[to_kill[i]] != -1);
				}
			int i = 0;
			while (goal[i] == -1)
				i++;
			forn(j, vn)
				i = pa[to_kill[i]];
			cc++;
			// printf("cycle\n");
			while (i != -1 && u[i] != cc) {
				// printf("i=%d\n", i);
				u[i] = cc;
				int x = to_kill[i];
				pa[goal[i]] = -1, goal[i] = -1;
				out(i, x), cnt++;
				is_killed[x] = 1;
				i = pa[x];	
			}
		}
	}
	if (cnt != ans) {
		printf("FAIL: cnt=%d, ans=%d\n", cnt, ans);
		forn(i, vn) 
			if (goal[i] != -1) {
				int j = 0;
				while (u[path[i][j]] == cc)
					j++;
				int need = path[i][j];
				printf("%d needs %d, goals to kill %d\n", i, need, goal[i]);
			}

	}
	assert(cnt == ans);
}

int main() {
	int tn;
	scanf("%d", &tn);
	forn(t, tn) {
		printf("Case #%d: ", t + 1);
		err("Case #%d\n", t + 1);
		solve();
	}
}
