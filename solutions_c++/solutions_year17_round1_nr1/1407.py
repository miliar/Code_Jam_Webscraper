#include <cstdio>

char s[30][30];
int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		int r, c, i, j, k;
		char ind;
		scanf("%d%d", &r, &c);
		for (i = 0; i < r; i++) scanf("%s", &s[i]);

		for (i = 0; i < r; i++) {
			for (j = 0; j < c; j++) {
				if (s[i][j] != '?') {
					for (k = j-1; k >= 0; k--) {
						if (s[i][k] == '?') s[i][k] = s[i][j];
						else break;
					}
					for (k = j + 1; k <c; k++) {
						if (s[i][k] == '?') s[i][k] = s[i][j];
						else break;
					}
				}
			}
		}

		for (j = 0; j < c; j++) {
			for (i = 0; i < r; i++) {
				if (s[i][j] != '?') {
					for (k = i - 1; k >= 0; k--) {
						if (s[k][j] == '?') s[k][j] = s[i][j];
						else break;
					}
					for (k = i + 1; k <r; k++) {
						if (s[k][j] == '?') s[k][j] = s[i][j];
						else break;
					}
				}
			}
		}
		printf("Case #%d:\n", t);
		for (i = 0; i < r; i++) printf("%s\n", s[i]);

	}

	return 0;
}