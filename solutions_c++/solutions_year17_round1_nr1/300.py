#include <string>
#include <iostream>

using namespace std;

char cake[30][30];

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		int r, c; cin >> r >> c;
		for (int i = 0; i < r; ++i) {
			string line; cin >> line;
			for (int j = 0; j < c; ++j) {
				cake[i][j] = line[j];
			}
		}
		// drop down
		for (int i = 1; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (cake[i][j] == '?') cake[i][j] = cake[i - 1][j];
			}
		}
		// drop up
		for (int i = r-2; i >= 0; --i) {
			for (int j = 0; j < c; ++j) {
				if (cake[i][j] == '?') cake[i][j] = cake[i + 1][j];
			}
		}
		// drop right
		for (int i = 0; i < r; ++i) {
			for (int j = 1; j < c; ++j) {
				if (cake[i][j] == '?') cake[i][j] = cake[i][j - 1];
			}
		}
		// drop left
		for (int i = 0; i < r; ++i) {
			for (int j = c - 2; j >= 0; --j) {
				if (cake[i][j] == '?') cake[i][j] = cake[i][j+1];
			}
		}

		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}