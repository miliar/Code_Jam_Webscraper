#include<stdio.h>

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t, test;
	scanf("%d", &test);
	for (t = 1; t <= test; t++) {
		long long a, b, an, bn, n, k, two = 1;
		scanf("%I64d%I64d", &n, &k);
		if (k == 1) {
			printf("Case #%d: %I64d %I64d\n", t, n / 2, (n - 1) / 2);
			continue;
		}
		a = n, b = n + 1, an = 1, bn = 0;
		while (1) {
			k -= two, two *= 2;
			if (a % 2 == 0) {
				b = a / 2, a = (a-1) / 2;
				bn = 2 * bn + an;
			}
			else {
				a = (b - 1) / 2, b = b / 2;
				an = 2 * an + bn;
			}
			if (two >= k) {
				if (bn >= k) 
					printf("Case #%d: %I64d %I64d\n", t, b / 2, (b - 1) / 2);
				else 
					printf("Case #%d: %I64d %I64d\n", t, a / 2, (a - 1) / 2);
				break;
			}
		}
	}
	return 0;
}