#include <stdio.h>
#include <string.h>

const int maxn = 1010;

int a[maxn + 1];
char s[maxn + 1];
int res, n, K;

void init() {
	int i;
	scanf("%s%d", s + 1, &K);
	n = strlen(s + 1);
	for (i = 1; i <= n; ++i)
		a[i] = s[i] == '+' ? 1 : 0;
}

void work() {
	int i, j;
	res = 0;
	for (i = 1; i <= n - K + 1; ++i) {
		if (a[i] == 0) {
			++res;
			for (j = i; j < i + K; ++j) a[j] = 1 - a[j];
		}
	}
}

void output() {
	for (int i = 1; i <= n; ++i)
		if (a[i] == 0) {
			res = -1;
		}
	if (res == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
}

int main() {
	int T, t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		init();
		work();
		output();
	}

	return 0;
}