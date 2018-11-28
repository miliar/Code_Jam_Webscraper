#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXN = 10001;

int T, k, r[MAXN];
char s[MAXN];

int main() {
	freopen("A.in", "r", stdin);
	scanf("%d", &T);
	for (int cs = 1; cs <= T; cs++) {
		scanf("%s%d", s + 1, &k);
		int n = strlen(s + 1);
		for (int i = 1; i <= n; i++) {
			if (s[i] == '-') r[i] = 0;
			else r[i] = 1;
		}
		int answer = 0;
		for (int i = 1; i <= n - k + 1; i++) {
			if (r[i] == 0) {
				answer++;
				for (int j = i; j <= i + k - 1; j++) {
					r[j] ^= 1;
				}
			}
		}
		for (int i = 1; i <= n; i++) {
			if (r[i] == 0) {
				answer = -1;
				break;
			}
		}
		printf("Case #%d: ", cs);
		if (answer == -1) puts("IMPOSSIBLE");
		else printf("%d\n", answer);
	}
}
