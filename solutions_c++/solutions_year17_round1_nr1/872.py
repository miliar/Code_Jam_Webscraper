#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

typedef long long ll;

const int MAX_R = 25, MAX_C = 25;

int T, R, C;

char grid[MAX_R + 1][MAX_C + 1];

void print_grid() {
	FOR(i, 0, R) {
		printf("\n%s", grid[i]);
	}
}

char first_char(int row) {
	FOR(i, 0, C) {
		if (grid[row][i] != '?') {
			return grid[row][i];
		}
	}
	return '?';
}

int find_first_non_empty_row() {
	FOR(i, 0, R) {
		FOR(j, 0, C) {
			if (grid[i][j] != '?') {
				return i;
			}
		}
	}
	return -1;
}

int main()
{
	// freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("r1a_a.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		scanf("%d %d", &R, &C);
		
		FOR(i, 0, R) {
			scanf("%s", grid[i]);
		}
		
		int first_non_empty_row = find_first_non_empty_row();
		
		FOR(i, first_non_empty_row, R) {
			char c = first_char(i);
			
			if (c == '?') {
				FOR(j, 0, C) {
					grid[i][j] = grid[i - 1][j];
				}
			}
			else {
				FOR(j, 0, C) {
					if (grid[i][j] != '?') c = grid[i][j];
					grid[i][j] = c;
				}
			}
		}
		
		// fill first empty rows
		RFOR(i, 0, first_non_empty_row) {
			FOR(j, 0, C) {
				grid[i][j] = grid[i + 1][j];
			}
		}

		printf("Case #%d: ", t);
		print_grid();
		printf("\n");
	}
	return 0;
}
