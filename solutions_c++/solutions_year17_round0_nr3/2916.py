#include <bits/stdc++.h>
using namespace std;

long long N, K, n, k;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int A = 1; A <= t; A++) {
		cin >> N >> K;
		n = N;
		K--;
		k = K;
		long long i = 0;
		while (k >= (1LL << i)) {
			k -= (1LL << i);
			n = (n - 1) / 2;
			i++;
		}
		long long rem = (N - K + k) - n * (1LL << i);

		if (k < rem)
			n++;

		long long m = (n + 1) / 2;
		long long ls = m - 1, rs = n - ls - 1;
		printf("Case #%d: %lld %lld\n", A, max(ls, rs), min(ls, rs));
	}

	return 0;
}
