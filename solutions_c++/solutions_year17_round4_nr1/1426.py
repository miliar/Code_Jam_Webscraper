#include <bits/stdc++.h>

using namespace std;

int T, n, p;
int cnt[9];
int main() {
	// freopen("a.in", "r", stdin);
	// freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d %d", &n, &p);
		int ans = 0;
		memset(cnt, 0, sizeof(cnt));
		int x;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &x);
			x %= p;
			cnt[x]++;
		}
		ans += cnt[0];
		if (p == 2) ans += (cnt[1] + 1) / 2;
		else if (p == 3) {
			int a = cnt[1], b = cnt[2];
			if (a > b) swap(a, b);
			ans += a;
			b -= a;
			ans += (b + 2) / 3;
		} else {
			int a = cnt[1], b = cnt[3];
			if (a > b) swap(a, b);
			ans += a;
			b -= a;
			ans += (cnt[2]) / 2;
			a = cnt[2] % 2;
			if (a * 2 == b) {
				ans += a;
			} else if (a * 2 < b) {
				ans += a;
				b -= a * 2;
				ans += (b + 3) / 4;
			} else {
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}


	return 0;
}
