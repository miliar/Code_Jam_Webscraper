#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

double p[100];

int main() {
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ca++);
		int n, k;
		scanf("%d%d", &n, &k);
		double u;
		scanf("%lf", &u);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &p[i]);
		}
		sort(p, p + n);
		int len = 1;
		while (fabs(u) > 1e-5) {
			if (len == n) {
				for (int i = 0; i < n; i++) p[i] += u / n;
				u = 0;
				continue;
			}
			double use = 0;
			for (int i = 0; i < len; i++) use += p[len] - p[i];
			use = min(use, u);
			for (int i = 0; i < len; i++) p[i] += use / len;
			u -= use;
			for (int i = len; i < n; i++) {
				if (fabs(p[i] - p[i - 1]) < 1e-5) {
					len++;
				} else break;
			}
		}
		double ans = 1;
		for (int i = 0; i < n; i++) {
			ans = ans * p[i];
		}
		printf("%.10lf\n", ans);
	}
}
