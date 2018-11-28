#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int t, k, ans;
char s[1000+10];
int f[1000+10];

int solve() {
	int n = strlen(s);
	int a, b, cnt = 0;
	for (int i = 0;i <= n;++i)
		f[i] = 0;
	for (int i = 0;i < n;++i) {
		a = i - k >= 0 ? f[i - k] : 0;
		f[i] = i - 1 >= 0 ? f[i - 1] : 0;
		b = (f[i] - a) & 1;
		if ((b == 1 && s[i] == '+') || (b == 0 && s[i] == '-')) {
			f[i] += 1;
			cnt++;
			if (i > n - k) return -1;
		}
	}

	return cnt;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%*c", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%s%d%*c", &s, &k);
		ans = solve();
		printf("Case #%d: ", i);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}