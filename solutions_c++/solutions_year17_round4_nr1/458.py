#include <bits/stdc++.h>
using namespace std;
int t, n, a[1000], g;
int c[10];
int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d%d", &n, &g);
		int s = 0;
		for (int i = 0; i <= g; i++) {
			c[i] = 0;
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			a[i] %= g;
			s += a[i];
		}
		if (s % g > 0) {
			a[n++] = g - s % g;
		}
		for (int i = 0; i < n; i++) {
			c[a[i] % g]++;
		}
		int ans = c[0];
		if (g == 2) {
			assert(c[1] % 2 == 0);
			ans += c[1] / 2;
		} else if (g == 3) {
			assert((c[1] + c[2] + c[2]) % 3 == 0);
			int t = min(c[1], c[2]);
			c[1] -= t;
			c[2] -= t;
			ans += t;
			ans += c[1] / 3 + c[2] / 3;
		} else if (g == 4) {
			assert((c[1] + c[2] + c[2] + c[3] + c[3] + c[3]) % 4 == 0);
			int t = min(c[1], c[3]);
			c[1] -= t;
			c[3] -= t;
			ans += t;
			ans += c[2] / 2;
			c[2] %= 2;
			ans += c[1] / 4 + c[3] / 4;
			c[1] %= 4;
			c[3] %= 4;
			ans += c[2];
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}