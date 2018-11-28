#include <stdio.h>

char s[30][30];

int main()
{
	int T;
	scanf("%d", &T);
	for (int re = 1; re <= T; re++)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", s[i]);
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				char c = s[i][j];
				if (c != '?')
				{
					for (int k = i-1; k >= 0 && s[k][j] == '?'; k--)
					{
						s[k][j] = c;
					}
					for (int k = i+1; k < n && s[k][j] == '?'; k++)
					{
						s[k][j] = c;
					}
				}
			}
		}
		for (int i = 0; i < m; i++)
		{
			if (s[0][i] != '?')
			{
				for (int k = i - 1; k >= 0 && s[0][k] == '?'; k--)
				{
					for (int j = 0; j < n; j++)
					{
						s[j][k] = s[j][i];
					}
				}

				for (int k = i + 1; k < m && s[0][k] == '?'; k++)
				{
					for (int j = 0; j < n; j++)
					{
						s[j][k] = s[j][i];
					}
				}


			}
		}

		printf("Case #%d:\n", re);
		for (int i = 0; i < n; i++)
		{
			puts(s[i]);
		}
	}
}