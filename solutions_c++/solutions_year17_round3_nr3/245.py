#include <bits/stdc++.h>

using namespace std;
const double eps = 1e-11;

int T, n, k;
double rem;
double p[55];

bool check(double x) {
	double tot = 0;
	for (int i = 1; i <= n; i++) {
		if (p[i] < x) tot += x - p[i];
	}
	return tot - eps < rem;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d %d", &n, &k);
		scanf("%lf", &rem);
		for (int i = 1; i <= n; i++) {
			scanf("%lf", &p[i]);
		}
		double l = 0., r = 1.;
		while (l + eps < r) {
			double mid = (l + r) / 2;
			if (check(mid)) {
				l = mid;
			} else r = mid;
		}
		double ans = 1.;
		for (int i = 1; i <= n; i++) {
			double x = p[i];
			if (x < l) x = l;
			ans *= x;
		}
		printf("Case #%d: %.10lf\n", cas, ans);
	}
	

	return 0;
}
