#include <bits/stdc++.h>
using namespace std;
int t, n, m, c, p[1020], b[1020];
int v[1020];
int d[1020];
int f[1020];
int tmp;
bool ok(int x) {
	int re = 0;
	tmp = 0;
	for (int i = n; i > 0; i--) {
		re += v[i];
		tmp += max(v[i] - x, 0);
		re -= x;
		if (re < 0) {
			re = 0;
		}
	}
	return re == 0;
}

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		int ans = 0;
		memset(v, 0, sizeof v);
		memset(d, 0, sizeof d);
		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; i++) {
			scanf("%d%d", &p[i], &b[i]);
			v[p[i]]++;
			d[b[i]]++;
			ans = max(ans, d[b[i]]);
		}
		for (int i = 1;; i++) {
			if (ok(i)) {
				ans = max(ans, i);
				break;
			}
		}
		ok(ans);
		printf("Case #%d: %d %d\n", tt, ans, tmp);
	}

}