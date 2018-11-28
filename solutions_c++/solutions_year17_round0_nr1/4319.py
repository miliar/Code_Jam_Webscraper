#include <cstdio>
#include <cstring>
int t, k;
char s[1001];
int main() {
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		int ans = 0;
		scanf("%s%d", s, &k);
		int slen = strlen(s);

		for (int j = 0; j < slen - k + 1; j++) {
			if (s[j] == '-') {
				for (int l = 0; l < k; l++) {
					if (s[j + l] == '+'){
						s[j + l] = '-';
					} else {
						s[j + l] = '+';
					}
				}
				ans++;
			}	
		}
		for (int j = 0; j < k; j++) {
			if (s[slen - j - 1] == '-') {
				ans = -1;
			}
		}

		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		} else {
			printf("Case #%d: %d\n", i + 1, ans);
		}
	}
}
