#include <stdio.h>

__inline int max(int a, int b) {
	return a > b ? a : b;
}
int t, n,sum,ans;
int main() {
	//freopen("c:\\input.txt", "r", stdin);
	//freopen("c:\\output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		ans = 0;
		char str[1004] = { 0 };
		int C[1004] = { 0 };
		scanf("%s%d", str, &n);
		for (int i = 0; str[i] != NULL; i++) {
			if (str[i + n - 1] == NULL) {
				sum = 0;
				for (int j = max(0, i - n + 1); j <= i; j++) sum += C[j];
				if ((sum + (str[i] == '-' ? 1 : 0)) & 1) {
					printf("Case #%d: IMPOSSIBLE\n", tc);
					goto loop;
				}
			}
			else {
				sum = 0;
				for (int j = max(0, i - n + 1); j <= i; j++) sum += C[j];
				if ((sum + (str[i] == '-' ? 1 : 0)) & 1) {
					C[i] = 1;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	loop:;
	}
}