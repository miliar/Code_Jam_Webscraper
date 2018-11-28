#include <bits/stdc++.h>

using namespace std;

int tp = 0;
int n, k, m;
int T;
int c[200001], v[20001], a[20001], b[20001];
int cnt[20001];

int main( ) {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	while (T --) {
		scanf("%d %d %d", &n, &k, &m);
		for (int i = 1; i <= n; i ++) c[i] = v[i] = 0;
		for (int i = 1; i <= k; i ++) cnt[i] = 0;
		int mx = 0;
		for (int i = 1; i <= m; i ++) {
			scanf("%d %d", &a[i], &b[i]);
			++ cnt[b[i]];
			mx = max(mx, cnt[b[i]]);
			c[a[i]] ++;
		}
		for (int i = 1; i <= n; i ++) {
			c[i] += c[i - 1];
			mx = max(mx, (c[i] + i - 1) / i);
		}
		for (int i = 1; i <= m; i ++) v[a[i]] ++;
		int ans = 0;
		for (int i = 1; i <= n; i ++)
			ans += max(v[i] - mx, 0);
		printf("Case #%d: %d %d\n", ++ tp, mx, ans);
	}
	return 0;
}
