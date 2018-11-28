#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 7;

int n, pos[N], d, s[N];

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		scanf("%d %d", &d, &n);
		double ans = 1e100;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &pos[i], &s[i]);
			double t = 1. * (d - pos[i]) / s[i];
			ans = min(ans, pos[i] / t + s[i]);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
