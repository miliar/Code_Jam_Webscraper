#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
using namespace std;
#define int long long
#define double long double
vector<string> grid;
vector<char> BLANK;
void fill_across(int r, char c, int s) {
	for (int i = s - 1; i >= 0; i--) {
		if (grid[r][i] != '?') break;
		grid[r][i] = c;
	}
	for (int i = s + 1; i < grid[r].size(); i++) {
		if (grid[r][i] != '?') break;
		grid[r][i] = c;
	}
}
void fill_up(int r, char c, int s) {
	for (int i = s - 1; i >= 0; i--) {
		if (grid[r][i] != '?') break;
		grid[r][i] = c;
	}
	for (int i = s + 1; i < grid[r].size(); i++) {
		if (grid[r][i] != '?') break;
		grid[r][i] = c;
	}
}
void solve(int r) {
	if (r >= grid.size()) return;
	int ii = -1;
	int tracker = 0;
	for (int iii = 0; iii < grid[r].size(); iii++) {
		char x = grid[r][iii];
		if (x != '?') {
			fill_across(r, x, tracker);
			ii = tracker;
		}
		tracker++;
	}
	if (ii < 0) {
		BLANK[r] = true;
	}
	solve(r+1);
}
void solve_blanks() {
	for (int i = 0; i < BLANK.size(); i++) {
		if (BLANK[i]) {
			int tmp = i;
			while (tmp < grid.size() && BLANK[tmp]) {
				tmp++;
			}
			if (tmp == grid.size()) {
				//wrong way
				for (int j = i; j < grid.size(); j++) {
					for (int jj = 0; jj < grid[i-1].size(); jj++) {
						grid[j][jj] = grid[i-1][jj];
					}
				}
			}
			else {
				for (int j = i; j < tmp; j++) {
					for (int jj = 0; jj < grid[tmp].size(); jj++) {
						grid[j][jj] = grid[tmp][jj];
					}
				}
			}
		}
		
	}
}
#undef int
int main() {
	#define int long long
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int cases; cin >> cases >> ws;
	for (int i = 1; i <= cases; i++) {
		int r,c; cin >> r >> c >> ws;
		grid.clear();
		BLANK.clear();
		cout << "Case #" << i << ":\n";
		for (int j = 0; j < r; j++) {
			string tmp; cin >> tmp >> ws;
			grid.emplace_back(tmp);
			BLANK.push_back(false);
		}
		solve(0);
		solve_blanks();
		for (auto s : grid) cout << s << endl;
	}
	
	return 0;
}