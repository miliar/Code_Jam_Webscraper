#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

set<pair<int, int> > pri[3];
map<int, int> occ[3];
int n, c, m;

void addZ(int who, int pos)
{
	if (occ[who][pos])
		pri[who].erase(make_pair(occ[who][pos], pos));
	occ[who][pos]++;
	pri[who].insert(make_pair(occ[who][pos], pos));
}

void add(int who, int pos)
{
	addZ(who, pos);
	addZ(2, pos);
}

void reset()
{
	occ[0].clear(); occ[1].clear(); occ[2].clear();
	pri[0].clear(); pri[1].clear(); pri[2].clear();
}

void remZ(int who, int pos)
{
	pri[who].erase(make_pair(occ[who][pos], pos));
	occ[who][pos]--;
	if (occ[who][pos] == 0)
		occ[who].erase(pos);
	else
		pri[who].insert(make_pair(occ[who][pos], pos));
}

void rem(int who, int pos)
{
	remZ(who, pos);
	remZ(2, pos);
}

int pop(int who, int no)
{
	auto it = pri[2].rbegin();
	while (occ[who].find(it->second) == occ[who].end()) it++;
	if (it->second != no)
	{
		rem(who, it->second);
		return 0;
	}
	it++;
	while (it != pri[2].rend() && occ[who].find(it->second) == occ[who].end()) it++;
	if (it != pri[2].rend())
	{
		rem(who, it->second);
		return 0;
	}
	rem(who, no);
	return 1;
}

pair<int, int> solve()
{
	scanf("%d%d%d", &n, &c, &m);
	reset();
	for (int i = 0;i < m;i++)
	{
		int pos, who; scanf("%d%d", &pos, &who);
		add(--who, --pos);
	}
	pair<int, int> ans(0, 0);
	while (occ[0].find(0) != occ[0].end() && !pri[1].empty())
	{
		rem(0, 0);
		ans.first += pop(1, 0);
		ans.first++;
	}
	while (occ[1].find(0) != occ[1].end() && !pri[0].empty())
	{
		rem(1, 0);
		ans.first += pop(0, 0);
		ans.first++;
	}
	while (!pri[0].empty() && !pri[1].empty())
	{
		auto o1 = *pri[0].rbegin(), o2 = *pri[1].rbegin();
		if (o1.first >= o2.first)
		{
			ans.first++;
			rem(0, o1.second);
			ans.second += pop(1, o1.second);
		} else
		{
			ans.first++;
			rem(1, o2.second);
			ans.second += pop(0, o2.second);
		}
	}
	for (auto u: pri[0]) ans.first += u.first;
	for (auto u: pri[1]) ans.first += u.first;
	return ans;
}

int main()
{
	int t; scanf("%d", &t);
	for (int _ = 1;_ <= t;_++)
	{
		fprintf(stderr, "\tCase #% 3d...", _); fflush(stdout);
		milliseconds start_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());

		pair<int, int> ans = solve();
		printf("Case #%d: %d %d\n", _, ans.first, ans.second);

		milliseconds end_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
		long long time_used = end_ti.count() - start_ti.count();
		fprintf(stderr, " done\t% 6lldms\n", time_used); fflush(stdout);
	}
	fprintf(stderr, "\n\n\n");
	return 0;
}
