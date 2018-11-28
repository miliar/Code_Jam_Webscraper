#include <bits/stdc++.h>
using namespace std;

void sol(int c)
{
	char s[1050];
	int k, ls, ans = 0;
	cin >> s >> k;
	ls = strlen(s);
	for (int i = 0; i <= ls - k; i++)
	{
		if (s[i] == '-')
		{
			for (int j = 0; j < k; j++)
			{
				if (s[i + j] == '-') s[i + j] = '+';
				else s[i + j] = '-';
			}
			ans++;
		}
	}
	for (int i = 0; i < ls; i++)
		if (s[i] == '-')
		{
			printf("Case #%d: IMPOSSIBLE\n", c);
			return;
		}
	printf("Case #%d: %d\n", c, ans);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) sol(i);
	return 0;
}
