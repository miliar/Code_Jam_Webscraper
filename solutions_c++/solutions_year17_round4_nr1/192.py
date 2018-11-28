#include <cstdio>


int max(int a, int b) { return a > b ? a : b; }
int min(int a, int b) { return a < b ? a : b; }

int solve2(int *r) {
	return r[0] + (r[1] + 1) / 2;
}

int solve3(int* r) {
	int m1 = r[0];
	int m2 = min(r[1], r[2]);
	r[1] -= m2;
	r[2] -= m2;
	int m3 = (r[1] + 2) / 3 + (r[2] + 2) / 3;
	return m1 + m2 + m3;
}

int solve4(int* r) {
	int m1 = r[0];
	int m2 = min(r[1], r[3]);
	r[1] -= m2;
	r[3] -= m2;
	m2 += r[2] / 2;
	r[2] %= 2;
	int m3 = 0;
	if (r[2] >= 1) {
		if (r[1] >= 2) {
			m3 = 1;
			r[2] -= 1;
			r[1] -= 2;
		} else if (r[3] >= 2) {
			m3 = 1;
			r[2] -= 1;
			r[3] -= 2;
		}
	}
	int m4 = (r[1] + 3) / 4 + (r[3] + 3) / 4;
	m4 = max(m4, r[2]);
	return m1 + m2 + m3 + m4;
}

int solve(int p, int* r) {
	if (p == 2) return solve2(r);
	if (p == 3) return solve3(r);
	return solve4(r);
}

int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		int n, p;
		scanf("%d%d", &n, &p);
		int r[5] = {0};
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			r[x % p]++;
		}
		printf("Case #%d: %d\n", tc, solve(p, r));
	}
	return 0;
}

