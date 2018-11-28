#include<stdio.h>
int in[101][101];
long long d[101][101];
long double t[101][101];
int e[101], s[101];
void solve() {
	int n, q, x, y;
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; i++)scanf("%d%d", e + i, s + i);
	for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) {
		scanf("%d", &in[i][j]);
	}
	for (int i = 1; i <= n; i++)for (int j = 1; j <= n; j++) {
		if (in[i][j] == -1) d[i][j] = 100000000000000ll;
		else d[i][j] = in[i][j];
	}
	for (int k = 1; k <= n; k++)for (int i = 1; i <= n; i++)for (int j = 1; j <= n; j++) {
		if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
	}
	for (int i = 1; i <= n; i++) for(int j=1; j<=n; j++) {
		if (e[i] >= d[i][j]) t[i][j] = (long double)d[i][j] / s[i];
		else t[i][j] = 1e12;
	}
	for (int k = 1; k <= n; k++)for (int i = 1; i <= n; i++)for (int j = 1; j <= n; j++) {
		if (t[i][j] > t[i][k] + t[k][j]) t[i][j] = t[i][k] + t[k][j];
	}
	for (int i = 1; i <= q; i++) {
		scanf("%d%d", &x, &y);
		printf("%.10Lf ", t[x][y]);
	}
	printf("\n");
	return;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		solve();
	}
	return 0;
}