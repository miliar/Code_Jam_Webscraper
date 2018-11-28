#include <cstdio>

int d[111][111][111];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		int x, y, z, r = 0;
		int i, j, k, l, m, n;
		scanf("%d%d", &n, &m);
		x = y = z = 0;
		while (n--) {
			scanf("%d", &i);
			if (i % m == 0) r++;
			if (i % m == 1) x++;
			if (i % m == 2) y++;
			if (i % m == 3) z++;
		}
		for (i = 0; i <= x; i++) for (j = 0; j <= y; j++) for (k = 0; k <= z; k++) d[i][j][k] = 0;
		for (i = 0; i <= x; i++) for (j = 0; j <= y; j++) for (k = 0; k <= z; k++) {
			if ((i + j + j + k * 3) % m == 0) l = d[i][j][k] + 1;
			else l = d[i][j][k];
			if (d[i + 1][j][k] < l) d[i + 1][j][k] = l;
			if (d[i][j + 1][k] < l) d[i][j + 1][k] = l;
			if (d[i][j][k + 1] < l) d[i][j][k + 1] = l;
		}
		printf("Case #%d: %d\n", T, d[x][y][z] + r);
	}
}