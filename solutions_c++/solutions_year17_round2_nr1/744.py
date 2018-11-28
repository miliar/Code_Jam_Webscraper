#include <cstdio>
#include <cstdlib>
#include <algorithm>

const int MAXN = 10007;

int b[MAXN], s[MAXN];

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int d, n;
		scanf("%d%d", &d, &n);
		double ans = 1e14;
		for (int i = 1; i <= n; ++i) {
			scanf("%d%d", &b[i], &s[i]);
			if (b[i] >= d) continue;
			ans = std::min(ans, 1.0 * d * s[i] / (d - b[i]));
		}
		printf("Case #%d: %.9f\n", Case, ans);
	}
	return 0;
}
