#include <bits/stdc++.h>
using namespace std;
const int N = 55, M = 1.15e6 + 5;
int x[N];
int add[N][M], cnt[N], del[N][M], iuse[N];
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++ i) {
			scanf("%d", &x[i]);
		}
		memset(add, 0, sizeof(add));
		memset(del, 0, sizeof(del));
		for (int i = 1; i <= n; ++ i) {
			for (int j = 1; j <= m; ++ j) {
				int a;
				scanf("%d", &a);
				int R = 10 * a / (9 * x[i]);
				int L = (10 * a + 11 * x[i] - 1) / (11 * x[i]);
				if (L <= R) {
					add[i][R] ++;
					if (L) del[i][L - 1] ++;
				}
			}
		}
		int ans = 0;
		memset(cnt, 0, sizeof(cnt));
		memset(iuse, 0, sizeof(iuse));
		for (int i = M - 1; i >= 1; -- i) {
			int f = 1e9;
			for (int j = 1; j <= n; ++ j) {
				cnt[j] += add[j][i];
				cnt[j] -= del[j][i];
				iuse[j] -= del[j][i];
				iuse[j] = max(0, iuse[j]);
				f = min(f, cnt[j] - iuse[j]);
			}
			/*if (f) {
				printf("f at %d\n", i);
			}*/
			ans += f;
			for (int j = 1; j <= n; ++ j) {
				iuse[j] += f;
			}
		}
		printf("Case #%d: %d\n", ++ zzz, ans);
	}
}

