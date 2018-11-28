#include <cstdio>
#include <cstring>

int main() {
	int T;
	char s[25];
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%s",s);
		for (int i = 1; i < strlen(s); i++) {
			int j = i;
			while (j > 0 && s[j-1] > s[j]) {
				s[j-1]--;
				j--;
			}

			if (j != i) {
				for (int k = j+1; k < strlen(s); k++) {
					s[k] = '9';
				}
				break;
			}
		}
		printf("Case #%d: ", tc);
		for (int i = 0; i < strlen(s); i++) {
			if (s[i] > '0') {
				printf("%c", s[i]);
			}
		}
		printf("\n");
	}
	return 0;
}