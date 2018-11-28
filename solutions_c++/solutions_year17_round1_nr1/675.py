#include <cstdio>
using namespace std;

char grid[30][30];	/* Oops */
int pos[30];
bool flag[30];
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int R, C;
		scanf("%d%d", &R, &C);
		for (int r = 0; r < R; ++r) scanf("%s", grid[r]);
		for (int r = 0; r < R; ++r) {
			int cnt = 0;
			for (int c = 0; c < C; ++c) if (grid[r][c] != '?')
				pos[cnt++] = c;
			if (cnt) {
				flag[r] = true;
				pos[cnt] = C;
				for (int i = 0; i < cnt; ++i) {
					for (int c = pos[i]; c < pos[i+1]; ++c)
						grid[r][c] = grid[r][pos[i]];
				}
				for (int c = 0; c < pos[0]; ++c)
					grid[r][c] = grid[r][pos[0]];
			} else flag[r] = false;
		}
		int cur = -1;
		for (int r = 0; r < R; ++r) if (flag[r]) { cur = r; break; }
		printf("Case #%d:\n", t);
		for (int r = 0; r < R; ++r) {
			if (flag[r]) cur = r;
			printf("%s\n", grid[cur]);
		}
	}
}
