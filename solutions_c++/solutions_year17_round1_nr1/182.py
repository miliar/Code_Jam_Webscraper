#include <bits/stdc++.h>
using namespace std;

char s[30][30], ans[30][30];
int n, m, T, t_;

bool judge(int u) {
	for (int v = 1; v <= m; v++)
		if (s[u][v] != '?') return false;
	return true;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%d %d",&n,&m);
		for (int i = 1; i <= n; i++)
			scanf("%s",s[i] + 1);

		int bg = 0;
		for (int i = 1; i <= n; i++) {
			if (judge(i)) {
				if (bg) memcpy(ans[i], ans[i - 1], sizeof(ans[i]));
				continue;
			}
			if (!bg) bg = i;
			int st = 0;
			for (int j = 1; j <= m; j++) {
				if (s[i][j] == '?') {
					if (st) ans[i][j] = ans[i][j - 1];
				} else {
					if (!st) st = j;
					ans[i][j] = s[i][j];
				}				
			}
			for (int j = 1; j < st; j++)
				ans[i][j] = ans[i][st];
		}
		for (int i = 1; i < bg; i++) memcpy(ans[i], ans[bg], sizeof(ans[i]));
		printf("Case #%d:\n",++t_);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) putchar(ans[i][j]);
			putchar('\n');
		}			
	}
	return 0;
}
