#include <cstdio>

int T, R, C;
char mat[25][25];
bool finish[26];

// check to finish
bool check(void)
{
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			if (mat[r][c] == '?') {
				return false;
			}
		}
	}
	for (int i = 0; i < 26; i++) {
		if (finish[i] == false) {
			return false;
		}
	}
	return true;
}

void solve(void)
{
	while (!check()) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (mat[r][c] != '?' && finish[mat[r][c] - 'A'] == false) {
					finish[mat[r][c] - 'A'] = true;
					int left, right, up, down;
					int a;
					for (a = c - 1; a >= 0 && mat[r][a] == '?'; a--);
					left = a + 1;
					for (a = c + 1; a < C && mat[r][a] == '?'; a++);
					right = a - 1;


					int b;
					for (b = r - 1; b >= 0 && mat[b][c] == '?'; b--);
					up = b + 1;
					for (b = r + 1; b < R && mat[b][c] == '?'; b++);
					down = b - 1;

					if (right - left > 0) {
						// hori 1st -> 2nd : vert
						int maxup = 0;
						int mindown = R - 1;

						for (int i = left; i <= right; i++) {
							int k;
							for (k = r - 1; k >= 0 && mat[k][i] == '?'; k--);
							if (k + 1 > maxup) {
								maxup = k + 1;
							}

							for (k = r + 1; k < R && mat[k][i] == '?'; k++);
							if (k - 1 < mindown) {
								mindown = k - 1;
							}
						}

						for (int i = left; i <= right; i++) {
							for (int k = maxup; k <= mindown; k++) {
								mat[k][i] = mat[r][c];
							}
						}
					}
					else {
						// vert 1st -> 2nd : hori
						int maxleft = 0;
						int minright = C - 1;

						for (int i = up; i <= down; i++) {
							int k;
							for (k = c - 1; k >= 0 && mat[i][k] == '?'; k--);
							if (k + 1 > maxleft) {
								maxleft = k + 1;
							}

							for (k = c + 1; k < C && mat[i][k] == '?'; k++);
							if (k - 1 < minright) {
								minright = k - 1;
							}
						}

						for (int i = up; i <= down; i++) {
							for (int k = maxleft; k <= minright; k++) {
								mat[i][k] = mat[r][c];
							}
						}
					}


				}
			}
		}
	}
}


int main(void)
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		for (int i = 0; i < 26; i++) {
			finish[i] = true;
		}
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; r++) {
			while (getchar() != '\n');
			for (int c = 0; c < C; c++) {
				scanf("%c", &mat[r][c]);
				if (mat[r][c] == '?') {
					continue;
				}
				finish[mat[r][c] - 'A'] = false;
			}
		}

		// run
		solve();
		printf("Case #%d:\n", tc);
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				char ch = '?';
				printf("%c", mat[r][c]);
			}
			printf("\n");
		}
	}
}
