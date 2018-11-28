#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>

int main() {
	int T;
	int D;
	int N;
	char buf[512];

	fgets(buf, 512, stdin);

	sscanf(buf, "%d", &T);

	int i,j;

	for (i = 0; i < T; ++i) {
		fgets(buf, 512, stdin);
		sscanf(buf, "%d %d", &D, &N);

		double maxtime = 0;

		for (j = 0; j < N; ++j) {
			fgets(buf, 512, stdin);

			int K,S;

			sscanf(buf, "%d %d", &K, &S);

			double time = ((double)(D - K)) / S;

			if (maxtime < time)
				maxtime = time;
		}

		printf("Case #%d: %lf\n", i + 1, D / maxtime);
	}

	return 0;
}