#include <stdio.h>
#include <algorithm>

using namespace std;

char cake[50][50];

bool check(char ch, int minx, int miny, int maxx, int maxy) {
	int count = 0;
	for (int i = minx; i <= maxx; ++i) {
		for (int j = miny; j <= maxy; ++j) {
			if (cake[i][j] != ch && cake[i][j] != '?') {
				return false;
			}
			if (cake[i][j] != '?') ++count;
		}
	}
	return count > 0;
}

void solve(int R, int C) {
	for (char ch = 'A'; ch <= 'Z'; ++ch) {
		int min_x = R;
		int max_x = -1;
		int min_y = C;
		int max_y = -1;
		int area = 0;
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				for (int p = i; p < R; ++p) {
					for (int q = j; q < C; ++q) {
						if (check(ch, i, j, p, q) && area < (p - i + 1) * (q - j + 1)) {
							min_x = i;
							max_x = p;
							min_y = j;
							max_y = q;
							area = (p - i + 1) * (q - j + 1);
						}
					}
				}
			}
		}
		//printf("%c %d %d %d %d\n", ch, min_x, max_x, min_y, max_y);
		for (int i = min_x; i <= max_x; ++i) {
			for (int j = min_y; j <= max_y; ++j) {
				cake[i][j] = ch;
			}
		}
	}
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			putchar(cake[i][j]);
		}
		puts("");
	}
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int R, C;
		scanf("%d%d", &R, &C);
		for (int j = 0; j < R; ++j) {
			scanf("%s", cake[j]);
		}
		printf("Case #%d:\n", i);
		solve(R, C);
	}
	return 0;
}
