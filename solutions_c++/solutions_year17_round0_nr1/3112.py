#include <cstdio>

char S[1001];
int K;

char flip(char c) {
    return c == '-' ? '+' : '-';
}

void solve() {
    int ans = 0;
    scanf("%s%d", S, &K);
    for (int i = 0; S[i + K - 1]; i++)
	if (S[i] == '-') {
	    for (int j = 0; j < K; j++)
		S[i + j] = flip(S[i + j]);
	    ans++;
	}
    for (int i = 0; S[i]; i++)
	if (S[i] == '-') {
	    puts("IMPOSSIBLE");
	    return;
	}
    printf("%d\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
	printf("Case #%d: ", i);
	solve();
    }
}
