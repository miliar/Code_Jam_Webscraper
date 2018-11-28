#include <stdio.h>
#include <string.h>
using namespace std;

char a[1005];
int k;

char change(char a)
{
	if (a == '+')
		return '-';
	else
		return '+';
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, mark, ans, kase, m;
	while (~scanf("%d", &m))
	{
		kase = 0;
		for (int i = 0; i < m; i++)
		{
			kase++;
			mark = 0;
			ans = 0;
			scanf("%s %d", &a, &k);
			int n = strlen(a);
			for (int j = 0; j <= n - k; j++)
			{
				if (a[j] != '+')
				{
					for (int l = j; l < j + k; l++)
						a[l] = change(a[l]);
					ans++;
				}
				if (j == n - k)
				{
					for (int l = j; l < j + k; l++)
					{
						if (a[l] != '+')
						{
							mark = 1;
							break;
						}
					}
				}
				
			}
			printf("Case #%d: ", kase);
			if (mark == 1)
				printf("IMPOSSIBLE\n");
			else
			{
				printf("%d\n", ans);
			}
		}
	}
}
