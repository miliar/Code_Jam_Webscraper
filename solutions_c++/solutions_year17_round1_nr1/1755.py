#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <numeric>
#include <regex>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 1; c <= t; ++c) {
		int R, C;
		cin >> R >> C;
		vector<string> grid(R);
		for (auto& row : grid) {
			cin >> row;
		}

		set<char> s;

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (grid[i][j] == '?') continue;

				if (s.find(grid[i][j]) != s.end()) continue;

				int m = j, M = j;
				for (; M < C and (grid[i][M] == '?' or grid[i][M] == grid[i][j]); ++M);
				for (; m >= 0 and (grid[i][m] == '?' or grid[i][m] == grid[i][j]); --m);

				int a = i, A = i;
				for(; A < R; ++A) {
					bool ok = true;
					for (int x = m+1; x < M; ++x) {
						if (grid[A][x] != '?' and grid[A][x] != grid[i][j]) {
							ok = false;
							break;
						}
					}

					if(not ok) break; 
				}

				for (; a >= 0; --a) {
					bool ok = true;
					for (int x = m+1; x < M; ++x) {
						if (grid[a][x] != '?' and grid[a][x] != grid[i][j]) {
							ok = false;
							break;
						}
					}

					if(not ok) break; 
				}

				for (int x = a+1; x < A; ++x) {
					for (int y = m+1; y < M; ++y) {
						grid[x][y] = grid[i][j];
					}
				}

				s.insert(grid[i][j]);
			}
		}

		cout << "Case #" << c << ":" << endl;
		for (auto& row : grid) cout << row << endl;
	}

	return 0;
}
