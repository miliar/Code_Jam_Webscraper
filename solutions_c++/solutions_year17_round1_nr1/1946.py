#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		int m;
		vector <string> grid;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			string tmp;
			cin >> tmp;
			grid.push_back(tmp);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				char c = grid[i][j];
				if (c != '?') {
					for (int x = j - 1; x >= 0 && grid[i][x] == '?'; x--) {
						grid[i][x] = c;
					}
					for (int x = j + 1; x < m && grid[i][x] == '?'; x++) {
						grid[i][x] = c;
					}
				}
			}
		}

		char last = '*';
		int idx = -1;
		for (int i = 0; i < n; i++) {
			if (grid[i][0] == '?') {
				for (int j = 0; j < m; j++) {
					char c = '*';
					for (int y = i - 1; y >= 0 && c == '*'; y--) {
						if (grid[y][j] != '?') {
							c = grid[y][j];
						}
					}
					for (int y = i + 1; y < n && c == '*'; y++) {
						if (grid[y][j] != '?') {
							c = grid[y][j];
						}
					}
					if (c == '*') {
						if (last != '*') {
							c = last;
						} else {
							idx = j;
						}
					}
					if (c != '*') {
						if (idx >= 0) {
							for (int k = 0; k <= idx; k++) {
								for (int x = i; x >= 0 && grid[x][k] == '?'; x--) {
									grid[x][k] = c;
								}
								for (int x = i + 1; x < n && grid[x][k] == '?'; x++) {
									grid[x][k] = c;
								}
							}
							idx = -1;
						} else {
							for (int x = i; x >= 0 && grid[x][j] == '?'; x--) {
								grid[x][j] = c;
							}
							for (int x = i + 1; x < n && grid[x][j] == '?'; x++) {
								grid[x][j] = c;
							}
						}
						last = c;
					}

				}
			}
		}

		cout << "Case #" << t << ": " << endl;;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << grid[i][j];
			}
			cout << endl;
		}
	}
}

