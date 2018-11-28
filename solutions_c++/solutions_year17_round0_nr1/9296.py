#include<bits/stdc++.h>
using namespace std;
const int N = 1111;
bool vis[N];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(vis, false, sizeof vis);
		int k;
		char s[1111];
		scanf(" %s%d", s, &k);

		int len = strlen(s);
		bool cnt = false;
		int ans = 0;
		for (int i = 0; i < len; i++) {
			bool bit = ((s[i] == '+') ^ cnt);

			if (bit) {
				if (vis[i]) {
					cnt ^= 1;
				}
				continue;
			}
			if (i + k - 1 >= len) {
				break;
			}
			++ans;
			cnt ^= 1;
			vis[i + k - 1] = true;
			if (vis[i]) {
				cnt ^= 1;
			}
		}
		cnt = false;
		bool ok = true;
		for (int i = 0; i < k - 1; i++) {
			if (vis[len - i - 1]) {
				cnt ^= 1;
			}
			bool bit = ((s[len - i - 1] == '+') ^ cnt);
			if (!bit) {
				ok = false;
				break;
			}
		}
		if (ok) {
			printf("Case #%d: %d\n", t, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
