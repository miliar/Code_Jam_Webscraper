#include <cstdio>

int N;
int D[6]; // ROYGBV - RYB 024
const char *p = "ROYGBV";

int main() {
	int tc, max1, max2, max3;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		scanf("%d", &N);
		for (int k = 0; k < 6; ++k) scanf("%d", &D[k]);

		if (D[0] * 2 > N || D[2] * 2 > N || D[4] * 2 > N) {
			// impossible
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}

		printf("Case #%d: ", t);
		if (D[0] >= D[2] && D[2] >= D[4]) max1 = 0, max2 = 2;
		else if (D[0] >= D[4] && D[4] >= D[2]) max1 = 0, max2 = 4;
		else if (D[2] >= D[0] && D[0] >= D[4]) max1 = 2, max2 = 0;
		else if (D[2] >= D[4] && D[4] >= D[0]) max1 = 2, max2 = 4;
		else if (D[4] >= D[0] && D[0] >= D[2]) max1 = 4, max2 = 0;
		else max1 = 4, max2 = 2;
		max3 = 6 - max1 - max2;

		while(D[max1] > 0) {
			putchar(p[max1]);
			if (D[max1] < D[max2] + D[max3]) {
				putchar(p[max2]);
				putchar(p[max3]);
				--D[max2];
				--D[max3];
			} else if (D[max2] > 0) {
				putchar(p[max2]);
				--D[max2];
			} else {
				putchar(p[max3]);
				--D[max3];
			}
			--D[max1];
		}

		puts("");
	}

	return 0;
}