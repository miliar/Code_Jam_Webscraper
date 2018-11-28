#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

char s[N];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		int k;
		scanf("%s %d", s, &k);
		int n = strlen(s);
		bool ok = true;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == '-') {
				ans++;
				if (i <= n - k) {
					for (int j = i; j < i + k; j++) {
						s[j] = (s[j] == '-' ? '+' : '-');
					}
				} else {
					ok = false;
					break;
				}
			}
		}
		if (ok) {
			printf("%d\n", ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
