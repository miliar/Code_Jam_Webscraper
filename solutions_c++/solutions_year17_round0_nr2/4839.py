#include <stdio.h>
#include <string.h>

char str[50];
int len;

bool cf ()
{
	for (int i = len - 1; i >= 0; i--)
		if (str[i] - str[i + 1] > 0)
			return false;

	return true;
}

int main ()
{
	int n;
	scanf("%d ", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		scanf("%s", str);
		len = strlen(str);
		if (cf())
		{
			printf("%s\n", str);
		}
		else
		{
			for (int j = 1; j < len; j++)
			{
				if (str[len - j] - str[len - j - 1] < 0)
				{
					str[len - j] = '9';
					str[len - j - 1] -= 1;
				}
			}
			for (int j = 0; j < len; j++)
			{
				if (j == 0 && str[j] == '0')
					continue;
				if (str[j] == '9')
					str[j + 1] = '9';
				printf("%c", str[j]);
			}
			printf("\n");
		}
	}
	return 0;
}