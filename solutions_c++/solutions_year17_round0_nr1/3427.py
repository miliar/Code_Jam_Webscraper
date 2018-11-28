#include<stdio.h>
char S[1005];
int K;
void swap(int x) {
	for (int i = 0; i < K; i++) {
		if (S[i + x] == '+')
			S[i + x] = '-';
		else
			S[i + x] = '+';
	}
	return;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		scanf("%s %d", S, &K);
		int len = -1,ans=0;
		while (S[++len] != 0);
		for (int i = 0; i + K <= len; i++) {
			if (S[i] == '-') {
				swap(i);
				ans++;
			}
		}
		bool poss = true;
		for (int i = len - 1; i >= len - K; i--) {
			if (S[i] == '-') {
				poss = false;
				break;
			}
		}
		printf("Case #%d: ", test++);
		if (poss)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}