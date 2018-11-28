#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int main() {
	int T; scanf("%d", &T);
	for (int kk = 1; kk <= T; kk++) {
		double d; int n;
		scanf("%lf%d", &d, &n);
		double ans = 100000000000000.0;
		for (int i = 0; i < n; i++) {
			double k, s;
			scanf("%lf%lf", &k, &s);
			double tmp = (d - k) / s;
			ans = min(ans, d / tmp);
		}
		printf("Case #%d: %.6f\n", kk, ans);
	}
	return 0;
}