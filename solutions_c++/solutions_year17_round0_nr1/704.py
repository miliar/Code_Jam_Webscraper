#include <cstdio>

#define SIZE 1005

char s[SIZE];

int main(void)
{
	int t, k;
	scanf("%d", &t);
	for (int _c = 0; _c < t; _c ++) {
		printf("Case #%d: ", _c + 1);
		scanf("%s%d", s, &k);
		int ans = 0;
		for (int i = 0; s[i + k - 1]; i ++) {
			if (s[i] == '+') continue;
			ans ++;
			for (int j = i; j < i + k; j ++) {
				s[j] = (s[j] == '+') ? '-' : '+';
			}
		}

		bool sol = true;
		for (int i = 0; s[i]; i ++) {
			if (s[i] == '-') {
				sol = false;
				break;
			}
		}
		if (sol) {
			printf("%d\n", ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}