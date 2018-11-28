#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; ++i) {
		printf("Case #%d: ", i+1);

		int N, K;
		scanf("%d%d", &N, &K);

		int nBelow1 = 0, nOver1 = 0;
		for(int j = 1, p = 0; K; j *= 2, ++p) {
			if(K > j) {
				--N;
				if(N % 2 == 1 && nOver1 == 0) {
					nOver1 = j;
				} else if(N % 2 == 1 && nOver1 > 0) {
					nOver1 = 2 * nOver1 + nBelow1;
				}
				nBelow1 = j*2 - nOver1;

				K -= j;
				N /= 2;
			} else {
				if(N == 0) {
					puts("0 0");
					break;
				}

				--N;

				int min = N / 2;
				int max = min;
				if(N % 2 == 1) {
					if(K <= nOver1)
						++min;
					++max;
				} else {	// K > nOver1
					if(K <= nOver1)
						++max;
				}

				printf("%d %d\n", max, min);
				break;
			}

			// printf("%d\t%d\t%d\n", N, nOver1, nBelow1);
		}
	}

	return 0;
}
