#include <cstdio>
#include <cmath>

const double eps = 1e-7;

int main() {
	int T, D, N, K[1024], S[1024], tt;
	double l, r, mid, t[1024];
	bool OK;

	scanf("%d", &T);
	for (int C = 1; C <= T; C++) {
		scanf("%d%d", &D, &N);
		l = r = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d%d", &K[i], &S[i]);
			t[i] = (D - K[i] + .0) / S[i];
			r = fmax(r, D / t[i]);
		}
		tt = 0;
		while (l + eps < r && tt++ < 1000) {
			mid = (l + r) * .5;
			OK = true;
			for (int i = 0; i < N; i++) {
				if (D < t[i] * mid) {
					OK = false;
					break;
				}
			}
			if (OK) {
				l = mid;
			} else {
				r = mid;
			}
		}
		printf("Case #%d: %.8lf\n", C, l);
	}
	return 0;
}
