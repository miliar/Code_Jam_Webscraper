#include <iostream>
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstring>
#include <map>
#include <numeric>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int rowCount, colCount;
vector<string> board;
vector<vector<bool>> filled;


void solve() {
	for (int r = 0; r < rowCount; r++) {
		for (int c = 0; c < colCount; c++) {
			if (!filled[r][c] && board[r][c] != '?') {
				char ch = board[r][c];
				int colIndex = c-1;
				int startCol = c;
				int endCol = c;
				while (colIndex >= 0 && board[r][colIndex] == '?') {
					board[r][colIndex] = ch;
					filled[r][colIndex] = true;
					startCol = colIndex--;
				}
				colIndex = c + 1;
				while (colIndex < colCount && board[r][colIndex] == '?') {
					board[r][colIndex] = ch;
					filled[r][colIndex] = true;
					endCol = colIndex++;
				}


				for (int i = r - 1; i >= 0; i--) {
					bool isAllEmpty = true;
					for (int j = startCol; j <= endCol; j++) {
						if (board[i][j] != '?') {
							isAllEmpty = false;
							break;
						}
					}
					if (isAllEmpty) {
						for (int j = startCol; j <= endCol; j++) {
							board[i][j] = ch;
							filled[i][j] = true;
						}
					}
					else {
						break;
					}
				}

				for (int i = r + 1; i < rowCount; i++) {
					bool isAllEmpty = true;
					for (int j = startCol; j <= endCol; j++) {
						if (board[i][j] != '?') {
							isAllEmpty = false;
							break;
						}
					}
					if (isAllEmpty) {
						for (int j = startCol; j <= endCol; j++) {
							board[i][j] = ch;
							filled[i][j] = true;
						}
					}
					else {
						break;
					}
				}

				filled[r][c] = true;
				c = endCol;
			}
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int testCase;
	cin >> testCase;
	for (int t = 1; t <= testCase; t++) {
		cin >> rowCount >> colCount;
		board.resize(rowCount);
		for (int i = 0; i < rowCount; i++) {
			cin >> board[i];
		}

		filled.assign(rowCount, vector<bool>(colCount, false));

		solve();

		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < rowCount; i++) {
			cout << board[i] << endl;
		}
	}

}