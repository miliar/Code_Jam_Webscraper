#include <stdio.h>
int main()
{
	int t, testcase, i, k, size, a, cnt, j;
	char c[1010];
	scanf("%d", &t);
	for (testcase = 1; testcase <= t; testcase++)
	{
		cnt = 0;
		scanf("%s %d", &c, &k);
		for (i = 1; i <= 1009; i++)
		{
			if (c[i] == '\n' || c[i] == '\0') break;
		}
		size = i;
		for (i = 0; i <= size - k; i++)
		{
			if (c[i] == '-')
			{
				cnt++;
				c[i] = '+';
				for (j = 1; j < k; j++)
				{
					if (c[i + j] == '-') c[i + j] = '+';
					else c[i + j] = '-';
				}
			}
		}
		a = 0;
		for (i = size - k + 1; i < size; i++)
		{
			if (c[i] == '-')
			{
				a = 1;
				break;
			}
		}



		printf("Case #%d: ", testcase);
		if (a == 1) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}