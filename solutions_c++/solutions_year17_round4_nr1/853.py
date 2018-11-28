#include<stdio.h>
int in[4];
int solve() {
	int n, p, t, c=0;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < p; i++) in[i] = 0;
	for (int i = 1; i <= n; i++) {
		scanf("%d", &t);
		in[t%p] ++;
	}
	c += in[0];
	if (p == 2) {
		c += (in[1] + 1) / 2;
		return c;
	}
	if (p == 3) {
		int m = in[1] > in[2] ? in[2] : in[1];
		c += m;
		in[1] -= m; in[2] -= m;
		if (in[1] != 0) c += (in[1] - 1) / 3 + 1;
		if (in[2] != 0) c += (in[2] - 1) / 3 + 1;
		return c;
	}
	if (p == 4) {
		int m = in[1] > in[3] ? in[3] : in[1];
		c += m;
		int r = in[1] + in[3] - m - m;
		int max = 0;
		for (int x = 0; x <= r; x += 2) {
			if (in[2] < x/2) continue;
			int t = x / 2 + (in[2] - x/2) / 2 + (r-x)/4;
			if ((in[2] - x / 2) % 2 != 0 || (r - x) % 4 != 0) t++;
			if (t > max) max = t;
		}
		return c + max;
	}
	return 0;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: %d\n", tt, solve());
	}
	return 0;
}

/*
a 1 2
b 1 1 1
c 2 2 2

a+3b <= x
a+3c <= y
a+b+c;
*/

/*
a 2 2
b 1 3
c 1 1 2
d 2 3 3
e 1 1 1 1
f 2 2 2 2
g 3 3 3 3*/