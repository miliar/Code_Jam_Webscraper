#include<cstdio>

long long k, s, d;
int n, t;

int main() {
	scanf("%d", &t);
	for (int c = 1; c <= t; c++) {
		scanf("%lld%d", &d, &n);

		double ti = 0;
		for (int i = 0; i < n; i++) {
			scanf("%lld%lld", &k, &s);
			double tmp = (d - k) *1. / s;
			ti = ti > tmp? ti: tmp;
		}

		printf("Case #%d: %lf\n", c, d / ti);
	}
	return 0;
}
