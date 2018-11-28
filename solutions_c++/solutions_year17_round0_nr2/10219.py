#include <stdio.h>
FILE *fp1 = fopen("input.txt", "r");
FILE *fp2 = fopen("output.txt", "w");
void main()
{
	int i,t,k,n,a[20],temp,x,y,j;
	fscanf(fp1,"%d", &t);
	for (k = 1; k <= t; k++)
	{
		fscanf(fp1,"%d", &n);
		for (i = n; i >= 1; i--)
		{
			x = i; y = 0;
			while (1)
			{
				if (x <= 0) break;
				y++; a[y] = x % 10; x /= 10;
			}
			for (j = 1; j < y; j++)
			{
				if (a[j] < a[j + 1]) break;
			}
			if (j == y)
			{
				fprintf(fp2,"CASE #%d: %d\n", k, i); break;
			}
		}
	}
	fclose(fp1);
	fclose(fp2);
}