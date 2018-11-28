#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char s[20];
int a[20], ans[20], ansn, n, found;
void dfs(int x, int ok) {
	if (x == 0) {
		found = 1;
		return;
	}
	if (ok) {
		ans[x] = 9;
		dfs(x - 1, ok);
	}
	else {
		for (int i = 9; i >= ans[x + 1]; i--) {
			if (i > a[x]) continue;
			ans[x] = i;
			if (a[x] > i) dfs(x - 1, 1);
			else dfs(x - 1, 0);
			if (found) return;
		}
	}
}
int main() {
	int T; for (scanf("%d", &T); T--; ) {
		scanf("%s", s + 1);
		n = strlen(s + 1);
		reverse(s + 1, s + n + 1);
		for (int i = 1; i <= n; i++) a[i] = s[i] - '0';
		found = 0;
		for (ansn = n; ansn >= n - 1; ansn--) {
			for (int i = 9; i >= 1; i--) {
				if (ansn == n && i > a[ansn]) continue;
				ans[ansn] = i;
				if ((ansn == n && i < a[ansn]) || ansn < n) dfs(ansn - 1, 1);
				else dfs(ansn - 1, 0);
				if (found) break;
			}
			if (found) break;
		}
		static int tc = 0;
		printf("Case #%d: ", ++tc);
		for (int i = ansn; i >= 1; i--) printf("%d", ans[i]);
		puts("");
	}
}