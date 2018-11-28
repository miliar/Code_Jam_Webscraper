#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int daytime = 1440;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int ac, aj;
		scanf("%d %d", &ac, &aj);
		vector<vector<int>> activities;
		for (int i = 0; i < ac; i++)
		{
			int c, d;
			scanf("%d %d", &c, &d);
			activities.push_back(vector<int> { c, d, 0 });
		}
		for (int i = 0; i < aj; i++)
		{
			int c, d;
			scanf("%d %d", &c, &d);
			activities.push_back(vector<int> { c, d, 1 });
		}
		sort(activities.begin(), activities.end());

		vector<int> t(2, 0), ts(2, 0);
		vector<vector<int>> nts(2);
		int ans = 0;
		for (int i = 0; i < ac + aj; i++)
		{
			t[activities[i][2]] += activities[i][1] - activities[i][0];

			int nxt = (i + 1) % (ac + aj);
			if (activities[i][2] != activities[nxt][2])
				ans++;
			else
			{
				int period = activities[nxt][0] - activities[i][1];
				if (period < 0)
					period += daytime;

				ts[activities[i][2]] += period;
				nts[activities[i][2]].push_back(-period);
			}
		}

		if (t[0] + ts[0] > daytime / 2 || t[1] + ts[1] > daytime / 2)
		{
			int id = t[0] + ts[0] > daytime / 2 ? 0 : 1;
			int st = t[id] + ts[id] - daytime / 2;
			
			sort(nts[id].begin(), nts[id].end());
			int i = 0;
			while (st > 0)
			{
				st += nts[id][i];
				i++;
			}

			ans += 2 * i;
		}

		printf("Case #%d: %d\n", _case + 1, ans);
	}

	return 0;
}