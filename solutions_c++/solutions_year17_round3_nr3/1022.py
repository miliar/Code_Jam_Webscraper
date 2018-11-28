#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, t, N, K, n, i;
	double tu, cores[50], ans;
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		ans = 1;
		scanf("%d %d", &N, &K);
		scanf("%lf", &tu);
		for(n = 0; n < N; ++n) {
			scanf("%lf", cores+n);
		}
		sort(cores, cores+N);
		for(n = 1; n < N; ++n) {
			if(cores[n] > cores[n-1]) {
				if(tu / n + cores[n-1] > cores[n]) {
					for(i = 0; i < n; ++i) {
						tu -= cores[n] - cores[i];
						cores[i] = cores[n];
					}
				} else {
					tu = tu / n;
					for(i = 0; i < n; ++i) {
						cores[i] += tu;
					}
					tu = 0;
					break;
				}
			}
		}
		if(tu > 0) {
			tu = tu / N;
			for(i = 0; i < N; ++i) {
				cores[i] += tu;
			}
		}
		for(n = 0; n < N; ++n) {
			cores[n] = min(1.0, cores[n]);
		}
		ans = 1;
		for(n = 0; n < N; ++n) {
			ans *= cores[n];
		}
		printf("Case #%d: %.9lf\n", t+1, ans);
	}
	return 0;
}
