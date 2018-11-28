#include <stdio.h>
#include <stdlib.h>
int main()
{
	int t, tt, d, n, i;
	int *k, *s;
	double *time;
	double max, ans;
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &d, &n);
		k = (int*)malloc(sizeof(int)*n);
		s = (int*)malloc(sizeof(int)*n);
		time = (double*)malloc(sizeof(double)*n);
		for (i = 0; i < n; i++)
		{
			scanf("%d %d", &k[i], &s[i]);
		}
		time[0] = (double)(d - k[0]) / (double)(s[0]);
		max = time[0];
		for (i = 1; i < n; i++)
		{
			time[i] = (double)(d - k[i]) / (double)(s[i]);
			if (max < time[i]) max = time[i];
		}
		ans = (double)d / max;

		printf("Case #%d: %.6f\n", tt, ans);

	}
	return 0;
}