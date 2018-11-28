#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <vector>

using namespace std;

int n, m;
char a[30][30];
int s[30][30];

int sum(int x1, int y1, int x2, int y2) {
	return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1];
}

void search(int x1, int y1, int x2, int y2) {
	int cnt = sum(x1, y1, x2, y2);
	if (cnt == 1) {
		char ch = '?';
		for (int i = x1; i <= x2; i++)
			for (int j = y1; j <= y2; j++)
				if (a[i][j] != '?')
					ch = a[i][j];
		for (int i = x1; i <= x2; i++)
			for (int j = y1; j <= y2; j++)
				a[i][j] = ch;
		return;
	}
	for (int i = x1; i < x2; i++) {
		int c1 = sum(x1, y1, i, y2);
		if (c1 > 0 && c1 < cnt) {
			search(x1, y1, i, y2);
			search(i+1, y1, x2, y2);
			return;
		}
	}
	for (int j = y1; j < y2; j++) {
		int c2 = sum(x1, y1, x2, j);
		if (c2 > 0 && c2 < cnt) {
			search(x1, y1, x2, j);
			search(x1, j+1, x2, y2);
			return;
		}
	}
}

void run(int cas) {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++)
		scanf("%s", a[i] + 1);
	memset(s, 0, sizeof(s));
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			s[i][j] = s[i][j - 1] + (a[i][j] != '?');
	for (int j = 1; j <= m; j++)
		for (int i = 1; i <= n; i++)
			s[i][j] += s[i - 1][j];
	search(1, 1, n, m);
	printf("Case #%d:\n", cas);
	for (int i = 1; i <= n; i++)
		printf("%s\n", a[i] + 1);
}

int main() {
	int cas, tt;
	scanf("%d", &tt);
	for (cas = 1; cas <= tt; cas++)
		run(cas);
	return 0;
}