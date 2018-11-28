#include <bits/stdc++.h>

using namespace std;

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int n, p;
		scanf("%d %d", &n, &p);
		int cnt[5] = {0}, ans = 0;
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &x);
			if (x % p == 0) ++ans;
			else cnt[x % p]++;
		}
		for (int i = 1; p - i >= i; i++) {
			while (cnt[i] && cnt[p - i]) {
				if (i == p - i && cnt[i] < 2) break;
				ans++;
				cnt[i]--;
				cnt[p - i]--;
			}
		}
		if (p == 2) {
			ans += cnt[1] > 0;
		} else if (p == 3) {
			ans += cnt[1] / 3 + (cnt[1] % 3 > 0);
			ans += cnt[2] / 3 + (cnt[2] % 3 > 0);
		} else if (p == 4) {
			if (cnt[2] || cnt[1] || cnt[3]) ans++;
			if (cnt[2] && (cnt[1] > 2 || cnt[3] > 2)) {
				ans++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
