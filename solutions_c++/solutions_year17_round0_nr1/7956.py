#include <stdio.h>
#include<string.h>

int flipcake(char str[],int a)
{
	int i,j,count=0;
	for (i = 0; i < strlen(str)-a+1; i++)
	{
		if (str[i] == '-')
		{
			for (j = 0; j < a; j++)
			{
				if (str[i + j] == '+')
					str[i + j] = '-';
				else if (str[i + j] == '-')
					str[i + j] = '+';
			}
			count++;
		}
	}
	return count;
}
int main()
{
	int i,j, T, num,result,count;
	char str[1001];
	FILE *in = NULL, *out = NULL;
	in = fopen("A-large.in", "r");
	out = fopen("output.txt", "w");
	fscanf(in, "%d", &T);
	for (i = 0; i < T; i++)
	{
		count = 0;
		fscanf(in, "%s %d", str,&num);
		result = flipcake(str, num);
		for (j = 0; j < strlen(str); j++)
			if (str[j] == '-')
				count++;
		if (count != 0)
			fprintf(out,"Case #%d: IMPOSSIBLE\n", i + 1);
		else
			fprintf(out,"Case #%d: %d\n", i + 1, result);
	}

	fclose(in);
	fclose(out);
	return 0;
}