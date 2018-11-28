#include <stdio.h>
char list[1001],l;
int flip(int start, int len)
{
	int i;
	if (start + len > l)
		return 0;
	for (i = start;i < start + len;i++)
	{
		if (list[i] == '+')
			list[i] = '-';
		else
			list[i] = '+';
	}
	return 1;
}
int main()
{
	FILE *in, *out;
	int test, ii, i, k,cnt;
	in = fopen("A-small-attempt0.in", "r");
	out = fopen("outputAS.txt", "w");
	fscanf(in,"%d", &test);
	for (ii = 1;ii <= test;ii++)
	{
		fscanf(in,"%s", list);
		fscanf(in,"%d", &k);
		cnt = 0;
		for (l = 0;list[l] != NULL;l++);
		for (i = 0;i <= l - k;i++)
			if (list[i] == '-')
			{
				if (flip(i, k) == 1)
					cnt++;
				else
					break;
			}
		for (i = 0;i < l;i++)
			if (list[i] == '-')
				break;
		if (i != l)
			fprintf(out,"Case #%d: IMPOSSIBLE\n",ii);
		else
			fprintf(out,"Case #%d: %d\n", ii,cnt);
	}
	fclose(in);
	fclose(out);
	return 0;
}