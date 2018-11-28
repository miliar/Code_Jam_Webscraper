#include <iostream>
#include <string>
#include <vector>
#define DEBUG(s) (s)

using namespace std;

bool isFree(vector<string> &grid, int l, int r, int u, int d, char cur) {
	for (int toCheckI = u; toCheckI <= d; ++toCheckI) {
		for (int toCheckJ = l; toCheckJ <= r; ++toCheckJ) {
			if (grid[toCheckI][toCheckJ] != '?' && grid[toCheckI][toCheckJ] != cur) {
				return false;
			}
		}
	}
	return true;
}


void printCase(vector<string> ans, int caseNo) {
	for (string s : ans) {
		for (char c : s) {
			if (c == '?') {
				cout << caseNo << " aborted; cake not fully assigned\n";
			}
		}
	}
	cout << "Case #" << caseNo << ":\n";
	for (string s : ans) {
		cout << s << "\n";
	}
}

int main() {

	ios::sync_with_stdio(false); // YOU USE IOSTREAM NOW

	int T; cin >> T;
	for (int tC = 1; tC <= T; ++tC) {
		int R, C; cin >> R >> C;
		vector<string> cake(R, "");
		for (int row = 0; row < R; ++row) {
			cin >> cake[row];
		}

		vector<string> ans(cake);

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (cake[i][j] == '?') {
					continue;
				}

				int upper = i;
				int lower = i;
				int left = j;
				int right = j;

				for (int pUp = upper; pUp >= 0; --pUp) {
					if (isFree(ans, left, right, pUp, pUp, cake[i][j])) {
						upper = pUp;
					} else {
						break;
					}
				}

				for (int pDown = lower; pDown < R; ++pDown) {
					if (isFree(ans, left, right, pDown, pDown, cake[i][j])) {
						lower = pDown;
					} else {
						break;
					}
				}

				for (int pLeft = left; pLeft >= 0; --pLeft) {
					if (isFree(ans, pLeft, pLeft, upper, lower, cake[i][j])) {
						left = pLeft;
					} else {
						break;
					}
				}

				for (int pRight = right; pRight < C; ++pRight) {
					if (isFree(ans, pRight, pRight, upper, lower, cake[i][j])) {
						right = pRight;
					} else {
						break;
					}
				}

				for (int tfi = upper; tfi <= lower; ++tfi) {
					for (int tfj = left; tfj <= right; ++tfj) {
						ans[tfi][tfj] = cake[i][j];
					}
				}
			}
		}

		printCase(ans, tC);
	}
}