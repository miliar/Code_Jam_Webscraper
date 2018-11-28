#include <cstdio>
#include <iostream>
#include <set>
using namespace std;
int T;
long long N, K;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%lld%lld", &N, &K);
		long long r = 2;
		long long a = N, b = N;
		long long p1 = 1, p2 = 0;
		while (r - 1 < K) {
			r *= 2;
			long long c1 = 0, c2 = 0;
			if (a % 2 == 0) {
				c1 += p1, c2 += p1;
			}
			else {
				c1 += p1 + p1;
			}
			if (b % 2 == 0) {
				c1 += p2, c2 += p2;
			}
			else {
				c2 += p2 + p2;
			}
			p1 = c1, p2 = c2;
			a = a / 2;
			b = (b - 1) / 2;
		}
		r = r / 2 - 1;
		if (K - r <= p1) {
			printf("Case #%d: %lld %lld\n", t, a / 2, (a - 1) / 2);
		}
		else {
			printf("Case #%d: %lld %lld\n", t, b / 2, (b - 1) / 2);
		}
	}

}