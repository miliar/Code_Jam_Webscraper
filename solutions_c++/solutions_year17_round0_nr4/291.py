#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int to_mask(char op) {
	if (op == '+') return 1;
	if (op == 'x') return 2;
	if (op == 'o') return 3;
}

char to_char(int mask) {
	if (mask == 1) return '+';
	if (mask == 2) return 'x';
	if (mask == 3) return 'o';
	return '.';
}

const int N = 110;

int mat[N][N], can[N][N];
int ret[N][N];
int n, m;

inline bool valid(int i, int j) {
	return min(i, j) >= 0 && max(i, j) < n;
}

int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> n >> m;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				mat[i][j] = ret[i][j] = 0;
				can[i][j] = 3;
			}
		}

		int total = 0;
		for (int k = 0; k < m; k++) {
			char op;
			int i, j;
			cin >> op >> i >> j;
			i--, j--;
			mat[i][j] = to_mask(op);

			if (mat[i][j] & 1) {
				for (int d = -n; d <= n; d++) {
					int x = i + d, y = j + d;
					if (valid(x, y) && (can[x][y] & 1)) {
						can[x][y] ^= 1;
					}

					x = i - d, y = j + d;
					if (valid(x, y) && (can[x][y] & 1)) {
						can[x][y] ^= 1;
					}
				}
				total++;
			}

			if (mat[i][j] & 2) {
				for (int d = -n; d <= n; d++) {
					int x = i + d, y = j;
					if (valid(x, y) && (can[x][y] & 2)) {
						can[x][y] ^= 2;
					}

					x = i, y = j + d;
					if (valid(x, y) && (can[x][y] & 2)) {
						can[x][y] ^= 2;
					}
				}
				total++;
			}
		}

		do {
			int best = -1;
			int bit = -1;
			auto p = make_pair(-1, -1);

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (can[i][j] & 1) {
						int rcount = 0;
						for (int d = -n; d <= n; d++) {
							int x = i + d, y = j + d;
							if (valid(x, y) && (can[x][y] & 1)) rcount++;
							x = i - d, y = j + d;
							if (valid(x, y) && (can[x][y] & 1)) rcount++; 
						}

						if (best == -1 || rcount < best) {
							best = rcount;
							bit = 1;
							p = make_pair(i, j);
						}
					}

					if (can[i][j] & 2) {
						int rcount = 0;
						for (int d = -n; d <= n; d++) {
							int x = i + d, y = j;
							if (valid(x, y) && (can[x][y] & 2)) rcount++;
							x = i, y = j + d;
							if (valid(x, y) && (can[x][y] & 2)) rcount++;
						}

						if (best == -1 || rcount < best) {
							best = rcount;
							bit = 2;
							p = make_pair(i, j);
						}
					}
				}
			}

			int i = p.first;
			int j = p.second;

			if (bit == 1) {
				for (int d = -n; d <= n; d++) {
					int x = i + d, y = j + d;
					if (valid(x, y) && (can[x][y] & 1)) can[x][y] ^= 1;
					x = i - d, y = j + d;
					if (valid(x, y) && (can[x][y] & 1)) can[x][y] ^= 1;
				}
				mat[i][j] |= 1;
				total++;
				ret[i][j] = mat[i][j];
			}

			if (bit == 2) {
				for (int d = -n; d <= n; d++) {
					int x = i + d, y = j;
					if (valid(x, y) && (can[x][y] & 2)) can[x][y] ^= 2;
					x = i, y = j + d;
					if (valid(x, y) && (can[x][y] & 2)) can[x][y] ^= 2;
				}
				mat[i][j] |= 2;
				total++;
				ret[i][j] = mat[i][j];
			}

			if (bit == -1) break;
		} while (true);

		vector<pair<int, int>> changes;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (ret[i][j]) {
					changes.emplace_back(i, j);
				}
			}
		}

		cout << "Case #" << t << ": ";
		cout << total << " " << changes.size() << "\n";

		for (auto& p : changes) {
			cout << to_char(ret[p.first][p.second]) << " " << (p.first + 1) << " " << (p.second + 1) << "\n";
		}

	}

	return 0;
}
