#include <bits/stdc++.h>

using namespace std;

char s[1010];
int x[1010];
int v[1010];
int k;

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%s %d", s, &k);
		int n = strlen(s);
		for (int i = 0; i < n; ++i) {
			v[i] = s[i] == '+';
			x[i] = 0;
		}
		int ans = 0;
		bool can = true;
		int z = 0;
		for (int i = 0; can && i < n; ++i) {
			z ^= x[i];
			if (z ^ v[i] == 0) {
				if (i + k > n) {
					can = false;
				} else {
					z ^= 1;
					x[i + k] ^= 1;
					++ans;
				}
			}
		}
		printf("Case #%d: ", tc);
		if (can) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}