#include <stdio.h>
#include <math.h>
int main()
{
	FILE *in, *out;
	int test, tt;
	long long int n, k, h, cnt, div;
	in = fopen("C-small-2-attempt0.in", "r");
	out = fopen("outputCS.txt", "w");
	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		fscanf(in, "%lld %lld", &n, &k);
		h = log2(k) + 1;
		div = pow(2, h - 1);
		n = n - div + 1;
		k = k - div + 1;
		cnt = n%div;
		if (k <= cnt)
		{
			h = n / div + 1;
			if (h % 2 == 0)
				fprintf(out, "Case #%d: %lld %lld\n", tt, h / 2, h / 2 - 1);
			else
				fprintf(out, "Case #%d: %lld %lld\n", tt, h / 2, h / 2);
		}
		else
		{
			h = n / div;
			if (h % 2 == 0)
				fprintf(out, "Case #%d: %lld %lld\n", tt, h / 2, h / 2 - 1);
			else
				fprintf(out, "Case #%d: %lld %lld\n", tt, h / 2, h / 2);
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}