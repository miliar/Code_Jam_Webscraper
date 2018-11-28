/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve() {
	long long n, k;
	cin >> n >> k;
	long long i = 1, shift = 0;
	fprintf(stderr, "[n=%lld,k=%lld]\n", n, k);
	while (i < k) {
		fprintf(stderr, "[n=%lld,k=%lld,i=%lld]\n", n, k, i);
		k -= i;
		i *= 2, shift++;
	}
	long long cnt = 1, all = 1;
	for (int j = 0; j < shift; j++, all *= 2) 
		if ((n >> j) % 2 != 0)
			cnt = cnt * 2 + (all - cnt);
	// printf("[cnt=%d] ", cnt);
	long long len = (n >> shift) - (cnt < k) - 1;
	long long l = len / 2, r = len - l;
	printf("%lld %lld\n", max(l, r), min(l, r));
}

int main() {
	int tn;
	cin >> tn;
	for (int t = 1; t <= tn; t++) {
		fprintf(stderr, "test %d\n", t);
		printf("Case #%d: ", t);
		solve();
	}
}
