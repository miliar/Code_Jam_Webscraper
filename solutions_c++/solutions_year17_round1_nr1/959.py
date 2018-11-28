#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <utility>
#include <map>
#include <set>

using namespace std;

const int maxm = 50;
const int maxn = 50;

char a[maxm + 1][maxn + 1];
int m, n;

void init() {
	int i, j, k;
	char found = false;
	char ever = false;
	scanf("%d%d", &m, &n);
	for (i = 1; i <= m; ++i) {
		scanf("%s", a[i] + 1);
	}

	for (i = 1; i <= m; ++i) {
		found = false;
		for (j = 1; j <= n; ++j) {
			if (a[i][j] != '?') {
				found = true;
				break;
			}
		}

		if (found) {
			if (!ever) {
				for (k = 1; k < i; ++k) {
					for (j = 1; j <= n; ++j) a[k][j] = a[i][j];
				}
				ever = true;
			}
		}
		else {
			if (ever) {
				for (j = 1; j <= n; ++j) {
					a[i][j] = a[i - 1][j];
				}
			}
		}
	}
}

void work() {
	int i, j, k;
	for (i = 1; i <= m; ++i) {
		j = 1;
		while (j <= n && a[i][j] == '?') ++j;
		for (k = 1; k < j; ++k) {
			a[i][k] = a[i][j];
		}
		for (k = j; k <= n; ++k) {
			if (a[i][k] == '?') a[i][k] = a[i][k - 1];
		}
	}
}

void output() {
	int i, j;
	for (i = 1; i <= m; ++i) {
		for (j = 1; j <= n; ++j)
		{
			printf("%c", a[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int T, t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d:\n", t);	
		init();
		work();
		output();
	}
	return 0;
}