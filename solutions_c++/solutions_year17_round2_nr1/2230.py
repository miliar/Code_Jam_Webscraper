#include <stdio.h>

int main()
{
	FILE *in, *out;
	int test, tt, n, i, j;
	double ans, max, cal, d, list[1000][2];

	in = fopen("A-large.in", "r");
	out = fopen("outputAL.txt", "w");

	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		max = 0;
		fscanf(in, "%lf %d", &d, &n);
		for (i = 0;i < n;i++)
			fscanf(in, "%lf %lf", &list[i][0], &list[i][1]);
		for (i = 0;i < n;i++)
		{
			cal = (d - list[i][0]) / list[i][1];
			if (cal > max)
				max = cal;
		}
		fprintf(out, "Case #%d: %.6lf\n", tt, d / max);
	}

	fclose(in);
	fclose(out);
	return 0;
}