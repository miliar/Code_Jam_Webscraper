#include <stdio.h>
int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		char S[1001];
		char flip[256];
		flip['-'] = '+';
		flip['+'] = '-';
		int K, ans = 0, len = 0;
		scanf("%s %d", S, &K);
		while (S[len]) len++;
		for (int i = 0; i<len-(K-1); i++) {
			char ch = S[i];
			if (ch == '-') {
				ans++;
				for (int j = 0; j < K; j++) S[i + j] = flip[S[i + j]];
			}
		}
		for (int i = 0; i < len; i++)
			if (S[i] == '-') ans = -1;
		printf("Case #%d: ",tc);
		if (ans < 0)printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}