#include <stdio.h>
#include <string.h>
#define MAX 1001

int main()
{
	int t;
	char dump;
	scanf("%d", &t);
	scanf("%c", &dump);

	for (int case_n = 1; case_n <= t; case_n++)
	{
		char pancakes[MAX];
		int size;

		scanf("%s", pancakes);
		scanf("%d", &size);

		int len = strlen(pancakes);
		int i;
		int cnt = 0;

		for (i = 0; i <= len - size; i++)
		{
			if (pancakes[i] != '+')
			{
				for (int j = 0; j < size; j++)
				{
					if (pancakes[i + j] == '+')
					{
						pancakes[i + j] = '-';
					}
					else
					{
						pancakes[i + j] = '+';
					}
				}
				cnt++;
			}
		}

		int possible = 1;
		for (; i < len; i++)
		{
			if (pancakes[i] != '+')
			{
				possible = 0;
				break;
			}
		}

		if (possible)
		{
			printf("Case #%d: %d\n", case_n, cnt); 
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", case_n);
		}
	}
}