#include <cstdio>
#include <cstring>
const int maxn = 1005;
int T, k, n, ans, d[maxn], p[maxn];
char s[maxn];
int main() {
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase) {
		scanf("%s%d", s + 1, &k);
		n = strlen(s + 1);
		for (int i = 1; i <= n; ++i) p[i] = s[i] == '-';
		ans = p[0] = p[++n] = 0;
		for (int i = 1; i <= n; ++i) d[i] = p[i] ^ p[i - 1];
		for (int i = 1; i <= n; ++i) if (d[i] && i + k <= n) d[i] ^= 1, d[i + k] ^= 1, ++ans;
		for (int i = 1; i <= n; ++i) if (d[i]) ans = -1;
		printf(ans == -1 ? "Case #%d: IMPOSSIBLE\n" : "Case #%d: %d\n", kase, ans);
	}
	return 0;
}
