#include <stdio.h>
#include <stdlib.h>

void solve(int cas, int R, int C, char **cake) {
	// to back
	for (int i = 0; i < R; ++i) {
		char c = '?';
		for (int j = C - 1; j >= 0; --j) {
			if (cake[i][j] != '?') {
				c = cake[i][j];
				continue;
			} else if (c == '?') {
				continue;
			} else {
				cake[i][j] = c;
			}
		}
	}
	// to front
	for (int i = 0; i < R; ++i) {
		char c = '?';
		for (int j = 0; j < C; ++j) {
			if (cake[i][j] != '?') {
				c = cake[i][j];
				continue;
			} else if (c == '?') {
				continue;
			} else {
				cake[i][j] = c;
			}
		}
	}
	// to upper
	for (int i = 0; i < C; ++i) {
		char c = '?';
		for (int j = R - 1; j >= 0; --j) {
			if (cake[j][i] != '?') {
				c = cake[j][i];
				continue;
			} else if (c == '?') {
				continue;
			} else {
				cake[j][i] = c;
			}
		}
	}
	// to lower
	for (int i = 0; i < C; ++i) {
		char c = '?';
		for (int j = 0; j < R; ++j) {
			if (cake[j][i] != '?') {
				c = cake[j][i];
				continue;
			} else if (c == '?') {
				continue;
			} else {
				cake[j][i] = c;
			}
		}
	}
	printf("Case #%d:\n", cas);
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			printf("%c", cake[i][j]);
		}
		printf("\n");
	}
}

int main(int argc, char *argv[]) {
	int total;
	scanf("%d", &total);
	for (int i = 0; i < total; i++) {
		int R, C;
		char **cake;
		scanf("%d %d\n", &R, &C);
		cake = (char**) malloc(R * sizeof(char*));
		for (int j = 0; j < R; ++j) {
			cake[j] = (char*) malloc(C * sizeof(char));
		}
		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) {
				scanf("%c", &cake[j][k]);
			}
			scanf("\n");
		}
		solve(i + 1, R, C, cake);
	}
	return 0;
}