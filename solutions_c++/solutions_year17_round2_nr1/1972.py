#include <bits/stdc++.h>
using namespace std;

typedef double ff;
int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		int d, n;
		scanf("%d%d", &d, &n);
		ff tmax = 0;
		for (int j = 0; j < n; ++j) {
			int k, s;
			scanf("%d%d", &k, &s);
			tmax = max(tmax, (ff)(d - k) / s);
		}
		double ans = (ff)d / tmax;
		cout.precision(7);
		cout << "Case #" << (i + 1) << ": " << fixed << ans << endl;
	}
	return 0;
}
