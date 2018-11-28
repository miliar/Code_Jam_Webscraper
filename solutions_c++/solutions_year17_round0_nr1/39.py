#include <cstdio>
#include <cstdlib>
#include <cstring>

char s[1010];
int k;

void process() {
	int len = strlen(s);

	int res = 0;
	for (int i = 0; i < len - k + 1; i++) {
		if (s[i] == '-') {
			res++;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '+') {
					s[i + j] = '-';
				} else {
					s[i + j] = '+';
				}
			}
		}
	}
	for (int i = len - k + 1; i < len; i++) {
		if (s[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", res);
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		scanf("%s%d", s, &k);
		process();
	}
	
	return 0;
}