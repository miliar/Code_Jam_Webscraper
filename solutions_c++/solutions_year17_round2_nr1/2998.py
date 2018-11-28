#include <cstdio>
#include <algorithm>

int main () {
	int t, d, n, k, s;
	double slower;
	scanf ("%d", &t);

	for (int l = 1; l <= t; l++) {
		scanf ("%d %d", &d, &n);

		slower = 0;
		for (int i = 0; i < n; i++) {
			scanf ("%d %d", &k, &s);
			slower = std::max (slower , (d-k)/(double)s);
		}

		printf ("Case #%d: %.6lf\n", l, d/slower);
	}

	return 0;
}
