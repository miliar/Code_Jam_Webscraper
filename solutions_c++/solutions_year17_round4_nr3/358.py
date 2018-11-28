#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


bool is_shooted(int y, int x, vector<string> &grid)
{
	int C = grid[0].size();
	int R = grid.size();
	for (int i = x - 1; i >= 0 && grid[y][i] != '#'; --i) if (grid[y][i] == '-') {
		return true;
	}
	for (int i = x + 1; i < C && grid[y][i] != '#'; ++i) if (grid[y][i] == '-') {
		return true;
	}
	for (int i = y - 1; i >= 0 && grid[i][x] != '#'; --i) if (grid[i][x] == '|') {
		return true;
	}
	for (int i = y + 1; i < R && grid[i][x] != '#'; ++i) if (grid[i][x] == '|') {
		return true;
	}
	return false;
}

bool solve(vector<string> &grid, vector<pair<int, int>> &shooters, vector<bool> &hall, vector<bool> &vall, int pos = 0)
{
	if (pos == shooters.size()) {
		for (int i = 0; i < grid[0].size(); ++i) {
			for (int j = 0; j < grid.size(); ++j) {
				if (grid[j][i] == '.') {
					if (!is_shooted(j, i, grid)) return false;
				}
			}
		}
		return true;
	}
	auto& sh = shooters[pos];
	if (hall[pos]) {
		grid[sh.second][sh.first] = '-';
		if (solve(grid, shooters, hall, vall, pos + 1)) return true;
	}
	if (vall[pos]) {
		grid[sh.second][sh.first] = '|';
		if (solve(grid, shooters, hall, vall, pos + 1)) return true;
	}
	return false;
}

bool check_poss(vector<string> &grid, vector<pair<int, int>> &shooters, vector<bool> &hall, vector<bool> &vall)
{
	vector<pair<int, int>> dots;
	for (int i = 0; i < grid[0].size(); ++i) {
		for (int j = 0; j < grid.size(); ++j) {
			if (grid[j][i] == '.') {
				dots.push_back(make_pair(i, j));
			}
		}
	}

	for (int pos = 0; pos < shooters.size(); ++pos) {
		auto& sh = shooters[pos];
		if (hall[pos]) {
			grid[sh.second][sh.first] = '-';
		}
	}
	for (int i = 0; i < dots.size(); ++i) {
		if (is_shooted(dots[i].second, dots[i].first, grid)) {
			dots.erase(dots.begin() + i);
			--i;
		}
	}

	for (int pos = 0; pos < shooters.size(); ++pos) {
		auto& sh = shooters[pos];
		if (vall[pos]) {
			grid[sh.second][sh.first] = '|';
		}
	}
	for (int i = 0; i < dots.size(); ++i) {
		if (is_shooted(dots[i].second, dots[i].first, grid)) {
			dots.erase(dots.begin() + i);
			--i;
		}
	}
	return dots.size() == 0;

}

int main() {
	int T;
	cin >> T;
	for (int q = 1; q <= T; ++q) {
		int R, C;
		cin >> R >> C;
		vector<string> grid(R);
		for (auto& r : grid) cin >> r;

		vector<pair<int, int>> shooters;
		for (int i = 0; i < C; ++i) for (int j = 0; j < R; ++j) {
			auto& c = grid[j][i];
			if (c == '|' || c == '-') shooters.push_back(make_pair(i, j));
		}

		vector<bool> hall(shooters.size(), true);
		vector<bool> vall(shooters.size(), true);

		for (int s = 0; s < shooters.size(); ++s) {
			auto& sh = shooters[s];
			int x = sh.first;
			int y = sh.second;
			for (int i = x - 1; i >= 0 && grid[y][i] != '#'; --i) if (grid[y][i] == '-' || grid[y][i] == '|') {
				hall[s] = false;
				break;
			}
			for (int i = x + 1; i < C && grid[y][i] != '#'; ++i) if (grid[y][i] == '-' || grid[y][i] == '|') {
				hall[s] = false;
				break;
			}
		}

		for (int s = 0; s < shooters.size(); ++s) {
			auto& sh = shooters[s];
			int x = sh.first;
			int y = sh.second;
			for (int i = y - 1; i >= 0 && grid[i][x] != '#'; --i) if (grid[i][x] == '-' || grid[i][x] == '|') {
				vall[s] = false;
				break;
			}
			for (int i = y + 1; i < R && grid[i][x] != '#'; ++i) if (grid[i][x] == '-' || grid[i][x] == '|') {
				vall[s] = false;
				break;
			}
		}

		bool ret = true;
		for (int i = 0; i < shooters.size(); ++i) if (!hall[i] && !vall[i]) ret = false;
		if (ret) ret = check_poss(grid, shooters, hall, vall);
		if (ret) ret = solve(grid, shooters, hall, vall);

		cout << "Case #" << q << ": " << (ret ? "POSSIBLE" : "IMPOSSIBLE") << endl;
		if (ret) for (auto& r : grid) cout << r << endl;
	}
	return 0;
}