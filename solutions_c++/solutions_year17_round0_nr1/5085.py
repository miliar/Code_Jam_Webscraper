#include <cstdio>
#include <cstring>

const int N = 1001;

char s[N];
int n, k;

int main() {
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%s", s);
		scanf("%d", &k);
		n = strlen(s);
		int ans = 0;
		for (int i = 0; i + k <= n; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < k; j++) {
					s[i + j] ^= '+' ^ '-';
				}
				ans++;
			}
		}
		bool flag = true;
		for (int i = 0; i < n; i++) {
			if (s[i] == '-') {
				flag = false;
			}
		}
		if (!flag) printf("Case #%d: IMPOSSIBLE\n", cas);
		else printf("Case #%d: %d\n", cas, ans);
	}
}
