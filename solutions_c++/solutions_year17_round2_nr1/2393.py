#include <cstdio>

int T, n;
int k[1013], s[1013], d;

int main(){
	scanf("%d", &T);
	for (int Case = 0; Case < T; Case++) {
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &k[i], &s[i]);
			
		}

		long double l, r;
		l = 1.0;
		r = 20000.0 * d;

		while (r - l > 1e-6) {
			long double m = l + (r - l) / 2.0;
			bool ans = true;

			for (int i = 0; i < n; i++) {
				if (m < s[i]) {
					continue;
				}

				long double t = k[i] / (m - s[i]);

				if (m * t < d) {
					ans = false;
					break;
				}
			}

			if (ans) {
				l = m;
			} else {
				r = m;
			}
		}

		printf("Case #%d: %.6Lf\n", Case+1, l);
	
	}
}
