#include<stdio.h>
int getd(long long x, long long b) {
	return x / b % 10;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		long long x;
		scanf("%lld", &x);
		for (long long b = 10; b <= x; b *= 10) {
			if (getd(x, b / 10) < getd(x, b)) {
				x = x / b;
				x *= b;
				x--;
			}
		}
		printf("Case #%d: %lld\n", tt, x);
	}
	return 0;
}