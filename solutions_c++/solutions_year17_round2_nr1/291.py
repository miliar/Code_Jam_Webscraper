#include <cstdio>

using namespace std;

int N, D;
int K[1005], S[1005];

double solve();

int main() {
	int tc;
	scanf("%d", &tc);

	for (int t = 1; t <= tc; ++t) {
		scanf("%d %d", &D, &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &K[i], &S[i]);
		}

		double ans = solve();
		printf("Case #%d: %.9f\n", t, ans);
	}

	return 0;
}

double solve() {
	double l = 1, r = 5e+15;

	for (int i = 0; i < 100; ++i) {
		double mid = (l + r) / 2;
		int j;

		for (j = 0; j < N; ++j) {
			if (S[j] >= mid) continue;
			// K[j] + S[j] * t = mid * t
			const double t = K[j] / (double)(mid - S[j]);
			//printf("%g\n", t);

			if (mid * t < D) break;
		}

		if (j == N) {
			l = mid;
		} else {
			r = mid;
		}
	}

	return (l + r) / 2;
}