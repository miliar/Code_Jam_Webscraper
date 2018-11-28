#include <cstdio>

long long pow10[19] = {1};

int getDigit(long long x, int y) {
	return (x / pow10[y]) % 10;
}

long long solve(long long N) {
	int i, j = 18;
	for (i = 17; i >= 0; --i) {
		if (getDigit(N, i + 1) > getDigit(N, i)) break;
		if (getDigit(N, i + 1) < getDigit(N, i)) j = i;
	}
	return i < 0 ? N : (N / pow10[j]) * pow10[j] - 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	for (int i = 1; i <= 18; ++i) pow10[i] = pow10[i - 1] * 10;
	int T;
	long long N;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%lld", &N);
		printf("Case #%d: %lld\n", t, solve(N));
	}
	return 0;
}
