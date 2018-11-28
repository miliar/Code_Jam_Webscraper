#include <iostream>

void C(int cas) {
	unsigned long long Q[2000][2] = { 0 }, head = 0, tail = 0, n, k, x;
	scanf("%llu%llu", &n, &k);
	Q[tail][0] = n;
	Q[tail++][1] = 1;
	while (head < tail) {
		unsigned long long top = Q[head][0], cnt = Q[head][1];
		head++;
		if (k <= cnt) {
			printf("Case #%d: %llu %llu\n", cas, top / 2, (top - 1) / 2);
			return;
		}
		k -= cnt;
		x = top / 2;
		if (Q[tail - 1][0] != x) {
			Q[tail++][0] = x;
		}
		Q[tail - 1][1] += cnt;
		x = (top - 1) / 2;
		if (Q[tail - 1][0] != x) {
			Q[tail++][0] = x;
		}
		Q[tail - 1][1] += cnt;
	}
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		C(i);
	}
}