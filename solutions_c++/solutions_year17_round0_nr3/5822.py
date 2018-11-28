#include < stdio.h>
#include < string.h>

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);

	long long t, n, k, i, j, min, max, cur, cnt, l, r, st, d, q, a[1005];

	scanf("%lli", &t);

	for (i = 0; i < t; i++)
	{
		scanf("%lli %lli", &n, &k);

		a[0] = a[n + 1] = 1;
		for (j = 1; j <= n; j++)
			a[j] = 0;

		for (q = 0; q < k; q++)
		{
			min = max = 1000;
			cur = cnt = 0;
			st = 1;
			for (j = 1; j <= n + 1; j++)
				if (a[j] == 0)
					cnt++;
				else if (cnt > cur)
				{
					cur = cnt;
					l = st;
					r = j - 1;
					cnt = 0;
					st = j + 1;
				}
				else
				{
					st = j + 1;
					cnt = 0;
				}

			d = r - l + 1;

			max = d / 2;
			min = (d - 1) / 2;
			a[l + min] = 1;
		}

		printf("Case #%lli: %lli %lli\n", i + 1, max, min);
	}		

	return 0;
}