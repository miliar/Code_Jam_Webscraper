#include <iostream>
#include <set>
#include <vector>
#include <string>

using namespace std;

set<char> used;

void expandChar(vector<string>& grid, int currentRow, int currentColumn) {

	char c = grid[currentRow][currentColumn];

	int lastCol = currentColumn, firstCol = currentColumn;
	for (int i = currentColumn + 1; i < grid[currentRow].size(); ++i) {
		if (grid[currentRow][i] == '?') {

			grid[currentRow][i] = c;
			lastCol = i;
		} else
			break;
	}
	for (int i = currentColumn - 1; i >= 0; --i) {
		if (grid[currentRow][i] == '?') {

			grid[currentRow][i] = c;
			firstCol = i;
		} else
			break;
	}

	bool fill = true;
	for (int i = currentRow + 1; i < grid.size(); ++i) {
		for (int j = firstCol; j <= lastCol; ++j) {
			if (grid[i][j] != '?') {
				fill = false;
				break;
			}
		}
		if (fill) {

			for (int j = firstCol; j <= lastCol; ++j) {
				grid[i][j] = c;
			}
		} else
			break;
	}

	fill = true;
	for (int i = currentRow - 1; i >= 0; --i) {
		for (int j = firstCol; j <= lastCol; ++j) {
			if (grid[i][j] != '?') {
				fill = false;
				break;
			}
		}
		if (fill) {

			for (int j = firstCol; j <= lastCol; ++j) {
				grid[i][j] = c;
			}
		} else
			break;
	}
}

void completeCake(vector<string>& grid, int rows, int columns) {

	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < columns; ++j) {

			if ((grid[i][j] != '?') && (used.find(grid[i][j]) == used.end())) {

				expandChar(grid, i, j);
				used.insert(grid[i][j]);
			}

		}

	}
}

int main(int argc, char* argv[]) {


	int testCases = 0;
	cin >> testCases;


	for (int i = 0; i < testCases; i++) {

		int rows, columns;
		vector<string> grid;
		cin >> rows >> columns;

		for (int j = 0; j < rows; ++j) {
			string aux;
			cin >> aux;
			grid.push_back(aux);
		}

		completeCake(grid, rows, columns);

		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < rows; ++j) {
			cout << grid[j] << endl;
		}

		used.clear();
	}
}