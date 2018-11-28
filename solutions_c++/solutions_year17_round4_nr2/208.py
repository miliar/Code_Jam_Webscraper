#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;

struct ti
{
	int p, b;
} ts[1007];
bool operator <(ti a, ti b)
{
	return a.p < b.p;
}
vector<int> mx, sm;
int buy[1007][1007];
// ride, buyer

int check(int ans, int t)
{
	mx.resize(ans); sm.resize(ans);
	memset(buy, 0, sizeof(buy));
	fill(mx.begin(), mx.end(), 0);
	fill(sm.begin(), sm.end(), 0);
	int a2 = t;
	g(i, 0, t)
	{
		g(j, 0, ans) if(mx[j] != ts[i].p)
		{
			buy[j][ts[i].b] = 1;
			// printf("buy1 %d %d\n", j, ts[i].b);
			mx[j] = ts[i].p; ++sm[j]; --a2; goto okk;
		}
		g(j, 0, ans) if(sm[j] != ts[i].p)
		{
			buy[j][ts[i].b] = 1;
			// printf("buy1 %d %d\n", j, ts[i].b);
			mx[j] = ts[i].p; ++sm[j]; goto okk;
		}
		return -1;
		okk:;
	}
	return a2;
}

int cnt[1007];

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		memset(buy, 0, sizeof(buy));
		int n, m, t; cin >> n >> m >> t;
		g(i, 0, t) cin >> ts[i].p >> ts[i].b;
		sort(ts, ts + t);
		memset(cnt, 0, sizeof(cnt));
		int hh = 0;
		g(i, 0, t) hh = max(hh, ++cnt[ts[i].b]);
		// mx.clear(); sm.clear();
		// int ans = 0, a2 = 0;
		// g(i, 0, t)
		// {
			// g(j, 0, ans) if(sm[j] != ts[i].p && !buy[j][ts[i].b])
			// {
				// buy[j][ts[i].b] = 1;
				// printf("buy1 %d %d\n", j, ts[i].b);
				// mx[j] = ts[i].p; ++sm[j]; goto ok;
			// }
			// mx.push_back(ts[i].p); sm.push_back(1); buy[ans++][ts[i].b] = 1;
			// ok:;
		// }
		// a2 = t;
		// fail;
		int l = 0, r = t;
		while(l < r)
		{
			int m = (l + r) >> 1;
			if(check(m, t) != -1) r = m; else l = m + 1;
		}
		l = max(l, hh);
		printf("Case #%d: %d %d\n", _, l, check(l, t));
	}
	return 0;
}
