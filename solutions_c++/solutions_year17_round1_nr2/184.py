#include <bits/stdc++.h>
#define eps (1e-8)
using namespace std;

int n, m;
int T, ans, t_;
int st[52], val[52][52], base[52];

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%d %d",&n,&m);
		for (int i = 1; i <= n; i++) scanf("%d",&base[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				scanf("%d",&val[i][j]);
		int sing = 1, ans = 0;
		for (int i = 1; i <= n; i++) st[i] = 1;
		bool flag = true;
		for (int i = 1; i <= n; i++) sort(val[i] + 1, val[i] + m + 1);
		while (flag) {
			for (int i = 1; i <= n; i++) {
				while (st[i] <= m && (double) val[i][st[i]] < (double) (sing * base[i]) * 0.9 - eps)
					st[i]++;
				if (st[i] > m) { flag = false; break; }
			}
			if (!flag) break;
			bool fl = true;
			for (int i = 1; i <= n; i++) {
				if ((double) val[i][st[i]] <= (double) (sing * base[i]) * 1.1 + eps) continue;
				fl = false;
			}
			if (!fl) { sing++; continue; }
			else {
				ans++;
				for (int i = 1; i <= n; i++) st[i]++;
			}
		}
		printf("Case #%d: %d\n",++t_, ans);
	}
	return 0;
}
