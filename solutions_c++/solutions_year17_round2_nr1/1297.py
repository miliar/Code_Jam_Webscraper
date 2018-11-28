#include<cstdio>

int T, d, n;

double max(double x, double y) {
	return x > y ? x : y;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int Test = 1; Test <= T; Test++) {
		scanf("%d %d", &d, &n);
		double tt = 0;
		for (int i = 0; i < n; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			tt = max(tt, 1. * (d - x) / y);
		}
		printf("Case #%d: %lf\n", Test, d / tt);
	}
}
