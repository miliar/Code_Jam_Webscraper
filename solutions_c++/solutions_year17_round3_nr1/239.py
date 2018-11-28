#include<cstdio>
#include<algorithm>
#include<cmath>

int test, t, r[1003], h[1003], f[1003], n, k;

bool cmp(int x, int y) {
	return 1ll * r[x] * h[x] > 1ll * r[y] * h[y];
}

long long max(long long x, long long y) {
	return x > y ? x : y;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++) scanf("%d %d", &r[i], &h[i]);
		for (int i = 1; i <= n; i++) f[i] = i;
		std::sort(f + 1, f + n + 1, cmp);
		long long ans = 0;
		for (int i = 1; i <= n; i++) {
			int c = 1;
			long long s = 1ll * r[f[i]] * r[f[i]] + 2ll * r[f[i]] * h[f[i]];
			for (int j = 1; j <= n && c < k; j++)
				if (i == j) continue;
				else if (r[f[j]] <= r[f[i]]) {
					s += 2ll * r[f[j]] * h[f[j]];
					c++;
				}
			if (k == c) ans = max(s, ans);
		}
		printf("Case #%d: %.9lf\n", test, ans * 4 * atan(1));
	}
}
