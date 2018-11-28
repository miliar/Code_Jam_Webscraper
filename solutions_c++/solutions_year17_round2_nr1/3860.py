#include <stdio.h>

int main ()
{
	int n, t;
	double d, a, b, max;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%lf%d", &d, &n);
		for (int j = 1; j <= n; j++)
		{
			scanf("%lf%lf", &a, &b);
			double x = (d - a)/b;
			// printf("%lf %lf %lf\n", a, b, x);
			if (x > max || j == 1)
				max = x;
		}
		printf("Case #%d: %lf\n", i, d/max);
	}

	return 0;
}