#include <stdio.h>
#include <string.h>

char str[2000];
int len;

void clear ()
{
	for (int i = 0; i < 2000; i++)
		str[i] = 0;
}

bool allc ()
{
	for (int i = 0; i < len; i++)
		if (str[i] == '-')
			return false;

	return true;
}

int main ()
{
	int n, m;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		clear();
		int count = 0;
		bool check = true;
		printf("Case #%d: ", i);
		scanf("%s%d", str, &m);
		len = strlen(str);
		for (int j = 0; j < len; j++)
		{
			if (allc())
				break;
			if (str[j] == '-')
			{
				if (j + m <= len)
				{
					count += 1;
					for (int k = j; k < j + m; k++)
					{
						if (str[k] == '-')
							str[k] = '+';
						else if (str[k] == '+')
							str[k] = '-';
					}
				}
			}
			// printf("%s\n", str);
		}
		for (int j = 0; j < len; j++)
		{
			// printf("%c ", str[j]);
			if (str[j] == '-')
				check = false;
		}
		if (check)
			printf("%d\n", count);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}