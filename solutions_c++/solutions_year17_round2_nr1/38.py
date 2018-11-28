#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int d, n;
		scanf("%d %d", &d, &n);
		
		long double p = 0.0;
		for (int i = 0; i < n; i++) {
			int k, s;
			scanf("%d %d", &k, &s);
			
			p = max(p, (long double)(d - k) / s);
		}
		
		printf("Case #%d: %.15lf\n", t, (double)(d / p));
	}

	return 0;
}
