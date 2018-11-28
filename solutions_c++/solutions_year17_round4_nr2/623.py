#include <bits/stdc++.h>
using namespace std;
int am[1010], bought[1010], t;
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fill_n(am, 1010, 0);
		fill_n(bought, 1010, 0);
		int n, m, c, mx, ans, ans2;
		mx = 0;
		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; i++)
		{
			int p, b;
			scanf("%d%d", &p, &b);
			bought[b]++;
			am[p]++;
			mx = max(mx, bought[b]);
		}
		for (int j = mx; true; j++)
		{
			int pre = 0;
			int moves = 0;
			bool possible = true;
			for (int k = 1; k <= n; k++)
			{
				if (am[k] <= j)
				{
					pre+=j - am[k];
				} 
				else if (am[k]-j <= pre)
				{
					///printf("hi\n");
					moves+=am[k]-j;
					pre-=am[k]-j;
				}
				else { possible = false; break; }
			}
			if (possible) 
			{
				ans = j;
				ans2 = moves;
				break;
			}
		}
		printf("Case #%d: %d %d\n", i, ans, ans2);

	}
}