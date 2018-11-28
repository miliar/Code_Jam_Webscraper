#include<cstdio>
int n, m;
char a[64][64];
int main()
{
	int i, j, k, l;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i++) scanf("%s", &a[i][1]);
		for (j = 1; j <= m; j++)
		{
			for (i = 1; i <= n; i++)
			{
				if (a[i][j] != '?') continue;
				for (k = i + 1; k <= n && a[k][j] == '?'; k++);
				if (k <= n)
				{
					for (l = i; l < k; l++) a[l][j] = a[k][j];
				}
			}
			for (i = n; i >= 1; i--)
			{
				if (a[i][j] != '?') continue;
				for (k = i - 1; k >= 1 && a[k][j] == '?'; k--);
				if (k >= 1)
				{
					for (l = i; l > k; l--) a[l][j] = a[k][j];
				}
			}
		}
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= m; j++)
			{
				if (a[i][j] != '?') continue;
				for (k = j + 1; k <= m && a[i][k] == '?'; k++);
				if (k <= m)
				{
					for (l = j; l < k; l++) a[i][l] = a[i][k];
				}
			}
			for (j = m; j >= 1; j--)
			{
				if (a[i][j] != '?') continue;
				for (k = j - 1; k >= 1 && a[i][k] == '?'; k--);
				if (k >= 1)
				{
					for (l = j; l > k; l--) a[i][l] = a[i][k];
				}
			}
		}
		printf("Case #%d:\n", t);
		for (i = 1; i <= n; i++) printf("%s\n", &a[i][1]);
	}
	return 0;
}
