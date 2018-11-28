#include <cstdio>

int main () {
	int t;
	long long int n, e, a, b;
	scanf ("%d", &t);
	for (int k = 1; k <= t; k++) {
		scanf ("%lld", &n);
		if (n < 10) {
			printf ("Case #%d: %lld\n", k, n);
			continue;
		}

		e = 10;

		while (e <= n) {
			a = (n%(e*10))/e;
			b = n%e/(e/10);
			
//			printf ("[n->%lld](a=%lld)(b=%lld)(e=%lld)", n, a, b, e);

			if (a > b)
				n = n - (n%e) - 1;

//			printf("[n<-%lld]\n", n);
			e *= 10;
		}

		printf ("Case #%d: %lld\n", k, n);
	}

	return 0;
}
