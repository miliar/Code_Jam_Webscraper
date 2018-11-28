#include <bits/stdc++.h>
using namespace std;

int tc;
int main() {
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		long long D, N;
		scanf("%lld%lld", &D, &N);

		double m = -1;
		for (int i=0; i<N; ++i) {
			long long k, s;
			scanf("%lld%lld", &k, &s);
			m = max(m, (double)(D-k)/s);
		}
		
		printf("Case #%d: %.10lf\n", tt, D/m);
	}

	return 0;
}
