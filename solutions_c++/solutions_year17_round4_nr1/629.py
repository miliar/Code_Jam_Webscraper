#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 110;

int n,p;
int c[4];

inline int solve () {
	scanf ("%d %d", &n, &p);

	for (int i = 0;i < 4;i ++) {
		c[i] = 0;
	}

	for (int i = 0;i < n;i ++) {
		int x;
		scanf ("%d", &x);
		c[x % p] ++;
	}

	int ans = 0,k;
	if (p == 2) {
		k = c[0];
		c[0] -= k;
		ans += k;

		k = c[1] / 2;
		c[1] -= k * 2;
		ans += k;
	} else if (p == 3) {
		k = c[0];
		c[0] -= k;
		ans += k;

		k = min (c[1], c[2]);
		c[1] -= k;
		c[2] -= k;
		ans += k;

		k = c[1] / 3;
		c[1] -= k * 3;
		ans += k;

		k = c[2] / 3;
		c[2] -= k * 3;
		ans += k;
	} else if (p == 4) {
		k = c[0];
		c[0] -= k;
		ans += k;

		k = min (c[1], c[3]);
		c[1] -= k;
		c[3] -= k;
		ans += k;

		k = c[2] / 2;
		c[2] -= k * 2;
		ans += k;

		k = min (c[1] / 2, c[2]);
		c[1] -= k * 2;
		c[2] -= k;
		ans += k;

		k = min (c[2], c[3] / 2);
		c[2] -= k;
		c[3] -= k * 2;
		ans += k;

		k = c[1] / 4;
		c[1] -= k * 4;
		ans += k;

		k = c[3] / 4;
		c[3] -= k * 4;
		ans += k;
	}
	ans += min (1, c[0] + c[1] + c[2] + c[3]);

	return ans;
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: %d\n", i, solve ());
	}
}