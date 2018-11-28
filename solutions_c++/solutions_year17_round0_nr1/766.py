#include <stdio.h>
#include <string.h>

char str[2000];

void solve() {
	scanf("%s", str);
	int K; scanf("%d", &K);
	int len = strlen(str);
	int cnt = 0;

	for (int i = 0; i < len - K + 1; i++) {
		if (str[i] == '-') {
			cnt++;
			for (int j = 0; j < K; j++) {
				str[i + j] = '+' + '-' - str[i + j];
			}
		}
	}

	for (int i = 0; i < len; i++) {
		if (str[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", cnt);
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}