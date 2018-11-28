#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int n, m;
int cnt[64];
int v[64];
int main()
{
	int i, j;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i++) scanf("%d", &v[i]);
		vector<pair<int, int> > a[64];
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= m; j++)
			{
				int p;
				scanf("%d", &p);
				int ss = (10 * p + 11 * v[i] - 1) / (11 * v[i]);
				int ee = (10 * p) / (9 * v[i]);
				if (ss < 1) ss = 1;
				if (ss <= ee) a[i].push_back(make_pair(ss, ee));
			}
			sort(a[i].begin(), a[i].end());
			reverse(a[i].begin(), a[i].end());
		}
		int ans = 0;
		while (true)
		{
			bool flag = false;
			int maxs = -1, mine = -1;
			for (i = 1; i <= n; i++)
			{
				if (a[i].empty()) { flag = true; break; }
				if (mine < 0 || mine>a[i][a[i].size() - 1].second)
					mine = a[i][a[i].size() - 1].second;
				if (maxs < a[i][a[i].size() - 1].first)
					maxs = a[i][a[i].size() - 1].first;
			}
			if (flag) break;
			if (maxs <= mine)
			{
				ans++;
				for (i = 1; i <= n; i++) a[i].pop_back();
			}
			else
			{
				for (i = 1; i <= n; i++)
				{
					if (mine == a[i][a[i].size() - 1].second)
						a[i].pop_back();
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
