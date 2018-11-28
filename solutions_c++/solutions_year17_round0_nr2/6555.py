#include <stdio.h>
int main()
{
	long long int t, testcase, n, i, size, tidy, j;
	char c[22];
	scanf("%lld", &t);
	for (testcase = 1; testcase <= t; testcase++)
	{
		scanf("%s", c);
		for (i = 0; i < 22; i++)
		{
			if (c[i] == '\n' || c[i] == '\0')
			{
				size = i;
				break;
			}
		}
		if (size != 1)
		{
			tidy = 1;
			for (i = 0; i < size - 1; i++)
			{
				if (c[i] > c[i + 1])
				{
					tidy = 0;
					break;
				}
			}
			if (tidy == 0)
			{
				if (c[i] != '1')
				{
					c[i]--;
					for (j = i - 1; j >= 0; j--)
					{
						if (c[j] == c[j + 1] + 1)
						{
							c[j]--;
							i--;
						}
					}
					for (j = i + 1; j < size; j++) c[j] = '9';
				}
				else
				{
					size--;
					for (i = 0; i < size; i++) c[i] = '9';
				}
			}
		}

		printf("Case #%lld: ", testcase);
		for (i = 0; i < size; i++) printf("%c", c[i]);
		printf("\n");
	}
	return 0;
}