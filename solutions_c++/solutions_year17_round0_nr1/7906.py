#include <cstdio>
#include <string.h>

int main() {
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		char s[1010];
		int k;
		memset(s, 0, sizeof(s));
		scanf("%s%d", s, &k);


		int len = strlen(s);
		// printf("%d %d\n", len, k);
		int ans = 0;
		bool ok = true;
		for (int i = 0; i < len; i++) {
			// printf("%s\n", s);
			if (s[i] == '-') {
				ans++;
				ok = true;
				for (int j = i; j < i + k; j++) {
					if (j == len) {
						ok = false;
						break;
					}
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				if (!ok) {
					break;
				}
			}
		}

		if (!ok) {
			printf("Case #%d: IMPOSSIBLE\n", ++ca);
		} else {
			printf("Case #%d: %d\n", ++ca, ans);
		}
	}
	return 0;
}
