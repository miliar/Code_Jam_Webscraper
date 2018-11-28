#include <bits/stdc++.h>

using namespace std;

char str[1010];

int main()
{

	int T, k;
	scanf("%d", &T);
	for(int icase = 1; icase <= T; ++icase)
	{
		scanf("%s %d", str, &k);
		int n = strlen(str);

		int i = 0, j = 0, ans = 0;

		for(i = 0; i+k <= n; ++i)
		{
			if(str[i] == '+')
			{
				continue;
			}

			for(j = 0; j < k; ++j)
			{
				if(str[i+j] == '-')
				{
					str[i+j] = '+';
				}
				else
				{
					str[i+j] = '-';
				}
			}

			ans++;
		}
		
		bool flag = true;

		for(int i = 0; i < n; ++i)
		{
			if(str[i] == '-')
			{
				flag = false;
				break;
			}
		}
		if(flag)
		{
			printf("Case #%d: %d\n", icase, ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", icase);
		}
	}

	return 0;
}
