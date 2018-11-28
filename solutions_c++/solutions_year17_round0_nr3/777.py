#include <stdio.h>
#include <algorithm>
#include <string.h>

void solve() {
	long long int N, K; scanf("%lld%lld", &N, &K);

	long long int m = 1;
	for (; (m << 1) <= K; m <<= 1);

	long long int div = (N - m + 1) / m;
	long long int ones = (N - m + 1) - (N - m + 1) / m * m;

	long long int width = div + (ones >= (K ^ m) + 1);
	width--;

	printf("%lld %lld\n", (width >> 1) + (width & 1), width >> 1);
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}