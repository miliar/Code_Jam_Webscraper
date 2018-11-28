// Small Test Case Only (don't know how to handle diagonals for larger test cases yet).

#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

int orig_grida[200][200]; // +
int orig_gridb[200][200]; // x
int grida[200][200]; // +, think about diagonals
int gridb[200][200]; // x, think about rows and cols

struct update {
	update(char ch, int r, int c) : ch(ch), r(r), c(c) {}
	char ch; int r; int c;
};

char combine(bool plus, bool exx) {
	if (plus && exx) return 'o';
	if (plus) return '+';
	if (exx) return 'x';
	return '.';
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		memset(orig_grida, 0, sizeof(orig_grida));
		memset(orig_gridb, 0, sizeof(orig_gridb));
		memset(grida, 0, sizeof(grida));
		memset(gridb, 0, sizeof(gridb));

		int n, m; cin >> n >> m;
		for (int i = 0; i < m; ++i) {
			char model; int r, c; cin >> model >> r >> c;
			r--; c--;

			if (model == '+' || model == 'o') orig_grida[r][c] = grida[r][c] = 1;
			if (model == 'x' || model == 'o') orig_gridb[r][c] = gridb[r][c] = 1;
		}

		// Step One: handle diagonals (handles n=1 correctly)
		for (int i = 0; i < n; ++i) {
			grida[0][i] = 1;
			if (i != 0 && i != n - 1)
				grida[n - 1][i] = 1;
		}

		// Step Two: handle rows and cols (handles n=1 correctly)
		int loc = -1;
		for (int i = 0; i < n; ++i) {
			if (orig_gridb[0][i]) { loc = i; break; }
		}
		if (loc < 0) {
			for (int i = 0; i < n; ++i) {
				gridb[i][i] = 1;
			}
		} else {
			int curr_row = 1;
			for (int i = 0; i < n; ++i) {
				if (i == loc) continue;
				gridb[curr_row][i] = 1;
				curr_row++;
			}
		}

		vector<update> updates;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cout << combine(grida[i][j], gridb[i][j]);
				if (orig_grida[i][j] != grida[i][j] ||
					orig_gridb[i][j] != gridb[i][j])
					updates.push_back(update(combine(grida[i][j], gridb[i][j]), i + 1, j + 1));
			}
			cout << endl;
		}
		cout << endl;

		// We always score 3n-2 style points:
		// n "x" style points
		// 2n-2 "+" style points
		cout << "Case #" << test << ": " << (n == 1 ? 2 : (3 * n - 2)) << " " << updates.size() << endl;
		for (int i = 0; i < updates.size(); ++i) {
			cout << updates[i].ch << " " << updates[i].r << " " << updates[i].c << endl;
		}
	}
	return 0;
}