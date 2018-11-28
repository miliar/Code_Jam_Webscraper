#include <cstdio>
#include <cstring>
char s[20];
int main() {
	int T;
	scanf("%d ", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%s", s);
		int len=strlen(s);
		for (int k = 0; k < len;k++){
			for (int j = 0; s[j + 1]; j++) {
				if (s[j] > s[j + 1]) {
					if (s[j] != '0') {
						s[j]--;
						j++;
						while (s[j] != 0) s[j++] = '9';
					}
				}
			}
		}

		printf("Case #%d: ", i);
		int j = 0;
		while (s[j] == '0') j++;
		for (; s[j]; j++)
			printf("%c", s[j]);
		puts("");
	}
	return 0;
}