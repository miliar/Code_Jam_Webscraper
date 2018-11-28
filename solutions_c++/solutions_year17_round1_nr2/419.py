#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

#define EPS   (1e-9)

int n, m, need[52], have[52][52], ptr[52];
vector<pair<int, int> > val[52];

int solve()
{
	int ans = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0;i < n;i++) scanf("%d", need+i);
	for (int i = 0;i < n;i++)
	{
		for (int j = 0;j < m;j++) scanf("%d", have[i]+j);
		sort(have[i], have[i]+m);
		val[i].clear();
		ptr[i] = 0;
		for (int j = 0;j < m;j++)
		{
			double loval = have[i][j]/(need[i]*1.1), hival = have[i][j]/(need[i]*0.9);
			pair<int, int> me(ceil(loval-EPS)+EPS, floor(hival+EPS)+EPS);
			if (me.first <= me.second) val[i].push_back(me);
		}
	}
	for (int i = 0;i < n;i++) if (ptr[i] == val[i].size()) return 0;
	while (ptr[0] < val[0].size())
	{
		auto u = val[0][ptr[0]];
		for (int i = 1;i < n;i++)
		{
			u.first = max(u.first, val[i][ptr[i]].first);
			u.second = min(u.second, val[i][ptr[i]].second);
			if (u.first > u.second)
				break;
		}
		if (u.first <= u.second)
		{
			ans++;
			for (int i = 0;i < n;i++) ptr[i]++;
		} else
		{
			int who = 0;
			for (int i = 1;i < n;i++) if (val[i][ptr[i]].second < val[who][ptr[who]].second)
				who = i;
			ptr[who]++;
		}
		bool ok = true;
		for (int i = 0;i < n;i++) if (ptr[i] == val[i].size())
			ok = false;
		if (!ok) break;
	}
	return ans;
}

int main()
{
	int t; scanf("%d", &t);
	for (int _ = 1;_ <= t;_++)
	{
		fprintf(stderr, "\tCase #% 3d...", _); fflush(stdout);
		milliseconds start_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());

		printf("Case #%d: %d\n", _, solve());

		milliseconds end_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
		long long time_used = end_ti.count() - start_ti.count();
		fprintf(stderr, " done\t% 6lldms\n", time_used); fflush(stdout);
	}
	fprintf(stderr, "\n\n\n");
	return 0;
}
