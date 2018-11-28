#include<stdio.h>
#include<string.h>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		unsigned long long N;
		scanf("%lld", &N);
		int prev = 10;
		for (unsigned long long i = 1; i <= N; i*=10) {
			int cur = N%(i*10) / i;
			if (cur > prev) {
				N = N / (i*10) * (i*10);
				N += (cur-1) * i;
				N += i - 1;
				cur--;
			}
			prev = cur;
		}
		printf("Case #%d: %lld\n", t, N);
	}
	return 0;
}