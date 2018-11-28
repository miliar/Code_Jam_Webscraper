#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, p;
int tgroup[200];

void proc(int caseidx) {
	scanf("%d %d", &n, &p);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &tgroup[i]);
	}
	sort(tgroup, tgroup + n);

	int ans = 0;

	int cp = 0;
	for (int i = 0; i < n; ++i) {
		if (tgroup[i] % p == 0) {
			++cp;
		}
	}

	if (p == 2) {
		int c0 = 0, c1 = 0;
		for (int i = 0; i < n; ++i) {
			c0 += (tgroup[i] % 2 == 0) ? 1 : 0;
			c1 += (tgroup[i] % 2 == 1) ? 1 : 0;
		}

		if (c1 % 2)
			ans = 1 + cp + (c1 / 2);
		else
			ans = cp + (c1 / 2);
	}
	else if (p == 3) {
		int c0 = 0, c1 = 0, c2 = 0;
		for (int i = 0; i < n; ++i) {
			c0 += (tgroup[i] % 3 == 0) ? 1 : 0;
			c1 += (tgroup[i] % 3 == 1) ? 1 : 0;
			c2 += (tgroup[i] % 3 == 2) ? 1 : 0;
		}

		ans = cp;
		int t = min(c1, c2);
		ans += t;
		c1 -= t;
		c2 -= t;
		ans += c1 / 3;
		ans += c2 / 3;
		c1 %= 3;
		c2 %= 3;
		if (c1 || c2)
			++ans;
	}
	else if (p == 4) {
		int c0 = 0, c1 = 0, c2 = 0, c3 = 0;
		for (int i = 0; i < n; ++i) {
			c0 += (tgroup[i] % 4 == 0) ? 1 : 0;
			c1 += (tgroup[i] % 4 == 1) ? 1 : 0;
			c2 += (tgroup[i] % 4 == 2) ? 1 : 0;
			c3 += (tgroup[i] % 4 == 3) ? 1 : 0;
		}

		ans = cp;

		int t1 = min(c1, c3);
		ans += t1;
		c1 -= t1;
		c3 -= t1;

		ans += (c2 / 2);
		c2 %= 2;

		int t2 = min(c1 / 2, c2);
		ans += t2;
		c1 -= 2 * t2;
		c2 -= t2;

		ans += c1 / 4;
		c1 %= 4;

		if (c1 || c2 || c3)
			++ans;
	}

	printf("Case #%d: %d\n", caseidx, ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}