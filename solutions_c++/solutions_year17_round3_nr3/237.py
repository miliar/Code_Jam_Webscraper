#include<cstdio>

int t, n, k;
double u, p[51];
const double eps = 1e-7;

double f(double x) {
	double y = 0;
	for (int i = 0; i < n; i++) if (p[i] < x) y += x - p[i];
	return y;
}

double search(double l, double r) {
	double mid = (l + r) / 2;
	if (l + eps >= r) return mid;
	if (f(mid) > u) return search(l, mid);
	else return search(mid, r);
}

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d %d", &n, &k);
		scanf("%lf", &u);
		for (int i = 0 ; i < n; i++) scanf("%lf", &p[i]);
		double x = search(0, 1), ans = 1;
		for (int i = 0; i < n; i++)
			if (p[i] < x) ans *= x;
			else ans *= p[i];
		printf("Case #%d: %lf\n", test, ans);
	}
}
