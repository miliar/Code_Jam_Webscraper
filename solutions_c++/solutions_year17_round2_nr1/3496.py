#include <stdio.h>

int main() {
	int T;
	double max, D, N, Ki, Si;
	double times[1000];

	scanf("%d", &T);

	for (int t = 0; t < T; ++t) {
		for (int i = 0; i < 1000; ++i) {
			times[i] = 0;
		}

		scanf("%lf %lf", &D, &N);

		for (int n = 0; n < N; ++n) {
			scanf("%lf %lf", &Ki, &Si);
			times[n] = (D-Ki)/Si;
		}

		max = times[0];
		for (int i = 0; i < 1000; ++i) {
			if (max < times[i]) max = times[i];
		}

		printf("Case #%d: %lf\n", t + 1, D/max);
	}
}