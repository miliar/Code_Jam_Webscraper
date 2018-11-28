#include <cstdio>
#include <cstdlib>

const int MAXN = 30;

char s[MAXN][MAXN];
int p[MAXN];

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
			scanf("%s", s[i] + 1);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j) {
				if (s[i][j] == '?') {
					if (j == 1) {
						for (int k = j + 1; k <= m; ++k)
							if (s[i][k] != '?') {
								s[i][j] = s[i][k];
								p[i] = Case;
								break;
							}
					}
					else s[i][j] = s[i][j - 1];
				}
				else p[i] = Case;
			}
		for (int i = 1; i <= n; ++i)
			if (p[i] == Case) {
				for (int j = i - 1; j > 0 && p[j] != Case; --j)
					for (int k = 1; k <= m; ++k)
						s[j][k] = s[i][k];
				for (int j = i + 1; j <= n && p[j] != Case; ++j)
					for (int k = 1; k <= m; ++k)
						s[j][k] = s[i][k];
			}
		printf("Case #%d:\n", Case);
		for (int i = 1; i <= n; ++i)
			printf("%s\n", s[i] + 1);
	}
	return 0;
}
