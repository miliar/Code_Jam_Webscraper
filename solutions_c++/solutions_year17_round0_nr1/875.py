#include <stdio.h>
#include <string.h>
const int maxLen = 1000;
int main() {
	int T;
	char str[maxLen +1];
	int k, len, ans;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%s %d", str, &k);
		len = strlen(str);
		ans = 0;

		for (int i = 0; i + k <= len; ++i) {
			if (str[i] == '-') {
				for (int j = 0; j < k; ++j) {
					if (str[i + j] == '-')
						str[i + j] = '+';
					else
						str[i + j] = '-';
				}
				ans++;	
			} 
		}

		for (int i = len - k; i < len && ans >= 0; ++i)
			if (str[i] == '-')
				ans = -1;

		printf("Case #%d: ", t);
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
