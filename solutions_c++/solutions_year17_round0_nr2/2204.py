#include <stdio.h>

int main() {
	int T, i, j, d, t = 1; char s[20];
	for (scanf("%d", &T); T--; ) {
		for (scanf("%s", s), i = 1; s[i]; i++) {
			if (s[i] < s[i-1]) {
				if (s[i-1] != '0') {
					s[i-1]--, s[i] = '9';
					for (j = i+1; s[j]; j++)
						s[j] = '9';
					i = -1;
				}
				else {
					for (j = i+1, s[i] = '9', i--, s[i] = '9', i--; s[i] == '0'; i--) ;
					for (; s[j]; j++)
						s[j] = '9';
					s[i]--, i = -1;
				}
			}
		}
		for (i = 0; s[i] == '0'; i++) ;
		printf("Case #%d: %s\n", t++, s+i);
	}
} 
