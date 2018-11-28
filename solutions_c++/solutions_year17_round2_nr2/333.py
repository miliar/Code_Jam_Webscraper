#include<stdio.h>
void swap(int &x, int &y) { x ^= y ^= x ^= y; }
void swap(char &x, char &y) { x ^= y ^= x ^= y; }
void ans(int r, int y, int b, char *ans) {
	int A = r, B = y, C = b;
	char X='R', Y='Y', Z='B';
	if (A < B)swap(A, B), swap(X, Y);
	if (B < C)swap(B, C), swap(Y, Z);
	if (A < B)swap(A, B), swap(X, Y);
	if (A > B + C) {
		ans[0] = 0;
		return;
	}
	int l = 0, i;
	for (i = 0; i < A; i++) {
		ans[i * 2] = X;
		if (B < C) {
			ans[i * 2 + 1] = Z;
			C--;
			l = 2;
		}
		else {
			ans[i * 2 + 1] = Y;
			B--;
			l = 1;
		}
	}
	i = i * 2;
	while (B + C > 0) {
		if (l == 1) {
			l = 2;
			C--;
			ans[i++] = Z;
		}
		else {
			l = 1;
			B--;
			ans[i++] = Y;
		}
	}
	ans[i] = 0;
}
void solve() {
	int n, r, o, y, g, b, v;
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
	char *x = new char[n + 10];
	ans(r, y, b, x);
	if(x[0] != NULL) printf("%s\n", x);
	else printf("IMPOSSIBLE\n");
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

//roygbv