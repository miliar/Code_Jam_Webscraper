#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T, D, N;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d", &D, &N);
		double maxTime = 0.0;
		int K, S;
		for (int i = 0; i < N; i++) {
			scanf("%d %d", &K, &S);
			double time = (double)(D - K)/(double)S;
			if (time > maxTime) maxTime = time;
		}
		printf("Case #%d: %lf\n", t + 1, (double)D/maxTime);
	}
	return 0;
}

