#include <cstdio>

char S[1001];

int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		int K;
		int ans = 0;
		scanf("%s%d", S, &K);
		for (int i = 0; S[i + K - 1]; ++i) {
			if (S[i] == '-') {
				for (int j = 0; j < K; ++j) {
					if (S[i + j] == '-') {
						S[i + j] = '+';
					} else {
						S[i + j] = '-';
					}
				}
				++ans;
			}
		}
		bool ok = true;
		for (int i = 0; S[i]; ++i) {
			if (S[i] == '-') {
				ans = -1;
			}
		}
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		} else {
			printf("Case #%d: %d\n", tc, ans);
		}
	}
	return 0;
}

