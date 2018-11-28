#include <stdio.h>
#include <map>
#include <string.h>
using namespace std;

char m[27][27];
bool all_null(char *s) {
	for (int i = 0; i < strlen(s); i++) {
		if (s[i] != '?') return false;
	}
	return true;
}
void fill_map(int r1, int c1, int r2, int c2, const char c) {
	for (int i = r1; i <= r2; i++) {
		for (int j = c1; j <= c2; j++) {
			m[i][j] = c;
		}
	}
}
int main(void) {
	freopen("c:\\cdj\\AL0.in", "r", stdin);
	freopen("c:\\cdj\\AL0.txt", "w", stdout);
	int T; scanf("%d\n", &T);
	for (int tc = 1; tc <= T; tc++) {
		int R, C; scanf("%d %d\n", &R, &C);
		for (int i = 0; i < R; i++) {
			scanf("%s\n", m[i]);
		}
		int from_row = 0;
		for (int i = 0; i < R; i++) {
			if (all_null(m[i])) {
				continue;
			}
			else {
				int from_column = 0;
				for (int j = 0; j < C; j++) {
					if (m[i][j] != '?') {
						fill_map(from_row, from_column, i, j, m[i][j]);
						from_column = j + 1;
					}
				}
				
				fill_map(from_row, from_column, i, C-1, m[i][from_column-1]);
				from_row = i + 1;
			}
		}
		for (int j = 0; j < C; j++) {
			fill_map(from_row, j, R - 1, j, m[from_row - 1][j]);
		}
		printf("Case #%d:\n", tc);
		for (int i = 0; i < R; i++) {
			
			printf("%s\n", m[i]);
		
		}
	}

}