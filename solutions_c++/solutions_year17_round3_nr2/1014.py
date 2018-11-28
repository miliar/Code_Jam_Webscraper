#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;
typedef long double ld;
typedef pair<ld, ld> pld;

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))

const int MAXN = 1050;
const ld PI = 3.14159265358979323846;

ll dp[MAXN][MAXN];

bool cmp(const pair<ll, ll>& a, const pair<ll, ll>& b)
{
	if (a.first == b.first)
		return a.second > b.second;
	return a.first > b.first;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n, m;
		cin >> n >> m;
		vector < pair<ii, int> > otr;
		for (int i = 0; i < n; i++)
		{
			int l, r;
			cin >> l >> r;
			otr.push_back(mp(mp(l, r), 1));
		}
		for (int i = 0; i < m; i++)
		{
			int l, r;
			cin >> l >> r;
			otr.push_back(mp(mp(l, r), 2));
		}

		sort(otr.begin(), otr.end());
		vector < ii > g;
		int ost[3] = { 720, 720, 720 };
		int cur_time = 0;
		for (int i = 0; i < n + m; i++)
		{
			ii d = otr[i].first;
			if (d.first > cur_time)
			{
				g.push_back(mp(d.first - cur_time, 0));
			}
			g.push_back(mp(d.second - d.first, otr[i].second));
			ost[otr[i].second] -= (d.second - d.first);
			cur_time = d.second;
		}
		if (cur_time < 1440)
		{
			if (g[0].second == 0)
				g[0].first += (1440 - cur_time);
			else
				g.push_back(mp(1440 - cur_time, 0));
		}
		
		for (int i = 0; i < g.size(); i++)
		{
			int tp = g[i].second;
			if (tp > 0)
			{
				if (g[i].second == g[(i + 2) % g.size()].second && g[(i + 1) % g.size()].second == 0)
				{
					int tm = g[(i + 1) % g.size()].first;
					if (ost[tp] >= tm)
					{
						g[(i + 1) % g.size()].second = tp;
						ost[tp] -= tm;
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < g.size(); i++)
		{
			int cur = g[i].second;
			if (cur == 0)
				continue;
			int ne = g[(i + 1) % g.size()].second;
			if (cur > 0 && ne > 0 && cur != ne)
				ans++;
			else
			{
				if (cur > 0 && cur == ne)
					continue;
				int nene = g[(i + 2) % g.size()].second;
				if (nene == 0)
					continue;
				if (cur != nene)
				{
					ans++;
				}
				else
					ans += 2;
			}
		}
		cout << "Case #" << t + 1 << ": " << ans << "\n";
	}

	return 0;
}