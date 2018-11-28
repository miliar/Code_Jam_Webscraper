#include<stdio.h>
#include<string.h>
int t, n, m, cnt, cas;
char s[1010];
int main()
{
	int i, j;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		scanf("%s %d", s, &m);
		n = strlen(s); cnt = 0; cas++;
		for (i = 0; i <= n - m; i++)
		{
			if (s[i] == '-')
			{
				for (j = i; j < i + m; j++)
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				cnt++;
			}
		}
		for (i = 0; i < n; i++)
			if (s[i] == '-')
				break;
		if (i == n)
			printf("Case #%d: %d\n", cas, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", cas);
	}
}