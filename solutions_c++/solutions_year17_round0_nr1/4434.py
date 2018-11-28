#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
const int N = 1024;
char S[N];

void flip(int idx) {
	if (S[idx] == '+') {
		S[idx] = '-';
	} else {
		S[idx] = '+';
	}
}

int main() {
	int T, n, K;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%s %d", S, &K);
		n = strlen(S);
		int answer = 0;
		rep(i, n) {
			bool need_flip = false;
			if (S[i] == '-') {
				answer ++;
				need_flip = true;
			}
			if (need_flip && i + K > n) {
				answer = -1;
				break;
			}
			rep(j, K) {
				if (need_flip) {
					flip(i+j);
				}
			}
		}
		printf("Case #%d: ", cas + 1);
		if (answer == -1) {
			puts("IMPOSSIBLE");
		} else  {
			printf("%d\n", answer);
		}
	}
	return 0;
}
