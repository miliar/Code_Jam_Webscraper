#include <cstdio>

char N[20];

int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		scanf("%s", N);
		for (int i = 1; N[i]; ++i) {
			if (N[i - 1] > N[i]) {
				for (int j = i; N[j]; ++j) {
					N[j] = '9';
				}
				--N[i - 1];
				for (int j = i - 2; j >= 0 && N[j] > N[j + 1]; --j) {
					N[j] = N[j + 1];
					N[j + 1] = '9';
				}
			}
		}
		printf("Case #%d: ", tc);
		for (int i = 0; N[i]; ++i) {
			if (N[i] > '0') {
				putchar(N[i]);
			}
		}
		putchar('\n');
	}
	return 0;
}

