/*
   ЗАПУСКАЕМ
   ░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
   ▄███▀░◐░░░▌░░░░░░░
   ░░░░▌░░░░░▐░░░░░░░
   ░░░░▐░░░░░▐░░░░░░░
   ░░░░▌░░░░░▐▄▄░░░░░
   ░░░░▌░░░░▄▀▒▒▀▀▀▀▄
   ░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
   ░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
   ░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
   ░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
   ░░░░░░░░░░░▌▌░▌▌░░░░░
   ░░░░░░░░░░░▌▌░▌▌░░░░░
   ░░░░░░░░░▄▄▌▌▄▌▌░░░░░ 
   */
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
struct Event
{
	int time;
	int type;
	int id;
	Event(int _pos, int _type, int _id)
	{
		time = _pos;
		type = _type;
		id = _id;
	}
	Event(){
		//
	}
};
bool operator<(Event x, Event y)
{
	if (x.time != y.time) return x.time < y.time;
	return x.id > y.id;
}
const int MAXN = 1007;
int rr[MAXN];
set<pair<int, int> > opened[MAXN];
int rb[MAXN][MAXN];
int zhfs()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		int n, p;
		scanf("%d %d", &n, &p);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &rr[i]);
			rr[i] *= 99;
			opened[i].clear();
		}
		vector<Event> ev;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= p; j++)
			{
				int q;
				scanf("%d", &q);
				q *= 99;
				int l = 10 * q / 11, r = 10 * q / 9;
				int mn = l / rr[i];
				if (l % rr[i]) mn++;
				int mx = r / rr[i];
				//cerr << q << " " << l << " " << mn << " " << mx << endl;
				if (mn <= mx)
				{
					rb[i][j] = mx;
					ev.push_back(Event(mn, i, j));
					ev.push_back(Event(mx, i, -j));
				}
			}
		}
		sort(ev.begin(), ev.end());
		int have = 0, res = 0;
		for (int i = 0; i < (int)ev.size(); i++)
		{
			if (ev[i].id > 0)
			{
				if ((int)opened[ev[i].type].size() == 0)
				{
					have++;
				}
				opened[ev[i].type].insert(make_pair(rb[ev[i].type][ev[i].id], ev[i].id));
			}
			else if (opened[ev[i].type].count(make_pair(ev[i].time, -ev[i].id)))
			{
				if (have == n)
				{
					while (have == n)
					{
						res++;
						for (int j = 1; j <= n; j++)
						{
							if ((int)opened[j].size() == 1)
							{
								have--;
							}
							opened[j].erase(opened[j].begin());
						}
//						assert(have != n);
					}
				}
				else
				{
					if ((int)opened[ev[i].type].size() == 1)
					{
						have--;
					}
					opened[ev[i].type].erase(make_pair(ev[i].time, -ev[i].id));
				}
			}
		}

		while (have == n)
		{
			res++;
			for (int j = 1; j <= n; j++)
			{
				if ((int)opened[j].size() == 1)
				{
					have--;
				}
				opened[j].erase(opened[j].begin());
			}
			assert(have != n);
		}

		printf("Case #%d: %d\n", tt, res);
	}
}

