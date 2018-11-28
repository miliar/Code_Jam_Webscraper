#include <cstdio>
#include <cstring>
int n;
char str[20];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d\n", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		gets(str);
		n = strlen(str);
		printf("Case #%d: ", tt);
		if (n == 1)
		{
			puts(str);
			continue;
		}
		for (int i = 1; i < n; i++)
		{
			if (str[i] < str[i - 1])
			{
				for (int j = i; j < n; j++)
					str[j] = '9';
				i--;
				str[i]--;
				for ( ; i > 0; i--)
				{
					if (str[i] < str[i - 1])
					{
						str[i] = '9';
						str[i - 1]--;
					}
					else break;
				}
				break;
			}
		}
		for (int i = 0; i < n; i++)
		{
			if (str[i] == '0')
				continue;
			puts(str + i);
			break;
		}
	}
	return 0;
}
