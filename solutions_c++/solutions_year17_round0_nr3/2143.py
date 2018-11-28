#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int t;
long long n, k;
long long ma, mi;


long long solve() {
	long long a, b, ca, cb, now, a1, b1, ca1, cb1;
	a = b = n;
	ca = 1; cb = 0;
	now = 0;
	while (now + ca + cb < k) {
		now += ca + cb;
		a1 = a - 1 - (a - 1) / 2;
		b1 = (b - 1) / 2;
		if ((a - 1) / 2 == a1) {
			ca1 = 2 * ca + cb;
			cb1 = cb;
		} else {
			ca1 = ca;
			cb1 = ca + 2 * cb;
		}
		ca = ca1; cb = cb1;
		a = a1; b = b1;
	}
	if (now + ca >= k) {
		ma = a - 1 - (a - 1) / 2;
		mi = (a - 1) / 2;
	}else {
		ma = b - 1 - (b - 1) / 2;
		mi = (b - 1) / 2;
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%lld%lld", &n, &k);
		solve();
		printf("Case #%d: ", i);
		printf("%lld %lld\n", ma, mi);
	}

	return 0;
}