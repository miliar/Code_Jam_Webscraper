#include <bits/stdc++.h>

using namespace std;

int		main()
{
	int		t; // number of test cases
	char	s[9001]; // string S
	int		k;
	int		slen;
	int		flips;
	bool	possible;

	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf(" %s", s);
		slen = strlen(s);
		scanf("%d", &k);
		flips = 0;
		for (int i = 0; i < slen - k + 1; i++)
		{
			if (s[i] == '+')
				continue;
			for (int j = 0; j < k; j++)
			{
				if (s[i + j] == '+')
					s[i + j] = '-';
				else
					s[i + j] = '+';
			}
			flips++;
		}
		possible = true;
		for (int i = slen - k + 1; i < slen; i++)
		{
			if (s[i] == '-')
			{
				possible = false;
				break;
			}
		}
		if (possible)
		{
			printf("Case #%d: %d\n", tt, flips);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
	return 0;
}
