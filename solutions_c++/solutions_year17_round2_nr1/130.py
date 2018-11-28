#include <cstdio>

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		double a, b, n, r = 0;
		int i, m;
		scanf("%lf%d", &n, &m);
		while (m--) {
			scanf("%lf%lf", &a, &b);
			a = (n - a) / b;
			if (a > r) r = a;
		}
		printf("Case #%d: %.12f\n", T, n / r);
	}
}