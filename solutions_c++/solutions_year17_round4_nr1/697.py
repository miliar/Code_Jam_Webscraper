#include<cstdio>

int t, n, p, g, s[10];

int min(int x, int y) {
	return x < y ? x : y;
}

int max(int x, int y) {
	return x > y ? x : y;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d %d", &n, &p);
		for (int i = 0; i < p; i++) s[i] = 0;
		for (int i = 0; i < n; i++) {
			int g;
			scanf("%d", &g);
			s[g % p]++;
		}
		int ans = s[0];
		if (p == 2) {
			ans += s[1] / 2;
			if (s[1] % 2) ans++;
		}
		else if (p == 3) {
			int s1 = s[1], s2 = s[2];
			ans += s1 / 3 + s2 / 3;
			s1 %= 3;
			s2 %= 3;
			ans += min(s1, s2);
			if (s1 != s2) ans++;
			s1 = s[1], s2 = s[2];
			int ans2 = s[0] + min(s1, s2);
			if (s1 < s2) {
				s2 -= s1;
				ans2 += s2 / 3;
				if (s2 % 3) ans2++;
			}
			else {
				s1 -= s2;
				ans2 += s1 / 3;
				if (s1 % 3) ans2++;
			}
			ans = max(ans, ans2);
			// 1 1 1, 2 2 2
			// 1 2
		}
		else {
			// 1 1 1 1
			// 1 1 2
			// 1 3
			// 2 2
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
