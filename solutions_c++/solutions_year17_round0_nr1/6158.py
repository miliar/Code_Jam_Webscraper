#include<cstdio>

int n, k, a;
char s[1005];

bool check() {
	for (int i = 0; s[i]; i++) if (s[i] == '-') return false;
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &n);
	while (n --> 0) {
		scanf("%s %d", s, &k);
		int ans = 0;
		for (int i = 0; s[i + k - 1]; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < k; j++) {
					if(s[i + j] == '+') s[i + j] = '-';
					else s[i + j] = '+';
				}
				ans++;
			}
		}
		if (check()) printf("Case #%d: %d\n", ++a, ans);
		else printf("Case #%d: IMPOSSIBLE\n", ++a);
	}
}
