#include<cstdio>
#include<cstring>
int n, r;
char a[1024];
int main()
{
	int i, j;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%s%d", &a[1], &r);
		n = strlen(&a[1]);
		int ans = 0;
		for (i = 1; i + r - 1 <= n; i++)
		{
			if (a[i] == '-')
			{
				for (j = 0; j < r; j++) a[i + j] = a[i + j] == '+' ? '-' : '+';
				ans++;
			}
		}
		for (; i <= n; i++)
		{
			if (a[i] == '-') ans = -1;
		}
		printf("Case #%d: ", t);
		if (ans < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
