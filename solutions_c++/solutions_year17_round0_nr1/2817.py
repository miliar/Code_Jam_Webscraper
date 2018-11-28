#include <bits/stdc++.h>
using namespace std;

char s[1005];
int k;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		scanf("%s %d", s, &k);
		int res = 0;
		int n = strlen(s);
		for (int i = 0; i < n; i++)
		{
			if (s[i] == '-')
			{
				res++;
				if (n - i < k)
				{
					res = n + 5;
					break;
				}
				for (int j = 0; j < k; j++)
				{
					if (s[i+j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
			}
		}
		if (res > n)
			printf("Case #%d: IMPOSSIBLE\n", z);
		else
			printf("Case #%d: %d\n", z, res);
	}
}