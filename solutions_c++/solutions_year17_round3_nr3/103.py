#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int n, k;
double u;
double p[55];

inline int sgn(double x) {
	if (fabs(x) < 1e-8) {
		return 0;
	} else {
		if (x > 0.0) {
			return 1;
		} else {
			return -1;
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &k);
		scanf("%lf", &u);
		for (int i = 0; i < n; ++ i) {
			scanf("%lf", &p[i]);
		}
		if (n == k) {
			sort(p, p + n);
			for (int i = 0; i < n && sgn(u) > 0; ) {
				int j = i;
				while (j < n && sgn(p[i] - p[j]) == 0) ++ j;
				double up;
				if (j == n) {
					up = 1.0;
				} else {
					up = p[j];
				}
				if (sgn(u - (up - p[i]) * (j - i)) >= 0) {
					for (int k = i; k < j; ++ k) {
						u -= (up - p[k]);
						p[k] = up;
					}
				} else {
					double delta = u / (j - i);
					for (int k = i; k < j; ++ k) {
						u -= delta;
						p[k] += delta;
					}
					break;
				}
			}
			double ans = 1.0;
			for (int i = 0; i < n; ++ i) {
				ans *= p[i];
			}
			printf("Case #%d: %.12lf\n", kase, ans);
		}
	}
	return 0;
}
