#include<stdio.h>
int in[1001][2];
int d[2][8], n, c;
int cx[1001], cy[1001];
void solve() {
	int m, x, y;
	scanf("%d%d%d", &n, &c, &m);
	for (int i = 0; i <= c; i++) cy[i] = 0;
	for (int i = 0; i <= n; i++) cx[i] = 0;
	for (int i = 1; i <= m; i++) {
		scanf("%d%d", &x, &y);
		in[x][y]++;
		cx[x]++;
		cy[y]++;
	}
	int a = 0;
	for (int i = 1; i <= c; i++) if (a < cy[i]) a = cy[i];
	int b = 0, s=0;
	for (int i = 1; i <= n; i++) {
		s += cx[i];
		int t = s / i; if (s%i != 0) t++;
		if (t > a) a = t;
	}
	for (int i = 1; i <= n; i++) {
		if (cx[i] > a) b += cx[i] - a;
	}
	printf("%d %d\n", a, b);
	return ;
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