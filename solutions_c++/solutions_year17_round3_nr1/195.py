#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define iter(i, n) for (int i = 1; i <= n; ++i)
#define forw(i, a, b) for (int i = a; i <= b; ++i)

long double pi = M_PI;
#define NR 1010

int r[NR], h[NR], p[NR], n, K;

int main() {
	freopen("A.in", "r", stdin);
	int tt;
	scanf("%d", &tt);
	iter(id, tt) {
		scanf("%d%d", &n, &K);
		iter(i, n) {
			scanf("%d%d", &r[i], &h[i]);
			p[i] = i;
		}
		
		sort(p + 1, p + n + 1, [&](int i, int j) { return 1ll * r[i] * h[i] > 1ll * r[j] * h[j]; });
		long long sum = 0;
		int R = 0;
		
		iter(t, K) {
			int i = p[t];
			sum += 1ll * r[i] * h[i];
			R = max(R, r[i]);
		}

		double ans = pi * R * R + 2 * pi * sum;

		long long tmp = 1ll * r[p[K]] * h[p[K]];

		for (int t = K + 1; t <= n; ++t) {
			int i = p[t];

			if (r[i] > R) {
				ans = max(ans, (double) (pi * r[i] * r[i] + 2 * pi * (sum + 1ll * r[i] * h[i] - tmp)));
			}
		}

		printf("Case #%d: %.10f\n", id, ans);
	}
	return 0;
}