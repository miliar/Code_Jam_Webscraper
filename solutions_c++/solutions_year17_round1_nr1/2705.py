#include <bits/stdc++.h>

using namespace std;

int T, R, C;

char grid[13][13];

int main () {

	scanf("%d\n", &T);

	for (int tt = 0; tt < T; ++tt) {
		scanf("%d %d\n", &R, &C);

		int firstRowEmpty = -1;

		for (int i = 0; i < R; ++i) {
			bool emptyRow = true;
			int pos = 0;
			for (int j = 0; j < C; ++j) {
				scanf("%c", &grid[i][j]);
				if (grid[i][j] == '?') {
					continue;
				} else {
					emptyRow = false;
					while (pos < j) {
						grid[i][pos] = grid[i][j];
						pos++;
					}
					pos = j + 1;
				}
			}

			if (emptyRow) {
				if (firstRowEmpty == i - 1) {
					firstRowEmpty = i;
				}
				while (pos < C && i != 0) {
					grid[i][pos] = grid[i - 1][pos];
					pos++;
				}
			} else {
				int temp = pos;
				while (temp < C) {
					grid[i][temp] = grid[i][pos - 1];
					temp++;
				}
			}
			scanf("\n");
		}

		for (int i = firstRowEmpty; i >= 0; --i) {
			for (int j  = 0; j < C; ++j) {
				grid[i][j] = grid[i + 1][j];
			}
		}

		cout << "Case #" << tt + 1 << ": " << endl; 

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}