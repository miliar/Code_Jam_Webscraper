#include<stdio.h>
char in[1100];
void solve() {
	int k, n, c = 0;
	scanf("%s%d", in, &k);
	for (n = 0; in[n]; n++) in[n] = (in[n] == '+');
	for (int i = 0; i <= n - k; i++) {
		if (in[i] == 0) {
			c++;
			for (int j = 0; j < k; j++) in[i + j] = !in[i + j];
		}
	}
	for (int i = n - k + 1; i < n; i++) if (in[i] == 0) {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("%d\n", c);
	return;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++) {
		printf("Case #%d: ", TT);
		solve();
	}
	return 0;
}