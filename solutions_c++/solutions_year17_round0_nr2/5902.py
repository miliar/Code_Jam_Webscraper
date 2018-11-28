#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	//freopen("B-small-attempt1.in.txt", "r", stdin);
	//freopen("B-small.out.txt", "w", stdout);
	//freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	for (int tc = 1; tc <= T; tc++) {
		
		printf("Case #%d: ", tc);
		char s[20];
		int len = 0;
		scanf("%s", s);
		while (s[len])len++;
		for (int i = len - 1; i >= 1; i--) {
			if (s[i] < s[i - 1]) {
				s[i - 1]--;
				for (int j = i; j < len; j++)
					s[j] = '9';
			}
		}
		printf("%s\n", s[0] <= '0' ? s + 1:s);
	}
}