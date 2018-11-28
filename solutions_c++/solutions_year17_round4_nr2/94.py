#include <bits/stdc++.h>

using namespace std;

const int MX = 1000;

int f[MX], g[MX], h[MX];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(f, 0, sizeof f);
		memset(g, 0, sizeof g);
		memset(h, 0, sizeof h);
		
		int n, c, m;
		scanf("%d %d %d", &n, &c, &m);
		for (int i = 0; i < m; i++) {
			int p, x;
			scanf("%d %d", &p, &x);
			f[p - 1]++;
			h[p - 1]++;
			g[x - 1]++;
		}
		
		int cnt = 0, ans = 0;
		for (int i = 0; i < n; i++) {
			if (i > 0) f[i] += f[i - 1];
			cnt = max((f[i] + i) / (i + 1), cnt);
		}
		
		for (int i = 0; i < c; i++) cnt = max(g[i], cnt);
		
		for (int i = 0; i < n; i++) ans += max(h[i] - cnt, 0);
		
		printf("Case #%d: %d %d\n", t, cnt, ans);
	}

	return 0;
}
