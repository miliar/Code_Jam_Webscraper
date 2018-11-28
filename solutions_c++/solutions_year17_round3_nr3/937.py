#include <stdio.h>

int main()
{
	FILE *in, *out;
	int test, tt, n, k, i, j, a;
	double total, list[50], tmp, d;

	in = fopen("C-small-1-attempt0.in", "r");
	out = fopen("outputCS.txt", "w");

	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		fscanf(in, "%d %d", &n, &k);
		fscanf(in, "%lf", &total);
		for (i = 0;i < n;i++)
			fscanf(in, "%lf", &list[i]);
		for (i = 0;i < n - 1;i++)
		{
			a = i;
			for (j = i + 1;j < n;j++)
				if (list[j] < list[a])
					a = j;
			tmp = list[a];
			list[a] = list[i];
			list[i] = tmp;
		}
		while (total > 0)
		{
			for (a = 1;a<n && list[a] == list[0];a++);
			if (a == n)
			{
				if (total / (double)n>1.0 - list[0])
				{
					for (i = 0;i < n;i++)
						list[i] = 1.0;
					total = 0;
				}
				else
				{
					for (i = 0;i < n;i++)
						list[i] += (total / (double)n);
					total = 0;
				}
			}
			else
			{
				if (total / (double)a>list[a] - list[0])
				{
					tmp = list[a] - list[0];
					for (i = 0;i < a;i++)
						list[i] += tmp;
					total -= (tmp*(double)a);
				}
				else
				{
					for (i = 0;i < a;i++)
						list[i] += (total / (double)a);
					total = 0;
				}
			}
		}
		for (tmp = 1.0, i = 0;i < n;i++)
			tmp *= list[i];
		fprintf(out,"Case #%d: %.6lf\n", tt, tmp);
	}

	fclose(in);
	fclose(out);
	return 0;
}