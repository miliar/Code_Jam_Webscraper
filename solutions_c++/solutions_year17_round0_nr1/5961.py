#include <stdio.h>
#include <string.h>
int main()
{
	int t, k, i, j, f, ans, len;
	char str[1010];
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.txt", "w", stdout);
	scanf("%d", &t);
	
	for (i = 1; i <= t; i++)
	{
		ans = 0;
		scanf("%s %d", &str, &k);
		len = strlen(str);
		for (j = 0; j<len; j++)
		{
			if (str[j] == '-' && j+k<=len)
			{
				ans++;

				for (f = 0; f < k; f++)
				{
					if (str[j+f] == '-')
						str[j+f] = '+';
					else if (str[j+f] == '+')
						str[j+f] = '-';
				}
			}
		}

		for (j = 0; j<len; j++)
		{
			if (str[j] == '-')
			{
				ans = -1;
				break;
			}
		}

		printf("Case #%d: ", i);
		if (ans != -1)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
}