#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T;
    long long int N, K, min, max;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%lld %lld", &N, &K);
		min = N;
		while (K > 0) {
			if (K & 1) {
				max = min >> 1;
				min = (min - 1) >> 1;
			} else {
				min = min >> 1;
			}
			K = K >> 1;
		}
		printf("Case #%d: %lld %lld\n", i + 1, max, min);
	}
	return 0;
}

