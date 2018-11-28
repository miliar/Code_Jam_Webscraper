#include <stdio.h>
#include <string.h>
const int maxLen = 20;
int main() {
	int T;
	char str[maxLen +1];
	long long int ans;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%s", str);
		int len = strlen(str);
		for (int i = len -1; i > 0; --i) {
			if (str[i] < str[i -1]) {
				str[i -1] -= 1;
				for (int j = i; j < len; ++j)
					str[j] = '9';
			}
		}

		sscanf(str, "%lld", &ans);
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}
