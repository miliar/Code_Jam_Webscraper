#include <cstdio>

int main() {
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		unsigned long long n, t, f, a, x;
		scanf("%lld", &n);

		bool done = false;
		while (!done) {
			done = true;


			f = 1;
			for (int i = 0; i < 18; i++) {
				f *= 10;
			}

			while (f != 0) {
				int x = n / f;
				if (x != 0) {
					break;
				}
				n -= x * f;
				f /= 10;
			}

			a = -1;
			t = 0;
			while (f != 0) {
				x = n / f;

				// printf("%lld %lld %lld %lld %lld\n", n, t, f , a, x);

				if (a == -1) {
					a = x;
				} else {
					if (a <= x) {
						t += a * f * 10;
						a = x;
					} else {
						done = false;
						t  += (a - 1) * f * 10;
						a = -1;
						while (f != 0) {
							t += 9 * f;
							f /= 10;
						}
						break;
					}
				}
				n -= x * f;
				f /= 10;
			}
			if ( a != -1) {
				t += a * f * 10 + x;
			}
			n = t;

			// printf("%lld\n", t);
		}

		printf("Case #%d: %lld\n", ++ca, t);
	}
	return 0;
}
