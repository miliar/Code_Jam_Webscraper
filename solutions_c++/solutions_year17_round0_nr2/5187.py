#include <stdio.h>
long long int list[19];
void sub(int index)
{
	if (list[index] > 0)
		list[index]--;
	else
	{
		list[index] = 9;
		sub(index - 1);
	}
}
int main()
{
	FILE *in, *out;
	int tt, test, i, j, start;
	long long int n;
	in = fopen("B-large.in", "r");
	out = fopen("outputBL.txt", "w");
	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		fscanf(in, "%lld", &n);
		for (i = 0;i < 19;i++)
			list[i] = -1;
		for (i = 18;n > 0;i--, n /= 10)
			list[i] = n % 10;
		start = i + 1;
		i = 17;
		while (1)
		{
			while (i >= start && list[i] <= list[i + 1])
				i--;
			if (i < start)
				break;
			sub(i);
			for (j = i + 1;j < 19;j++)
				list[j] = 9;
			i--;
		}
		for (n = 0, i = start;i < 19;n = n * 10 + list[i], i++);
		fprintf(out, "Case #%d: %lld\n", tt, n);
	}
	return 0;
}