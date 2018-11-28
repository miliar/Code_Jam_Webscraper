#include <stdio.h>
#include <string.h>

char str[1001];

void flip(int start, int k) {
	for (int i = start; i < start + k; i++) {
		if (str[i] == '-') str[i] = '+';
		else str[i] = '-';
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		int k;
		int len;
		scanf("%s %d", str, &k);
		len = strlen(str);
		int count = 0;

		for (int i = 0; i <= len - k; i++) {
			char c = str[i];
			if (c == '-') {
				flip(i, k);
				count++;
			}
		}
		
		bool success = true;
		for (int i = len - k + 1; i < len; i++) {
			if (str[i] == '-') {
				success = false;
				break;
			}
		}

		if (success) {
			printf("Case #%d: %d\n", t + 1, count);
		}
		else {
			printf("Case #%d: %s\n", t + 1, "IMPOSSIBLE");
		}
	}

	return 0;
}
