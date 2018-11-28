#include <iostream>
#include <vector>

using namespace std;

int main() {
	int test_cases;
	cin >> test_cases;

	for (int t = 1; t <= test_cases; t++) {
		int r, c;
		cin >> r >> c;
		vector<vector<char>> grid(r, vector<char>(c));
		vector<vector<char>> output_grid(r, vector<char>(c));

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> grid[i][j];
			}
		}

		pair<int,int> top_left = {0,0};
		int current_row, current_column;
		int next_row;
		pair<int,int> next_row_point;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (grid[i][j] != '?') {
					next_row = i;
					next_row_point = {i, j};
					goto next1;
				}
			}
		}
		next1:

		while (next_row < r) {
			current_row = next_row;
			current_column = next_row_point.second;
			char current  = grid[current_row][current_column];
			
			//find next row point:
			next_row = r;
			next_row_point = {r, 0};
			for (int i = current_row+1; i < r; i++) {
				for (int j = 0; j < c; j++) {
					if (grid[i][j] != '?') {
						next_row = i;
						next_row_point = {i, j};
						goto next2;
					}
				}
			}
			next2:

			for (int j = current_column+1; j < c; j++) {
				if (grid[current_row][j] != '?') {
					for (int k = top_left.first; k < next_row; k++) {
						for (int l = top_left.second; l < j; l++) {
							output_grid[k][l] = current;
						}
					}
					top_left.second = j;
					current = grid[current_row][j];
				}
			}
			for (int k = top_left.first; k < next_row; k++) {
				for (int l = top_left.second; l < c; l++) {
					output_grid[k][l] = current;
				}
			}
			
			top_left = {next_row, 0};
		}

		cout << "Case #" << t << ":\n";
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << output_grid[i][j];
			}
			cout << endl;
		}

	}
}