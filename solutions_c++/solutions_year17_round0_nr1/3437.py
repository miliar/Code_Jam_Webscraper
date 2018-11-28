#include <cstdio>
#include <cstring>

int T, K;
char S[10000];

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%s %d", S, &K);
		int ss = strlen(S);
		int Ans = 0, i;
		for (i = 0; i < ss; i++) {
			S[i] = (S[i] == '+');
		}
		for (i = 0; i < ss - K + 1; i++) {
			if (!S[i]) {
				for (int j = i; j < i + K; j++) {
					S[j] ^= 1;
				}
				Ans++;
			}
		}
		for (; i < ss; i++) {
			if (!S[i]) {
				printf("Case #%d: IMPOSSIBLE\n", tc);
				goto NEXT;
			}
		}
		printf("Case #%d: %d\n", tc, Ans);

	NEXT:;
	}

	return 0;
}