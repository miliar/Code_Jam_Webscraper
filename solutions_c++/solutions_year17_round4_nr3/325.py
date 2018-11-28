#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;

int T;
int R, C;
char G[100][100];
int cas;

int g[100][100];

int see(int vx, int vy)
{
	int x = 1;
	for (int i = vx-1; i >= 0; i--) {
		if (G[i][vy] == '|' || G[i][vy] == '-') {
			x = 0;
			break;
		} else if (G[i][vy] == '#') {
			break;
		}
	}

	for (int i = vx+1; i < R; i++) {
		if (G[i][vy] == '|' || G[i][vy] == '-') {
			x = 0;
			break;
		} else if (G[i][vy] == '#') {
			break;
		}
	}

	int y = 1;
	for (int j = vy-1; j >= 0; j--) {
		if (G[vx][j] == '|' || G[vx][j] == '-') {
			y = 0;
			break;
		} else if (G[vx][j] == '#'){
			break;
		}
	}

	for (int j = vy+1; j < C; j++) {
		if (G[vx][j] == '|' || G[vx][j] == '-') {
			y = 0;
			break;
		} else if (G[vx][j] == '#'){
			break;
		}
	}

	if (x == 0 && y == 0) {
		return -1;
	} else if (x == 0) {
		G[vx][vy] = '-';
		return 0;
	} else if (y == 0) {
		G[vx][vy] = '|';
		return 1;
	} else {
		G[vx][vy] = '-';
		g[vx][vy] = 1;
		return 2;
	}
}

int shoot(int vx, int vy)
{
	for (int j = vy-1; j >= 0; j--) {
		if (G[vx][j] == '-')
			return 0;
		else if (G[vx][j] == '#')
			break;
	}
	for (int j = vy+1; j < C; j++) {
		if (G[vx][j] == '-')
			return 0;
		else if (G[vx][j] == '#')
			break;
	}
	for (int i = vx-1; i >= 0; i--) {
		if (G[i][vy] == '|')
			return 0;
		else if (G[i][vy] == '#')
			break;
	}
	for (int i = vx+1; i < R; i++) {
		if (G[i][vy] == '|')
			return 0;
		else if (G[i][vy] == '#')
			break;
	}

	for (int i = vx+1; i < R; i++) {
		if (G[i][vy] == '-' && g[i][vy] == 1) {
			G[i][vy] = '|';
			g[i][vy] = 0;
			return 0;
		} else if (G[i][vy] == '#')
			break;
	}

	for (int i = vx-1; i >= 0; i--) {
		if (G[i][vy] == '-' && g[i][vy] == 1) {
			G[i][vy] = '|';
			g[i][vy] = 0;
			return 0;
		} else if (G[i][vy] == '#')
			break;
	}

	return -1;
}

void print()
{
	for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					printf("%c", G[i][j]);
				}
				puts("");
			}
}
void solve()
{
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (G[i][j] == '|' || G[i][j] == '-') {
				int se = see(i, j);
				if (se < 0) {
					printf("Case #%d: IMPOSSIBLE\n", cas);
					// print();
					return;
				}
			}
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (G[i][j] == '.') {
				int sh = shoot(i, j);
				if (sh < 0) {
					printf("Case #%d: IMPOSSIBLE\n", cas);
					// print();
					return;
				}
			}
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (G[i][j] == '.') {
				int sh = shoot(i, j);
				if (sh < 0) {
					printf("Case #%d: IMPOSSIBLE\n", cas);
					// print();
					return;
				}
			}
		}
	}


	printf("Case #%d: POSSIBLE\n", cas);
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			printf("%c", G[i][j]);
		}
		puts("");
	}
}

int main()
{
	scanf(" %d", &T);

	for (cas = 1; cas <= T; cas++) {
		scanf(" %d %d", &R, &C);
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				scanf(" %c", &G[i][j]);
				g[i][j] = 0;
			}
		}
		solve();
	}

	return 0;
}