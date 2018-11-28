#include<stdio.h>
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		int n, d, k, s;
		long double m = 0;
		scanf("%d%d", &d, &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d%d", &k, &s);
			long double t = (long double)(d - k) / s;
			if (m < t) m = t;
		}
		printf("Case #%d: %.10Lf\n", tt, d / m);
	}
	return 0;
}