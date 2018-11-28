#include <cstdio>

const int MAXR = 26, MAXC = 26;
int R, C;
char a[MAXR][MAXC];

int findFirstNonempty(int r) {
	for (int i = 0; i < C; ++i)
		if (a[r][i] != '?')
			return i;
	return -1;
}

void solve() {
	int x = 0, y;
	for (x = 0; x < R; ++x)
		if ((y = findFirstNonempty(x)) >= 0) break;
	for (int i = x; i < R; ++i) {
		y = findFirstNonempty(i);
		if (y >= 0) {
			for (int j = 0; j < y; ++j) a[i][j] = a[i][y];
			for (int j = y + 1; j < C; ++j)
				if (a[i][j] == '?') a[i][j] = a[i][j - 1];
		}
		else
			for (int j = 0; j < C; ++j) a[i][j] = a[i - 1][j];
	}
	for (int i = x - 1; i >= 0; --i)
		for (int j = 0; j < C; ++j)
			a[i][j] = a[i + 1][j];
	for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j)
			printf("%c%s", a[i][j], j == C - 1 ? "\n" : "");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i)
			scanf(" %s", a[i]);
		printf("Case #%d:\n", t);
		solve();
	}
	return 0;
}
