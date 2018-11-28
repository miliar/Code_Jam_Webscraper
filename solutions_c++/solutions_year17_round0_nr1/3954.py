#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, t, K, k, i, j, s, ans;
	char S[1001];
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		scanf(" %s %d", S, &K);
		s = strlen(S);
		ans = 0;
		for(i = 0; i <= s-K; ++i) {
			if(S[i] == '-') {
				++ans;
				for(j = 0; j < K; ++j) {
					S[i+j] = S[i+j]=='+'?'-':'+';
				}
			}
		}
		for(i = 0; i < s; ++i) {
			if(S[i] == '-') {
				ans = -1;
				break;
			}
		}
		if(ans != -1) {
			printf("Case #%d: %d\n", t+1, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		}

	}
	return 0;
}