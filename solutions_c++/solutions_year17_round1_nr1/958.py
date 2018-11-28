#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve(vector<string> &T, int R, int C, int r, const vector<bool> &emptyThisRow, const vector<bool> &emptyAfterThisRow) {
	//cout << "row " << r << endl;
	if (emptyAfterThisRow[r]) {
		//cout << "CASE A" << endl;
		for (int r_ = r; r_ < R; ++r_) {
			T[r_] = T[r - 1];
		}
	} else {
		if (emptyThisRow[r]) {
			//cout << "CASE B" << endl;
			solve(T, R, C, r + 1, emptyThisRow, emptyAfterThisRow);
			T[r] = T[r + 1];
		} else {
			//cout << "CASE C" << endl;
			int c = 0;
			while (T[r][c] == '?') {
				++c;
			}
			char cur_char = T[r][c];
			for (c = 0; c < C; ++c) {
				if (T[r][c] == '?') {
					T[r][c] = cur_char;
				} else {
					cur_char = T[r][c];
				}
			}
			if (r + 1 < R) {
				solve(T, R, C, r + 1, emptyThisRow, emptyAfterThisRow);
			}
		}
	}
}

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		//cout << "test = " << test << endl;
		int R, C;
		cin >> R >> C;
		vector<string> T(R);
		vector<bool> emptyThisRow(R, true);
		vector<bool> emptyAfterThisRow(R);
		for (int r = 0; r < R; ++r) {
			cin >> T[r];
			//cout << "read " << T[r] << endl;
			for (int c = 0; c < C; ++c) {
				if (T[r][c] != '?') {
					emptyThisRow[r] = false;
				}
			}
		}
		//cout << "here" << endl;
		emptyAfterThisRow[R - 1] = emptyThisRow[R - 1];
		for (int r = R - 2; r >= 0; --r) {
			emptyAfterThisRow[r] = emptyThisRow[r] && emptyAfterThisRow[r + 1];
		}
		//cout << "starimg" << endl;
		solve(T, R, C, 0, emptyThisRow, emptyAfterThisRow);
		cout << "Case #" << test << ":" << endl;
		for (int r = 0; r < R; ++r) {
			cout << T[r] << endl;
		}
	}
	return 0;
}
