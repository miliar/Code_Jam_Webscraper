/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int d, n, i;
		scanf("%d %d", &d, &n);

		long long best_k = -1, best_s = 0;
		for (i = 0; i < n; i++) {
			int k, s;
			scanf("%d %d", &k, &s);
			if ((d - k) * best_s > best_k * s) best_k = (d - k), best_s = s;
		}

		printf("Case #%d: %0.6f\n", K, (double)d * best_s / best_k);
		K++;
	}
	return 0;
}
