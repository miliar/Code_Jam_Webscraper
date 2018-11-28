#include <cstdio>

int TC;
int R, C;
char A[30][30];

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) {
			scanf("%s", A[i]);
		}
		for (int i = 0; i < R; ++i) {
			char x = '?';
			for (int j = 0; j < C; ++j) {
				if (A[i][j] == '?') {
					A[i][j] = x;
				} else {
					x = A[i][j];
				}
			}
			x = '?';
			for (int j = C - 1; j >= 0; --j) {
				if (A[i][j] == '?') {
					A[i][j] = x;
				} else {
					x = A[i][j];
				}
			}
		}
		for (int j = 0; j < C; ++j) {
			char x = '?';
			for (int i = 0; i < R; ++i) {
				if (A[i][j] == '?') {
					A[i][j] = x;
				} else {
					x = A[i][j];
				}
			}
			x = '?';
			for (int i = R - 1; i >= 0; --i) {
				if (A[i][j] == '?') {
					A[i][j] = x;
				} else {
					x = A[i][j];
				}
			}
		}
		printf("Case #%d:\n", tc);
		for (int i = 0; i < R; ++i) {
			printf("%s\n", A[i]);
		}
	}
	return 0;
}

