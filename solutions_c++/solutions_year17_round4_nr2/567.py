#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

int s[1010], a[1010], p[1010], TT, n, c, m;

int main() {

	scanf("%d", &TT);
	for (int T = 1; T <= TT; T++) {
		printf("Case #%d: ",T);

		memset(a, 0, sizeof(a));
		memset(s, 0, sizeof(s));
		memset(p, 0, sizeof(p));

		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
			a[x]++;
			p[y]++;
		}
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			s[i] = s[i - 1] + a[i];
			ans = max(ans, int(ceil(double(s[i]) / i)));
		}
		for (int i = 1; i <= c; i++) {
			ans = max(ans, p[i]);
		}
		int ans2 = 0;
		for (int i = 1; i <= n; i++) {
			ans2 += max(a[i] - ans, 0);
		}
		printf("%d %d\n", ans, ans2);
	}

	return 0;
}