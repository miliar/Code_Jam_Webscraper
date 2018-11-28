#include <stdio.h>
#include <string.h>

int main() {
	int T;
	scanf("%d", &T);
	char s[1010];
	int d;
	int count = 1;
	while(scanf("%s%d", s, &d) != EOF) {
		int len = strlen(s);
		int sum = 0;
		for (int i = 0; i < len - d + 1; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < d; j++) {
					if (s[i + j] == '+')
						s[i + j] = '-';
					else
						s[i + j] = '+';
				}
				sum++;
			}
		}
		bool t = true;
		for (int i = len - d; i < len; i++) {
			if (s[i] == '-') {
				t = false;
				break;
			}	
		}
		if (t == false) {
			printf("Case #%d: IMPOSSIBLE\n", count++);
		}
		else {
			printf("Case #%d: %d\n", count++, sum);
		}
	}
}