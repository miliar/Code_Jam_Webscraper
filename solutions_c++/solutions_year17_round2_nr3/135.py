#include <cstdio>

int a[101], b[101];
long long c[101][101];
double d[101][101];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		int i, j, k, n, m;
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i++) scanf("%d%d", &a[i], &b[i]);
		for (i = 1; i <= n; i++) for (j = 1; j <= n; j++) scanf("%lld", &c[i][j]);
		for (k = 1; k <= n; k++) for (i = 1; i <= n; i++) for (j = 1; j <= n; j++)
			if (c[i][k] != -1 && c[k][j] != -1 && (c[i][j] == -1 || c[i][j] > c[i][k] + c[k][j]))
				c[i][j] = c[i][k] + c[k][j];
		for (i = 1; i <= n; i++) for (j = 1; j <= n; j++) d[i][j] = c[i][j] != -1 && c[i][j] <= a[i] ? 1.* c[i][j] / b[i] : -1;
		for (k = 1; k <= n; k++) for (i = 1; i <= n; i++) for (j = 1; j <= n; j++)
			if (d[i][k] != -1 && d[k][j] != -1 && (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]))
				d[i][j] = d[i][k] + d[k][j];
		printf("Case #%d:", T);
		while (m--) {
			scanf("%d%d", &i, &j);
			printf(" %.12f", d[i][j]);
		}
		puts("");
	}
}