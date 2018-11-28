#include <bits/stdc++.h>
using namespace std;

struct Task {
	int n, m;
	vector<vector<int>> a, b;
	vector<vector<int>> g;
	vector<int> mt1, mt2, was;

	Task(int n, int m): n(n), m(m), a(n, vector<int>(n)), b(n, vector<int>(n)) {
		for (int i = 0; i < m; ++i) {
			int x, y;
			char symbol;
			cin >> symbol >> x >> y;
			--x; --y;
			if (symbol == 'x') symbol = 1;
			if (symbol == '+') symbol = 2;
			if (symbol == 'o') symbol = 3;
			a[x][y] = b[x][y] = symbol;
		}
	}

	bool dfs(int v) {
		if (was[v]) {
			return false;
		}
		was[v] = 1;
		for (auto& to : g[v]) {
			if (mt2[to] == -1 || dfs(mt2[to])) {
				mt2[to] = v;
				mt1[v] = to;
				return true;
			}
		}
		return false;
	}

	void run() {
		vector<int> col(n), row(n);
		g.resize(2*n);

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (a[i][j] & 1) {
					row[i] = col[j] = 1;
				}
			}
			g[i].clear();
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (!row[i] && !col[j]) {
					g[i].push_back(j);
				}
			}
		}

		mt1.assign(n, -1);
		mt2.assign(n, -1);
		was.resize(n);
		bool change;
		do {
			change = false;
			for (int i = 0; i < n; ++i) {
				was[i] = 0;
			}
			for (int i = 0; i < n; ++i) {
				if (mt1[i] == -1) 
					change |= dfs(i);
			}
		} while (change);

		for (int i = 0; i < n; ++i) {
			if (mt1[i] != -1) {
				b[i][mt1[i]] |= 1;
			}
		}

		mt1.assign(2*n, -1);
		mt2.assign(2*n, -1);

		for (int i = 0; i < 2*n; ++i) {
			g[i].clear();
		}

		row.assign(2*n, 0);
		col.assign(2*n, 0);

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (a[i][j] & 2) {
					row[i + j] = 1;
					col[i - j + n] = 1;
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (!row[i + j] && !col[i - j + n]) {
					g[i + j].push_back(i - j + n);
				}
			}
		}

		was.resize(2 * n);
		do {
			change = false;
			for (int i = 0; i < 2 * n; ++i) {
				was[i] = 0;
			}
			for (int i = 0; i < 2 * n; ++i) {
				if (mt1[i] == -1) 
					change |= dfs(i);
			}
		} while (change);

		for (int i = 0; i < 2 * n; ++i) {
			if (mt1[i] != -1) {
				int x = (i + (mt1[i] - n)) / 2;
				int y = (i - (mt1[i] - n)) / 2;
				b[x][y] |= 2;
			}
		}

		int result = 0;
		vector<tuple<char, int, int>> out;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (b[i][j] & 1) ++result;
				if (b[i][j] & 2) ++result;

				if (a[i][j] != b[i][j]) {
					char symbol;
					if (b[i][j] == 1) symbol = 'x';
					if (b[i][j] == 2) symbol = '+';
					if (b[i][j] == 3) symbol = 'o';
					out.push_back(make_tuple(symbol, i + 1, j + 1));
				}
			}
		}

		cout << result << ' ' << (int)out.size() << '\n';

		for (auto& item : out) {
			cout << get<0>(item) << ' ' << get<1>(item) << ' ' << get<2>(item) << '\n';
		}

	}
};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		int n, m;
		cin >> n >> m;
		Task task(n, m);
		task.run();
	}

	return 0;
}