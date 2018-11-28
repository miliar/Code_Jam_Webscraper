#include <stdio.h>
int n,co[6],list[1000]; //R0,O1,Y2,G3,B4,V5

int check(int a, int b)
{
	if (co[0] + 1 >= co[2] + co[4])
		return 0;
	if (co[2] + 1 >= co[0] + co[4])
		return 0;
	if (co[4] + 1 >= co[2] + co[0])
		return 0;
	switch (a)
	{
	case 0:
		if (b == 2 || b == 3 || b == 4)
			return 1;
		else
			return 0;
	case 1:
		if (b == 4)
			return 1;
		else 
			return 0;
	case 2:
		if (b == 0 || b == 4 || b == 5)
			return 1;
		else
			return 0;
	case 3:
		if (b == 0)
			return 1;
		else
			return 0;
	case 4:
		if (b == 0 || b == 1 || b == 2)
			return 1;
		else
			return 0;
	case 5:
		if (b == 2)
			return 1;
		else
			return 0;
	}
}

int main()
{
	FILE *in, *out;
	int test, tt, i, j,start,left,right,m;

	in = fopen("B-small-attempt4.in", "r");
	//in = fopen("input.txt", "r");
	out = fopen("outputBS.txt", "w");

	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		fscanf(in, "%d %d %d %d %d %d %d", &n, &co[0], &co[1], &co[2], &co[3], &co[4], &co[5]);
		for (i = 0;i < n;i++)
			list[i] = -1;

		for (j = 0, m = 0;m < 6;m++)
			if (co[m]>co[j])
				j = m;
		for (i = 0;i < n && co[j]>0;i += 2)
		{
			list[i] = j;
			co[j]--;
		}
		if (co[j] > 0)
		{
			fprintf(out, "Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}

		i--;
		for (j = 0, m = 0;m < 6;m++)
			if (co[m]>co[j])
				j = m;
		while (i < n && co[j]>0)
		{
			list[i] = j;
			co[j]--;
			i += 2;
		}
		if (co[j]>0)
		{
			for (i = 1;i < n && co[j]>0;i += 2)
			{
				if (list[i] != j)
				{
					list[i] = j;
					co[j]--;
				}
				else
					break;
			}
			if (co[j] > 0)
			{
				fprintf(out, "Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
		}

		for (i = 0;i < n;i++)
			if (list[i] == list[(i + 1)%n])
				break;
		if (i<n)
		{
			fprintf(out, "Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		else
		{
			for (j = 0, m = 0;m < 6;m++)
				if (co[m]>co[j])
					j = m;
			for (i = 0;i < n;i++)
				if (list[i] == -1)
					list[i] = j;
		}

		fprintf(out, "Case #%d: ", tt);

		for (i = 0;i < n;i++)
		{
			switch (list[i])
			{
			case 0:
				fprintf(out, "R");
				break;
			case 1:
				fprintf(out, "O");
				break;
			case 2:
				fprintf(out, "Y");
				break;
			case 3:
				fprintf(out, "G");
				break;
			case 4:
				fprintf(out, "B");
				break;
			case 5:
				fprintf(out, "V");
				break;
			}
		}
		fprintf(out, "\n");
	}


	fclose(in);
	fclose(out);
	return 0;
}