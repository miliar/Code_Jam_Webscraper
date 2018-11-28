#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		long long N, K;
		scanf("%lld%lld", &N, &K);

		int level = 0;
		long long cur = 0;
		while (1) {
			if (cur + (1LL<<level) >= K)
				break;
			cur += 1LL<<level;
			++level;
		}

		long long big = N/(1LL<<level);
		long long num = (N-cur) - (big-1)*(1LL<<level);

		printf("Case #%d: ", tt);
		if (K-cur <= num) {
			long long a = (big-1)/2, b = big-1-a;
			printf("%lld %lld\n", max(a, b), min(a, b));
		}
		else {
			long long a = (big-2)/2, b = big-2-a;
			printf("%lld %lld\n", max(a, b), min(a, b));
		}
	}

	return 0;
}
