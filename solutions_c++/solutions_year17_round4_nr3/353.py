/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const char H = '-';
const char V = '|';

//intended to solve the small only, this is my strategy for this GCJ. :)

vector<string> grid;

void print_ans(bool good, int &K) {
	if (!good) {
		cout << "Case #" << K << ": " << "IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << K << ": " << "POSSIBLE" << endl;
		for (auto &s : grid) {
			cout << s << endl;
		}
	}
	K++;
}

void flip(char &c) {
	if (c == H) c = V;
	else c = H;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	cin >> T;
	while (T--) {
		int n, m, i, j, k, l;
		cin >> n >> m;
		grid.clear();
		string s;

		vector<string> temp;

		for (i = 0; i < n; i++) {
			cin >> s;
			grid.push_back(s);
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				if (grid[i][j] == V) {
					flip(grid[i][j]);
				}
			}
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j = k + 1) {
				int count = 0;
				for (k = j; k < m; k++) {
					if (grid[i][k] == '#') break;
					if (grid[i][k] == H || grid[i][k] == V) ++count;
				}
				if (count > 1) {
					for (l = j; l < k; l++) {
						if (grid[i][l] == V || grid[i][l] == H) flip(grid[i][l]);
					}
				}
			}
		}

		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j = k + 1) {
				int h_count = 0, v_count = 0;
				for (k = j; k < n; k++) {
					if (grid[k][i] == '#') break;
					if (grid[k][i] == H) ++h_count;
					if (grid[k][i] == V) ++v_count;
				}
				if (h_count + v_count > 1 && v_count) {
					print_ans(false, K);
					goto NXT;
				}
			}
		}

		temp = grid;

		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j = k + 1) {
				bool have = false;
				for (k = j; k < m; k++) {
					if (grid[i][k] == '#') break;
					if (grid[i][k] == H) have = true;
				}
				if (have) {
					for (l = j; l < k; l++) grid[i][l] = '#';
				}
			}
		}

		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j = k + 1) {
				bool have = false;
				for (k = j; k < n; k++) {
					if (grid[k][i] == '#') break;
					if (grid[k][i] == V) have = true;
				}
				if (have) {
					for (l = j; l < k; l++) grid[l][i] = '#';
				}
			}
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				if (grid[i][j] != '#') {
					print_ans(false, K);
					goto NXT;
				}
			}
		}

		grid = temp;
		print_ans(true, K);

		NXT:;
	}

	return 0;
}
