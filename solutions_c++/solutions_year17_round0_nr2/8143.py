#include <cstdio>

int t;
char s[20];

int main() {
	scanf("%d", &t);
	for (int c = 0; c < t; c++) {
		scanf("%s", s);
		for (int i = 1; s[i]; i++) {
			if (s[i] < s[i - 1]) {
				for (int j = i - 1; j >= 0; j--) {
					s[j]--;
					if (j - 1 >= 0 && s[j] < s[j - 1]) {
						s[j] = '9';
					} else {
						break;
					}
				}
				for (int j = i; s[j]; j++) {
					s[j] = '9';
				}
			}
		}

		printf("Case #%d: %s\n", c + 1, s[0] == '0'? s + 1: s);
	}
	return 0;
}
