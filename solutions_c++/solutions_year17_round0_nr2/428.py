#include <stdio.h>
#include <string.h>

int main() {
	int T;
	scanf("%d", &T);
	char s[20];
	int count = 1;
	while(scanf("%s", s) != EOF) {
		int len = strlen(s);
		for (int i = 0; i < len - 1; i++) {
			if (s[i] > s[i + 1]) {
				int start;
				for (int j = i; j >= 0; j--) {
					if (s[j] == s[i])
						start = j;
				}
				s[start] -= 1;
				for (int j = start + 1; j < len; j++) {
					s[j] = '9';
				}
			}
		}
		printf("Case #%d: ", count++);
		for (int i = 0; i < len; i++) {
			if (s[i] == '0')
				continue;
			putchar(s[i]);
		}
		printf("\n");
	}
}