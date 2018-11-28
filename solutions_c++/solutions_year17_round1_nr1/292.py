#include <bits/stdc++.h>

using namespace std;

char str[1001][1001];
bool mark[1001];

int n, m, tp;
int main( ) {
	int T;
	scanf("%d", &T);
	while (T --) {
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i ++)
			scanf("%s", str[i] + 1);
		for (int i = 1; i <= n; i ++) mark[i] = false;
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= m; j ++)
				if (str[i][j] != '?') {
					char ch = str[i][j];
					int tmp = j - 1;
					while (tmp && str[i][tmp] == '?') -- tmp;
					++ tmp;
					for (int k = tmp; k <= j; k ++) str[i][k] = ch;
					tmp = j + 1;
					while (tmp <= m && str[i][tmp] == '?') ++ tmp;
					-- tmp;
					for (int k = j; k <= tmp; k ++) str[i][k] = ch;
					mark[i] = true;
				}
		for (int i = 1; i <= n; i ++)
			if (mark[i] == false) {
				int idx = -1;
				for (int j = i - 1; j >= 1; j --)
					if (mark[j]) {
						idx = j;
						break;
					}
				for (int j = i + 1; j <= n; j ++)
					if (mark[j]) {
						idx = j;
						break;
					}
				for (int j = 1; j <= m; j ++)
					str[i][j] = str[idx][j];
			}
		printf("Case #%d:\n", ++ tp);
		for (int i = 1; i <= n; puts(""), i ++)
			for (int j = 1; j <= m; j ++)
				printf("%c", str[i][j]);
	}
	return 0;
}
