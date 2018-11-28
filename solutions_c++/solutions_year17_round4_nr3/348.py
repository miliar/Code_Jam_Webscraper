#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <list>
#include <array>
#include <map>
#include <algorithm>
#include <set>
#include <utility>
#include <cmath>
#include <cassert>
using namespace std;

static bool search(vector<string> &G, const vector<pair<int, int>> &empty_cells, const map<pair<int, int>, map<pair<int, int>, char>> &req, int i, set<pair<int, int>> &fixed) {
	if (i == empty_cells.size()) {
		return true;
	}
	for (auto &laser_pos_dir : req.at(empty_cells.at(i))) {
		auto &laser_pos = laser_pos_dir.first;
		auto &laser_dir = laser_pos_dir.second;

		if (0 < fixed.count(laser_pos)) {
			if (laser_dir == G[laser_pos.first][laser_pos.second]) {
				return search(G, empty_cells, req, i + 1, fixed);
			} else {
				continue;
			}
		}

		fixed.insert(laser_pos);
		G[laser_pos.first][laser_pos.second] = laser_dir;
		if (search(G, empty_cells, req, i + 1, fixed)) {
			return true;
		}
		fixed.erase(laser_pos);
	}
	return false;
}

static bool run(const vector<string> &G, int i, int j, const pair<int, int> &dir, set<pair<int, int>> &route) {
	if (i < 0 || i >= G.size() || j < 0 || j >= G[0].size()) {
		return true;
	}
	if (G[i][j] == '#') {
		return true;
	} else if (G[i][j] == '-' || G[i][j] == '|') {
		return false;
	} else if (G[i][j] == '.') {
		route.emplace(i, j);
		return run(G, i + dir.first, j + dir.second, dir, route);
	} else if (G[i][j] == '/') {
		pair<int, int> new_dir = {-dir.second, -dir.first};
		return run(G, i + new_dir.first, j + new_dir.second, new_dir, route);
	} else if (G[i][j] == '\\') {
		pair<int, int> new_dir = {dir.second, dir.first};
		return run(G, i + new_dir.first, j + new_dir.second, new_dir, route);
	}
	assert(false);
}

static void solve() {
	int R, C;
	cin >> R >> C;
	vector<string> G;
	for (int i = 0; i < R; i++) {
		string s;
		cin >> s;
		G.push_back(s);
	}

	set<pair<int, int>> empty_cells;
	map<pair<int, int>, map<pair<int, int>, char>> req;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (G[i][j] == '.') {
				empty_cells.emplace(i, j);
			}
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (G[i][j] == '|' || G[i][j] == '-') {
				set<pair<int, int>> horizontal_route, vertical_route;
				bool horizontal_safe = run(G, i, j - 1, {0, -1}, horizontal_route) && run(G, i, j + 1, {0, 1}, horizontal_route);
				bool vertical_safe = run(G, i - 1, j, {-1, 0}, vertical_route) && run(G, i + 1, j, {1, 0}, vertical_route);

				if (horizontal_safe && vertical_safe) {
					for (auto &cell : horizontal_route) {
						if (0 < vertical_route.count(cell)) {
							empty_cells.erase(cell);
						} else if (0 < empty_cells.count(cell)) {
							req[cell][make_pair(i, j)] = '-';
						}
					}
					for (auto &cell : vertical_route) {
						if (0 < empty_cells.count(cell)) {
							req[cell][make_pair(i, j)] = '|';
						}
					}
				} else {
					if (horizontal_safe) {
						G[i][j] = '-';
						for (auto &cell : horizontal_route) {
							empty_cells.erase(cell);
						}
					} else if (vertical_safe) {
						G[i][j] = '|';
						for (auto &cell : vertical_route) {
							empty_cells.erase(cell);
						}
					} else {
						cout << "IMPOSSIBLE";
						return;
					}
				}
			}
		}
	}

	for (auto &cell : empty_cells) {
		if (req[cell].empty()) {
			cout << "IMPOSSIBLE";
			return;
		}
	}

	vector<pair<int, int>> empty_cells_vector(empty_cells.begin(), empty_cells.end());
	set<pair<int, int>> fixed;

	if (search(G, empty_cells_vector, req, 0, fixed)) {
		cout << "POSSIBLE";
		for (auto &row : G) {
			cout << endl << row;
		}
	} else {
		cout << "IMPOSSIBLE";
	}
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
