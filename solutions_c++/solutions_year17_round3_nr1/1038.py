#include <stdio.h>
#include <stdlib.h>

#define M_PI 3.14159265358979323846

const int maxn = 1050;

int n, k;
double r[maxn], h[maxn];
int index[maxn];
double d[maxn][maxn];

int cmp(const void *a, const void *b)
{
	if (r[*(int*)b] - r[*(int*)a] > 0) return 1;
	return -1;
}

double mymax(double a, double b)
{
	if (a >= b) return a;
	return b;
}

void process()
{
	int i, j;

	for (i = 0; i < n; i++)
		index[i] = i;
	qsort(index, n, sizeof(int), cmp);
	d[1][1] = M_PI * (r[index[0]] * r[index[0]] + 2 * r[index[0]] * h[index[0]]);
	for (i = 1; i < n; i++)
		d[1][i+1] = mymax(d[1][i], M_PI * (r[index[i]] * r[index[i]] + 2 * r[index[i]] * h[index[i]]));
	for (i = 2; i <= k; i++)
	{
		for (j = i; j <= n; j++)
			d[i][j] = mymax(d[i][j - 1], d[i - 1][j - 1] + M_PI * 2 * r[index[j - 1]] * h[index[j - 1]]);
	}
}

int main()
{
	int i, casecnt, casen;

	scanf("%d", &casen);

	for(casecnt = 1; casecnt <= casen; casecnt++)
	{
		printf("Case #%d: ", casecnt);
		scanf("%d %d", &n, &k);
		for (i = 0; i < n; i++)
			scanf("%lf %lf", &r[i], &h[i]);
		process();
		printf("%.9lf\n", d[k][n]);
	}

	return 0;
}