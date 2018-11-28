#include <cstdio>
#include <cstring>

int cases, K;
char S[5005];

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%s%d", S, &K);
		int len = strlen(S);
		int ans = 0;
		for(int i = 0; i <= len - K + 1; ++i) {
			if(S[i] == '+') continue;
			if(i == len - K + 1) {
				ans = -1;
				break;
			}
			++ans;
			for(int j = i; j < i + K; ++j) {
				if(S[j] == '-') S[j] = '+';
				else S[j] = '-';
			}
		}
		for(int i = 0; i < len; ++i)
			if(S[i] == '-') {
				ans = -1;
				break;
			}
		printf("Case #%d: ", xx);
		if(ans == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
	}
}
