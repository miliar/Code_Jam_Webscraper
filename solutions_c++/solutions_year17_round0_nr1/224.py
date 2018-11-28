#include <bits/stdc++.h>
using namespace std;

const int MOD = int(1e9 + 7);

char s[1111];
int n, k, f[1111];

void solve() {
	scanf("%s%d", s, &k);
	n = strlen(s);
	int res = 0, flip = 0;
	memset(f, 0, sizeof f);
	for (int i = 0; i < n; i++) {
		int cake = (s[i] == '-');
		flip ^= f[i];
		// printf("cake %d: %d\n", i, cake^flip);
		if (flip^cake) {
			// need flip
			if (i+k <= n) {
				res++;
				flip ^= 1;
				f[i+k] = 1;
			} else {
				res = -1;
				break;
			}
		}
	}
	if (res >= 0) printf("%d\n", res);
	else printf("IMPOSSIBLE\n");
}

int main() {
	freopen("A.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}