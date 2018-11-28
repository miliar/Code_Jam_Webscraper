#include <cstdio>

int main(void) {
	int T, K;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		char cakes[1001] = { 0 };
		int num = 0, up = 0, down = 0;
		scanf("%s %d\n", cakes, &K);
		for (int i = 0; cakes[i] && i < 10; i++) {
			num++;
			if (cakes[i] == '+')
				up++;
			else
				down++;
		}
		if (num == up) {
			printf("Case #%d: 0\n", i);
		}
		else {
			int flip = 0;
			for (int i = 0; i <= num - K; i++) {
				if (cakes[i] == '-') {
					flip++;
					for (int j = 0; j < K; j++) {
						if (cakes[i + j] == '+') {
							cakes[i + j] = '-';
							down++;
							up--;
						}
						else {
							cakes[i + j] = '+';
							up++;
							down--;
						}
					}
				}
				if (num == up)
					break;
			}
			if (num == up)
				printf("Case #%d: %d\n", i, flip);
			else
				printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}
