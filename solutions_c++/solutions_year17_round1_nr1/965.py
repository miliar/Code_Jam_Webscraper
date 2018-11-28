#include <iostream>
#include <vector>
#include <numeric>
#include<limits>
#include <random>
#include <iomanip> 
#include <deque>
#include <map>
#include <set>
using namespace std;



int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int row, column;
		cin >> row >> column;
		vector<vector<char>> grid(row, vector<char>(column));
		vector<char> column_first(column, '?');
		for (int i = 0; i < row; ++i)
			for (int j = 0; j < column; ++j) {
				cin >> grid[i][j];
				if (grid[i][j] != '?' && column_first[j] == '?') {
					column_first[j] = grid[i][j];
				}
			}

		for (int j = 0; j < column; ++j) {
			if (column_first[j] != '?') {
				char cur = column_first[j];
				for (int i = 0; i < row; ++i) {
					if (grid[i][j] == '?') {
						grid[i][j] = cur;
					}
					else {
						cur = grid[i][j];
					}
				}
			}
		}
		int idx = 0;
		while (column_first[idx] == '?')
			++idx;

		for (int j = idx; j >= 0; --j) {
			if (column_first[j] == '?') {
				for (int i = 0; i < row; ++i)
					grid[i][j] = grid[i][j + 1];
			}
		}

		for (int j = idx; j < column; ++j) {
			if (column_first[j] == '?') {
				for (int i = 0; i < row; ++i)
					grid[i][j] = grid[i][j - 1];
			}
		}

		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < row; ++i) {
			for (int j = 0; j < column; ++j)
				cout << grid[i][j];
			cout << endl;
		}



	}

	return 0;
}
