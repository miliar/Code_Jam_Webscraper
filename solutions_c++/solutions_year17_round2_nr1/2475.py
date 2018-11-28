#include <bits/stdc++.h>
using namespace std;
typedef pair<double, double> dd;
const int N = 1e3 + 10;

int n;
dd v[N];
double finish;

bool valid (const double &mid) {
	for (int i = 0; i < n; ++i) {
		double a = (finish - v[i].first) / v[i].second;
		double b = finish / mid;
		if (b < a)
			return false;
	}
	return true;
}

int main () {
	int test; scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		scanf("%lf %d", &finish, &n);
		for (int i = 0; i < n; ++i)
			scanf("%lf %lf", &v[i].first, &v[i].second);
		double lo = 0, hi = 1e18;
		for (int i = 0; i < 500; ++i) {
			double mid = (lo + hi) / 2.0;
			if (valid(mid))
				lo = mid;
			else
				hi = mid;
		}
		printf("Case #%d: %.6lf\n", t, lo);
	}
	return 0;
}