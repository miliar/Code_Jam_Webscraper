#include <cstdio>
#include <cmath>
int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		long long int N, K;
		scanf("%lld %lld", &N, &K);

		long long int F = log2(K), W = K - (1<<F);

		long long int len = N - ((1<<F) - 1);
		if(len % (1<<F) > W) len /= (1<<F), len++;
		else len /= (1<<F);
		len--;

		printf("Case #%d: %lld %lld\n", i+1, len-(len>>1), len>>1);
	}
	return 0;
}
