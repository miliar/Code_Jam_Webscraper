#include <bits/stdc++.h>
using namespace std;

const int DX[] = {-1, 0, 1, 0};
const int DY[] = {0, 1, 0, -1};
const int N = 50;
const int V = N * N * 2;
string s[N];
vector<int> graph[V];
int scc[V], inTime[V], lowlink[V], ttime;
stack<int> st;
vector<int> reach[N][N][2];
int m, n;

int ver(int x, int y) {
	return 2 * (x * n + y);
}

int neg(int x) {
	return x ^ 1;
}

bool inside(int x, int y) {
	return x >= 0 && x < m && y >= 0 && y < n;
}

void shoot(int x, int y, int dir) {
	int start = ver(x, y);
// 	cout << x << ' ' << y << ' ' << dir << ' ';
	if (dir == 1 || dir == 3) start = neg(start);
	set<tuple<int, int, int> > states;
	while (x += DX[dir], y += DY[dir], inside(x, y) && s[x][y] != '#') {
		if (s[x][y] == '|' || s[x][y] == '-') {
			graph[start].push_back(neg(start));
		} else if (s[x][y] == '.') {
			reach[x][y][dir % 2].push_back(start);
		} else if (s[x][y] == '\\') {
			dir = 3 - dir;
		} else if (s[x][y] == '/') {
			dir = dir ^ 1;
		} else {
			assert(false);
		}
		if (!states.emplace(x, y, dir).second) break;
// 		cout << x << ' ' << y << ' ' << dir << ' ';
	}
// 	cout << "DONE" << '\n';
}

vector<vector<int> > verInSCC;

void dfs(int u) {
	st.push(u);
	inTime[u] = lowlink[u] = ttime++;
	for (auto v : graph[u]) if (scc[v] == -1) {
		if (inTime[v] == -1) {
			dfs(v);
			lowlink[u] = min(lowlink[u], lowlink[v]);
		} else {
			lowlink[u] = min(lowlink[u], inTime[v]);
		}
	}
	if (lowlink[u] == inTime[u]) {
		int sccID = verInSCC.size();
		verInSCC.push_back(vector<int>());
		int v;
		do {
			v = st.top();
			st.pop();
			verInSCC.back().push_back(v);
			scc[v] = sccID;
		} while (v != u);
	}
}

void run() {
	cin >> m >> n;
	for (int i = 0; i < m; ++i) cin >> s[i];
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			graph[ver(i, j)].clear();
			graph[neg(ver(i, j))].clear();
			for (int k = 0; k < 2; ++k) {
				reach[i][j][k].clear();
			}
		}
	}
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) if (s[i][j] == '|' || s[i][j] == '-') {
			for (int k = 0; k < 4; ++k) {
				shoot(i, j, k);
			}
		}
	}
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) if (s[i][j] == '.') {
			if (reach[i][j][0].size() + reach[i][j][1].size() == 0) {
				cout << "IMPOSSIBLE" << '\n';
				return;
			}
			if (reach[i][j][0].size() == 0 || reach[i][j][1].size() == 0) {
				for (int k = 0; k < 2; ++k) {
					for (auto x : reach[i][j][k]) {
						graph[neg(x)].push_back(x);
					}
				}
			} else {
				for (auto x : reach[i][j][0]) {
					for (auto y : reach[i][j][1]) {
						graph[neg(x)].push_back(y);
						graph[neg(y)].push_back(x);
					}
				}
			}
		}
	}
	memset(scc, -1, sizeof scc);
	memset(inTime, -1, sizeof inTime);
	ttime = 0;
	verInSCC.clear();
	const int nv = m * n * 2;
	for (int i = 0; i < nv; ++i) if (inTime[i] == -1) {
		dfs(i);
	}
	assert(st.empty());
	for (int i = 0; i < m * n * 2; ++i) if (scc[i] == scc[neg(i)]) {
		cout << "IMPOSSIBLE" << '\n';
		return;
	}
	vector<int> value (verInSCC.size(), -1);
	for (int i = 0; i < (int) verInSCC.size(); ++i) {
		if (value[i] == -1) value[i] = 1;
		for (auto v : verInSCC[i]) {
			//cout << v << '\n';
			value[scc[neg(v)]] = 1 - value[i];
		}
	}
	//for (auto x : value) cerr << x << ' '; cerr << endl;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (s[i][j] == '|' || s[i][j] == '-') {
				if (value[scc[ver(i, j)]]) {
					s[i][j] = '|';
				} else {
					s[i][j] = '-';
				}
			}
		}
	}
	cout << "POSSIBLE" << '\n';
	for (int i = 0; i < m; ++i) cout << s[i] << '\n';
}

int main() {
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) {
		cout << "Case #" << tc << ": ";
		run();
	}
	return 0;
}
