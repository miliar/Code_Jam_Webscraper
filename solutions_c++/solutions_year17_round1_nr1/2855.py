#include <stdio.h>

int x[4] = {-1, 0, 1, 0}, y[4] = {0, 1, 0, -1}, k, l, r, u, d; char c[30][30], C;

int DFS(int i, int j, char C) {
	for (c[i][j] += 'a'-'A', l > j && (l = j), r < j && (r = j), u > i && (u = i), d < i && (d = i), k = 0; k != 4; k++)
		c[i+x[k]][j+y[k]] == C && DFS(i+x[k], j+y[k], C);
}

int main() {
	int T, N, M, i, j, t = 1, p, q, s, f, e, w;
	for (scanf("%d", &T); T--; ) {
		for (scanf("%d%d", &N, &M), i = 1; i <= N; i++)
			scanf("%s", c[i]+1);
		for (C = '?', i = 1; i <= N; i++)
			for (j = 1; j <= M; j++)
				if ('A' <= c[i][j] && c[i][j] <= 'Z') {
					for (C = c[i][j], l = u = 30, r = d = 0, DFS(i, j, C), p = u; p <= d; p++)
						for (q = l; q <= r; q++)
							c[p][q] = C-'A'+'a';
					for (w = 1; w; ) {
						if (w = 0, l-1) {
							for (q = l-1, p = u, s = f = e = 0; p <= d; p++)
								(c[p][q] == '?' || c[p][q] == C) && e++, c[p][q-1] != '?' && c[p][q-1] && (c[p][q-1] == C ? s++ : f++);
							if (e == d-u+1 && (!s || s && !f))
								for (w++, q = --l, p = u; p <= d; p++)
									c[p][q] = C-'A'+'a';
						}
						if (r < M) {
							for (q = r+1, p = u, s = f = e = 0; p <= d; p++)
								(c[p][q] == '?' || c[p][q] == C) && e++, c[p][q+1] != '?' && c[p][q+1] && (c[p][q+1] == C ? s++ : f++);
							if (e == d-u+1 && (!s || s && !f))
								for (w++, q = ++r, p = u; p <= d; p++)
									c[p][q] = C-'A'+'a';
						}
						if (u-1) {
							for (p = u-1, q = l, s = f = e = 0; q <= r; q++)
								(c[p][q] == '?' || c[p][q] == C) && e++, c[p-1][q] != '?' && c[p-1][q] && (c[p-1][q] == C ? s++ : f++);
							if (e == r-l+1 && (!s || s && !f))
								for (w++, p = --u, q = l; q <= r; q++)
									c[p][q] = C-'A'+'a';
						}
						if (d < N) {
							for (p = d+1, q = l, s = f = e = 0; q <= r; q++)
								(c[p][q] == '?' || c[p][q] == C) && e++, c[p+1][q] != '?' && c[p+1][q] && (c[p+1][q] == C ? s++ : f++);
							if (e == r-l+1 && (!s || s && !f))
								for (w++, p = ++d, q = l; q <= r; q++)
									c[p][q] = C-'A'+'a';
						}
					}
				}
		for (printf("Case #%d:\n", t++), i = 1; i <= N; puts(""), i++)
			for (j = 1; j <= M; j++)
				printf("%c", c[i][j]-'a'+'A');
	}
}
