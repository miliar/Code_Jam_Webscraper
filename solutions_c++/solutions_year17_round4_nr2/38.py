#include <cstdio>
#include <vector>

using namespace std;

int a[1001], b[1001];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		int i, j, n, m, l, r = 0;
		scanf("%d%d%d", &n, &m, &l);
		for (i = 1; i <= 1000; i++) a[i] = b[i] = 0;
		while (l--) {
			scanf("%d%d", &i, &j);
			a[i]++;
			b[j]++;
		}
		for (i = 1; i <= 1000; i++) {
			a[i] += a[i - 1];
			if ((a[i] + i - 1) / i > r) r = (a[i] + i - 1) / i;
			if (b[i] > r) r = b[i];
		}
		l = 0;
		for (i = 1; i <= 1000; i++) if (a[i] - a[i - 1] > r) l += a[i] - a[i - 1] - r;
		printf("Case #%d: %d %d\n", T, r, l);
	}
	return 0;
}