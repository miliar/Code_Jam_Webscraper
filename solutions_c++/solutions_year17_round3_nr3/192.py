#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define iter(i, n) for (int i = 1; i <= n; ++i)
#define forw(i, a, b) for (int i = a; i <= b; ++i)
#define back(i, a, b) for (int i = b; i >= a; --i)

#define NR 100

typedef double ld;
int tt, n, K;
ld U, a[NR], f[NR], h[NR];

int main() {
	freopen("C.in", "r", stdin);
	scanf("%d", &tt);
	iter(id, tt) {
		scanf("%d%d%lf", &n, &K, &U);
		iter(i, n) scanf("%lf", &a[i]);
		sort(a + 1, a + n + 1);
		a[n + 1] = 1;
		iter(i, n + 1) {
			ld d = a[i] - a[i - 1];
			if (d * (i - 1) <= U) {
				iter(k, i - 1) a[k] = a[i];
				U -= d * (i - 1);
			} else {
				iter(k, i - 1) a[k] += U / (i - 1);
				break;
			}
		}

		ld ans = 1;
		iter(i, n) ans *= a[i];

		printf("Case #%d: %.10f\n", id, ans);
	}
	return 0;
}