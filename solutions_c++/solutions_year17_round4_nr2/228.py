#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
int n, c, m;
int customer_cnt[1024];
int seat_cnt[1024];
pair<int, int> tickets[1024];
bool taken[1024][1024];
int ticket_cnt[1024][1024];
int leftmost[1024];
int main()
{
	int i, j;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%d%d%d", &n, &c, &m);
		memset(customer_cnt, 0, sizeof(customer_cnt));
		memset(seat_cnt, 0, sizeof(seat_cnt));
		memset(ticket_cnt, 0, sizeof(ticket_cnt));
		for (i = 1; i <= m; i++)
		{
			scanf("%d%d", &tickets[i].first, &tickets[i].second);
			customer_cnt[tickets[i].second]++;
			seat_cnt[tickets[i].first]++;
			ticket_cnt[tickets[i].second][tickets[i].first]++;
		}
		int y = 0;
		for (i = 1; i <= c; i++) y = max(y, customer_cnt[i]);
		int tot = 0;
		for (i = 1; i <= n; i++)
		{
			tot += seat_cnt[i];
			while (y*i < tot) y++;
		}
		memset(taken, false, sizeof(taken));
		int z = 0;
		for (i = 1; i <= y; i++) leftmost[i] = 1;
		for (i = 1; i <= n; i++)
		{
			vector<int> v;
			for (j = 1; j <= c; j++)
			{
				if (ticket_cnt[j][i]) v.push_back(ticket_cnt[j][i]);
			}
			sort(v.begin(), v.end());
			int topmost = 1;
			while (v.size())
			{
				int x = v[v.size() - 1]; v.pop_back();
				while (topmost <= y && x >= 1)
				{
					taken[topmost][i] = true;
					x--; topmost++;
				}
				if (x >= 1) { v.push_back(x); break; }
			}
			if (v.size())
			{
				sort(v.begin(), v.end());
				while(v.size())
				{
					int x = v[v.size() - 1]; v.pop_back();
					vector<pair<int, int>> w;
					for (j = 1; j <= y; j++)
						w.push_back(make_pair(leftmost[j], j));
					sort(w.begin(), w.end());
					for (j = 0; j < x; j++)
					{
						taken[w[j].second][w[j].first] = true;
						int k = w[j].second;
						while (leftmost[k] <= n && taken[k][leftmost[k]])
							leftmost[k]++;
					}
					z += x;
				}
			}
		}
		printf("Case #%d: %d %d\n", t, y, z);
	}
	return 0;
}
