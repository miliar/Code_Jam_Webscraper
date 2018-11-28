#include <bits/stdc++.h>

using namespace std;

int n, g[101], p;
int d[4];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		scanf("%d %d", &n, &p);
		memset(d, 0, sizeof(d));
		for (int i = 0; i < n; ++i) {
			scanf("%d", &g[i]);
			d[g[i]%p]++;
		}

		if (p == 2) 
			printf("Case #%d: %d\n", test, n-d[1]/2);
		else if (p == 3) {
			int c = min(d[1], d[2]);
			n -= c;
			d[1] -= c;
			d[2] -= c;
			n -= 2*(d[1]/3);
			n -= 2*(d[2]/3);
			d[1] %= 3;
			d[2] %= 3;
			if (d[1] > 1) --n;
			if (d[2] > 1) --n;
			printf("Case #%d: %d\n", test, n);
		}
	}
	return 0;
}
