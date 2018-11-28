#include <stdio.h>
#include <string.h>
int main()
{
	int test_case, i, len, modified, j, p;
	char str[20];
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large-output.txt", "w", stdout);
	scanf("%d", &test_case);
	for (i = 1; i <= test_case; i++)
	{
		scanf("%s", &str);
		len = strlen(str);

		for (p = 0; p < len; p++)
		{
			modified = -1;
			for (j = 0; j < len; j++)
			{
				if (modified == -1 && j != len - 1 && str[j] > str[j + 1])
				{
					str[j]--;
					modified = 1;
				}
				else if (modified == 1)
					str[j] = '9';
			}
		}

		printf("Case #%d: ", i);
		modified = 0;
		for (j = 0; j < len; j++)
		{
			if (modified == 0 && str[j] != '0')
				modified = 1;

			if (modified == 1)
				printf("%c", str[j]);
		}
		printf("\n");
	}
}