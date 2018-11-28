#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		long long n, k;
		scanf("%lld %lld", &n, &k);

		long long big = 1ll;
		long long weak = 0ll;

		while (k > 0) {
			if (k - big <= 0) {
				printf("%lld %lld\n", n / 2, max(0ll, (n - 1 - n / 2)));
				break;
			}

			k -= big;

			if (k - weak <= 0) {
				n--;
				printf("%lld %lld\n", n / 2, max(0ll, (n - 1 - n / 2)));
				break;
			}

			k -= weak;

			if (n & 1) {
				big <<= 1;
				big += weak;
			} else {
				weak <<= 1;
				weak += big;
			}

			n = n / 2;
		}
	}

	return 0;
}
