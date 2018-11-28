#include <stdio.h>

long long d[63];
void init() {
	d[0] = 1;
	for (int i = 1; i < 63; i++) {
		d[i] = 2 * d[i - 1];
	}
}

int find(long long k) {
	for (int i = 0; i < 63; i++) {
		if (d[i] > k) {
			return i - 1;
		}
	}
	return -1;
}

int main() {
	int T;
	init();
	scanf("%d", &T);
	int count = 1;
	long long K, N;
	while(scanf("%lld%lld", &N, &K) != EOF) {
		int hf = find(N + 1);
		long long m = d[hf] - 1;
		long long k = N - m;
		int h = find(K) + 1;
		long long p = K - (d[h - 1] - 1);
		if (hf < h) {
			printf("Case #%d: 0 0\n", count++);
			continue;
		}
		long long n = d[hf - h] - 1;
		long long node_n = d[h - 1];
		long long x = k / 2 / node_n;
		k -= 2 * node_n * x;
		if (k <= node_n) {
			if (k >= p) {
				printf("Case #%d: %lld %lld\n", count++, n + x + 1, n + x);
			}
			else {
				printf("Case #%d: %lld %lld\n", count++, n + x, n + x);
			}
		}
		else {
			k -= node_n;
			if (k >= p) {
				printf("Case #%d: %lld %lld\n", count++, n + x + 1, n + x + 1);
			}
			else {
				printf("Case #%d: %lld %lld\n", count++, n + x + 1, n + x);
			}
		}
	}
}