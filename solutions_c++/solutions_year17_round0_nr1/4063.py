#include <cstdio>
#include <cstring>

char s[1111];

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, k;
	scanf("%d\n", &T);
	for (int kase = 1; kase <= T; ++kase) {
		scanf("%s %d\n", s, &k);
		int l = strlen(s);
		int ans = 0;
		for (int i = 0; i < l - k + 1; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < k; ++j)
					s[i + j] = s[i + j] == '+' ? '-' : '+';
				++ans;
			}
		}
		printf("Case #%d: ", kase);
		bool end = false;
		for (int i = 0; i < l; ++i) {
			if (s[i] == '-') {
				end = true;
				puts("IMPOSSIBLE");
				break;
			}
		}
		if (!end) {
			printf("%d\n", ans);
		}
	}
	return 0;
}
