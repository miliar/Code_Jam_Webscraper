#include <stdio.h>
#include <stdlib.h>

const int maxn = 55;

int n, k;
double u, ans;
double p[maxn];
int index[maxn];

int cmp(const void *a, const void *b)
{
	if (p[*(int*)a] - p[*(int*)b] < 0) return -1;
	return 1;
}

void process()
{
	int i, j;
	double rem;

	for (i = 0; i < n; i++)
		index[i] = i;
	qsort(index, n, sizeof(int), cmp);
	if (u < 1e-10)
	{
		ans = p[0];
		for (i = 1; i < n; i++)
			ans *= p[i];
		return;
	}
	rem = 0;
	for (i = 0; i < n; i++)
		rem += 1 - p[i];
	if (rem - u < 1e-10)
	{
		ans = 1;
		return;
	}
	for (i = 0; i < n - 1; i++)
	{
		if ((i + 1) * (p[index[i + 1]] - p[index[i]]) < u)
		{
			u -= (i + 1) * (p[index[i + 1]] - p[index[i]]);
			for (j = 0; j <= i; j++)
				p[index[j]] = p[index[i + 1]];
		}
		else
		{
			for (j = 0; j <= i; j++)
				p[index[j]] += u / (i + 1);
			break;
		}
	}
	if (i >= n - 1 && u > 0)
	{
		for (i = 0; i < n; i++)
			p[i] += u / n;
	}
	ans = p[0];
	for (i = 1; i < n; i++)
		ans *= p[i];
}

int main()
{
	int i, casecnt, casen;

	scanf("%d", &casen);

	for (casecnt = 1; casecnt <= casen; casecnt++)
	{
		printf("Case #%d: ", casecnt);
		scanf("%d %d", &n, &k);
		scanf("%lf", &u);
		for (i = 0; i < n; i++)
			scanf("%lf", &p[i]);
		process();
		printf("%.6lf\n", ans);
	}

	return 0;
}