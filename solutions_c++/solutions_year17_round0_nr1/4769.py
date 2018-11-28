#include <bits/stdc++.h>
using namespace std;

char s[1002];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int tc;

	scanf("%d", &tc);

	int N;

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		int k, ans;

		ans = 0;

		scanf("%s %d", s, &k);

		int len = strlen(s);

		for(int i = 0; i + k - 1 < len; i++)
		{
			if(s[i] == '+')
			{
				continue;
			}
			ans++;
			for(int j = 0; j < k; j++)
			{
				if(s[i + j] == '+')
				{
					s[i + j] = '-';
				}
				else
				{
					s[i + j] = '+';
				}
			}
		}
		for(int j = 0; j < len; j++)
		{
			if(s[j] == '-')
			{
				ans = -1;
			}
		}
		if(ans == -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", ans);
		}
	}

	return 0;
}