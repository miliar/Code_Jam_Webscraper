#include <iostream>
#include <vector>
#include <random>
#include <array>
#include <cstdlib>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()

template<typename T> int sz(const T& x) { return static_cast<int>(x.size()); }
template<typename T> void mx(T& x, const T& y) { x = std::max(x, y); }
template<typename T> void mn(T& x, const T& y) { x = std::min(x, y); }

vector<string> field;

int n, m;


vector<pair<int, int>> covered;

bool fill_covered(int i, int j, int di, int dj) {
	// cout << "fill_covered " << i << ' ' << j << ' ' << di << ' ' << dj << endl;

	if (i < 0 || i >= n || j < 0 || j >= m || field[i][j] == '#') {
		return true;
	}
	if (field[i][j] == '-' || field[i][j] == '|') {
		return false;
	}
	if (field[i][j] == '.') {
		covered.push_back({i, j});
		return fill_covered(i + di, j + dj, di, dj);
	}
	if (field[i][j] == '/') {
		int new_di = -dj;
		int new_dj = -di;
		return fill_covered(i + new_di, j + new_dj, new_di, new_dj);
	}
	if (field[i][j] == '\\') {
		int new_di = dj;
		int new_dj = di;
		return fill_covered(i + new_di, j + new_dj, new_di, new_dj);
	} 
	return false;
}

vector<vector<int>> g;
vector<vector<int>> gr;
vector<bool> used;
vector<int> order;
vector<int> comp;

void dfs1(int u) {
	used[u] = true;
	for (int v : g[u]) {
		if (!used[v]) {
			dfs1(v);
		}
	}
	order.push_back(u);
}

void dfs2(int u, int c) {
	comp[u] = c;
	for (int v : gr[u]) {
		if (comp[v] == -1) {
			dfs2(v, c);
		}
	}
}


bool build_ans() {
	vector<vector<bool> > need_cover(n, vector<bool>(m));
	forn (i, n) {
		forn (j, m) {
			need_cover[i][j] = (field[i][j] == '.');
		}
	}

	vector<vector<vector<int>>> vars(n, vector<vector<int>>(m));

	vector<vector<bool>> is_fixed(n, vector<bool>(m, false));

	forn (i, n) {
		forn (j, m) {
			if (field[i][j] == '|' || field[i][j] == '-') {
				covered.clear();
				bool can_vertical = (fill_covered(i - 1, j, -1, 0) && fill_covered(i + 1, j, +1, 0));
				// cout << "can_vertical: " << can_vertical << endl;

				auto covered_vertical = covered;

				covered.clear();
				bool can_horizontal = (fill_covered(i, j - 1, 0, -1) && fill_covered(i, j + 1, 0, +1));
				auto covered_horizontal = covered;

				if (!can_horizontal && !can_vertical) {
					// cout << "bad i=" << i << " j=" << j << endl;
					return false;
				}

				if (can_horizontal && can_vertical) {
					int hor_var = 2 * (i * m + j);
					int ver_var = 2 * (i * m + j) + 1;
					for (auto p : covered_horizontal) {
						vars[p.first][p.second].push_back(hor_var);
					}
					for (auto p : covered_vertical) {
						vars[p.first][p.second].push_back(ver_var);
					}
					continue;
				}

				if (can_horizontal) {
					field[i][j] = '-';
					for (auto p : covered_horizontal) {
						need_cover[p.first][p.second] = false;
					}
					is_fixed[i][j] = true;
				}

				if (can_vertical) {
					field[i][j] = '|';
					for (auto p : covered_vertical) {
						need_cover[p.first][p.second] = false;
					}
					is_fixed[i][j] = true;
				}
			}
		}
	}

	g.assign(2 * n * m, vector<int>());
	gr.assign(2 * n * m, vector<int>());

	auto add_arc = [&](int x, int y) {
		g[x].push_back(y);
		gr[y].push_back(x);
	};

	auto add_or = [&](int x, int y) {
		// x || y
		add_arc(x ^ 1, y);
		add_arc(y ^ 1, x);
	};

	forn (i, n) {
		forn (j, m) {
			if (need_cover[i][j] && vars[i][j].empty()) {
				return false;
			}
		}
	}

	// forn (i, n) {
		// forn (j, m) {
			// if (need_cover[i][j]) {
				// cout << "need_cover " << i << ' ' << j << endl;
			// }
		// }
	// }

	forn (i, n) {
		forn (j, m) {
			if (!need_cover[i][j]) {
				continue;
			}
			sort(all(vars[i][j]));
			vars[i][j].erase(unique(all(vars[i][j])), vars[i][j].end());
			if (sz(vars[i][j]) == 1) {
				// cout << vars[i][j][0] << endl;
				add_or(vars[i][j][0], vars[i][j][0]);
			} else if (sz(vars[i][j]) == 2) {
				// cout << vars[i][j][0] << " || " << vars[i][j][1] << endl;
				add_or(vars[i][j][0], vars[i][j][1]);
			} else if (sz(vars[i][j]) > 2) {
				cout << "ERROR" << endl;
			}
		}
	}

	used.assign(2 * n * m, false);
	order.clear();
	forn (i, 2 * n * m) {
		if (!used[i]) {
			dfs1(i);
		}
	}

	comp.assign(2 * n * m, -1);
	int comps = 0;
	forn (i, 2 * n * m) {
		int v = order[2 * n * m - 1 - i];
		if (comp[v] == -1) {
			dfs2(v, comps++);
		}
	}

	for (int i = 0; i < 2 * n * m; i += 2) {
		if (comp[i] == comp[i ^ 1]) {
			// cout << "bad sat " << i << endl;
			return false;
		}
		int c = (i / 2) % m;
		int r = (i / 2) / m;
		if ((field[r][c] == '|' || field[r][c] == '-') && !is_fixed[r][c]) {
			if (comp[i] < comp[i ^ 1]) {
				field[r][c] = '|';
			} else {
				field[r][c] = '-';
			}
		}
	}


	return true;
}

void solve() {
	cin >> n >> m;
	field.resize(n);
	forn (i, n) {
		cin >> field[i];
	}

	if (build_ans()) {
		cout << "POSSIBLE" << endl;
		forn (i, n) {
			cout << field[i] << endl;
		}
	} else {
		cout << "IMPOSSIBLE" << endl;
	}

}

int main() {
  int t;
  cin >> t;
  forn (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
