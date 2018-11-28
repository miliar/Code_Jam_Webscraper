#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T, R, C;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d %d", &R, &C);
		char grid[25][25] = {};
		for (int j = 0; j < R; j++) {
			scanf("%s", &grid[j]);
		}
		for (int r = 0; r < R; r++) {
			for (int c = 1; c < C; c++) {
				if (grid[r][c] == '?') {
					grid[r][c] = grid[r][c - 1];
				}
			}
			if (grid[r][0] == '?') {
				if (grid[r][C - 1] != '?') {
					for (int c = C - 2; c >= 0; c--) {
						if (grid[r][c] == '?') {
							grid[r][c] = grid[r][c + 1];
						}
					}
				} else if (r != 0 && grid[r - 1][0] != '?') {
					for (int c = 0; c < C; c++) {
						grid[r][c] = grid[r - 1][c];
					}
				}
			}
		}
		for (int r = R - 2; r >= 0; r--) {
			if (grid[r][0] != '?') {
				continue;
			}
			for (int c = 0; c < C; c++) {
				grid[r][c] = grid[r + 1][c];
			}
		}
		printf("Case #%d:\n", i + 1);
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				printf("%c", grid[r][c]);
			}
			printf("\n");
		}
	}
	return 0;
}

