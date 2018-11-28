#include <stdio.h>
#include <algorithm>

void solve() {
	int n, d;
	scanf("%d %d", &d, &n);
	double maxTime = 0.0;
	for (int i = 0; i < n; i++) {
		int k, s;
		scanf("%d %d", &k, &s);
		maxTime = std::max(maxTime, (double)(d - k) / s);
	}
	double res = d / maxTime;
	printf("%f\n", res);
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
