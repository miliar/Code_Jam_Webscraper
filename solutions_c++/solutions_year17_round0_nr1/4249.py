#include <cstdio>
#include <cstring>
const int maxn = 1005;
char str[maxn];
int n, k, ans;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d\n", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%s%d", str, &k);
		n = strlen(str);
		ans = 0;
		for (int i = 0; i < n - k + 1; i++)
		{
			if (str[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; j++)
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
			}
		}
		for (int i = 0; i < n; i++)
			if (str[i] == '-')
				ans = -1;
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
