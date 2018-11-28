#include <bits/stdc++.h>

using namespace std;

int		main()
{
	int			t;
	long long	n;
	long long	k;
	scanf("%d", &t);
	map<long long, long long> adj_stalls;
	map<long long, long long>::reverse_iterator last;
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%lld %lld", &n, &k);
		adj_stalls.clear();
		adj_stalls[n] = 1;
		while (k > 0)
		{
			last = adj_stalls.rbegin();
			if (last->first > 1)
				adj_stalls[last->first / 2] += last->second;
			if (last->first > 2)
				adj_stalls[(last->first - 1) / 2] += last->second;
			if (last->second >= k)
			{
				printf("Case #%d: %lld %lld\n", tt, last->first / 2, (last->first - 1) / 2);
				break;
			}
			k -= last->second;
			adj_stalls.erase(--(last.base()));
		}
	}
	return 0;
}
