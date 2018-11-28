#include <bits/stdc++.h>
using namespace std;
int T, R, C;
char s[30][30];
int sum[30][30];
bool ban[30][30];
int getsum(int x1, int y1, int x2, int y2) {
	return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1];
}
void refresh() {
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + (s[i][j] - '?');
		}
	}
}
int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase) {
		scanf("%d%d", &R, &C);
		memset(ban, 0, sizeof ban);
		for (int i = 1; i <= R; ++i) scanf("%s", s[i] + 1);
		for (int i = 1; i <= R; ++i) for (int j = 1; j <= C; ++j) {
			if (ban[i][j]) continue;
			if (s[i][j] != '?') {
				refresh();
				int x1 = i, y1 = j, x2 = i, y2 = j;
				while (x1 > 1 && y1 > 1 && getsum(x1 - 1, y1 - 1, x2, y2) == s[i][j] - '?') --x1, --y1;
				while (x1 > 1 && y2 < C && getsum(x1 - 1, y1, x2, y2 + 1) == s[i][j] - '?') --x1, ++y2;
				while (x2 < R && y1 > 1 && getsum(x1, y1 - 1, x2 + 1, y2) == s[i][j] - '?') ++x2, --y1;
				while (x2 < R && y2 < C && getsum(x1, y1, x2 + 1, y2 + 1) == s[i][j] - '?') ++x2, ++y2;
				while (x1 > 1 && getsum(x1 - 1, y1, x2, y2) == s[i][j] - '?') --x1;
				while (x2 < R && getsum(x1, y1, x2 + 1, y2) == s[i][j] - '?') ++x2;
				while (y1 > 1 && getsum(x1, y1 - 1, x2, y2) == s[i][j] - '?') --y1;
				while (y2 < C && getsum(x1, y1, x2, y2 + 1) == s[i][j] - '?') ++y2;
				for (int k = x1; k <= x2; ++k) for (int l = y1; l <= y2; ++l) s[k][l] = s[i][j], ban[k][l] = true;
			}
		}
		printf("Case #%d:\n", kase);
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) putchar(s[i][j]);
			putchar('\n');
		}
	}
	return 0;
}
