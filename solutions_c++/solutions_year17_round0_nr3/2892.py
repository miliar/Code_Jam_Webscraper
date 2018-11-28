#include <bits/stdc++.h>

using namespace std;

int t;
long long n, k;

int main() {
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		scanf("%lld %lld", &n, &k);

		long long a = n, b = n, pow2 = 1;
		while (k - pow2 > 0) {
			a = a / 2;
			b = (b - 1) / 2;
			k -= pow2;
			pow2 *= 2;
		}


		if (a != b) {
			long long r = n - pow2 + 1;
			long long x = (r - pow2 * b)/(a - b);
			if (k <= x) {
				b = (a - 1) / 2;
				a = a / 2;
			} else {
				a = b / 2;
				b = (b - 1) / 2;
			}
		} else {
			a = a / 2;
			b = (b - 1) / 2;
		}

		cout << "Case #" << tt + 1 << ": " << a << " " << b << endl;
	}
}