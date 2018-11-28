#include <cstdio>
#include <cstring>
char str[1010];
int main()
{
	freopen("ans", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas ++)
	{
		int n;
		int ans = 0;
		scanf("%s%d", str, &n);
		int len = strlen(str);
		for (int i = 0; i < len; i ++)
		{
			if (str[i] == '-' && i + n <= len)
			{
				for (int j = 0; j < n; j ++)
				{
					str[i + j] = str[i + j] == '-' ? '+' : '-';
				}
				ans ++;
			}
			//puts(str);
		}
		bool flag = true;
		for (int i = 0; i < len; i ++)
		{
			if (str[i] == '-')
			{
				flag = false;
			}
		}
		if (flag == false)
		{
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
		else
		{
			printf("Case #%d: %d\n", cas, ans);
		}
	}
	return 0;
}