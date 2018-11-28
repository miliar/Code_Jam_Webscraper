#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Pancake {
	long long int R;
	long long int H;
};
int cmp(const void *a, const void *b) {
	struct Pancake *aa = (Pancake *)a;
	struct Pancake *bb = (Pancake *)b;
	return (bb->R * bb->H) - (aa->R * aa->H);
}
int main() {
	int T, N, K;
	double pi = acos(-1.0);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d", &N, &K);
		struct Pancake P[1000] = {};
		for (int i = 0; i < N; i++) {
			scanf("%d %d", &P[i].R, &P[i].H);
		}

		qsort(P, N, sizeof(struct Pancake), cmp);
		long long int ans = 0;
		long long int max = 0;
		for (int i = 0; i < K - 1; i++) {
			ans += 2 * P[i].R * P[i].H;
			if (P[i].R > max) max = P[i].R;
		}
		ans += max * max;
		long long int maxDelta = 0;
		for (int i = K - 1; i < N; i++) {
			long long int delta = 2 * P[i].R * P[i].H;
			if (P[i].R > max) {
				delta += P[i].R * P[i].R - max * max;
			}
			if (delta > maxDelta) maxDelta = delta;
		}
		ans += maxDelta;

		printf("Case #%d: %lf\n", t + 1, (double)ans * pi);
	}
	return 0;
}

