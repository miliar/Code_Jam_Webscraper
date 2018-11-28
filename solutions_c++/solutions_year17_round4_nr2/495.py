#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);

	int n, c, m, p, b, min_rides, cur_sum, promo;
	int position_count[1001];
	int ticket_count[1001];
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d %d", &n, &c, &m);
		for (int i = 0; i <= n; i++)
		{
			position_count[i] = 0;
		}
		for (int i = 0; i <= c; i++)
		{
			ticket_count[i] = 0;
		}
		min_rides = 0;
		cur_sum = 0;
		promo = 0;

		int a11 = 0, a12 = 0, a21 = 0, a22 = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%d %d", &p, &b);
			ticket_count[b]++;
			position_count[p]++;
		}
		for (int i = 1; i <= n; i++)
		{
			cur_sum += position_count[i];
			min_rides = max(min_rides, (cur_sum + i - 1) / i);
		}
		for (int i = 1; i <= c; i++)
		{
			min_rides = max(min_rides, ticket_count[i]);
		}
		for (int i = 1; i <= n; i++)
		{
			if (position_count[i] - min_rides > 0)
				promo += position_count[i] - min_rides;
		}
		printf("Case #%d: %d %d\n", tt, min_rides, promo);
	}
	return 0;
}
