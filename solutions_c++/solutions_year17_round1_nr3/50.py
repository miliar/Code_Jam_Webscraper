/*
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▐▐▐▐▐▐░░░░░░░
░░░░░░░░░░▐▐▌▌▌▌▌▌▐▐░░░░░
░░░░░░░░░▐▌▌▌▌▌▌▌▌▌▌▐░░░░
░░░░░░░░▐░░▌◐░▌▌▌◐░░░▐░░░
░░░░░░░░▐░░░░░░░░░░░░▐░░░  
░░░░░░░░▐░░░░░▐░░░░░░▐░░░
░░░░░░░░░▐░░░▐▐▐░░░░░▐░░░
░░░░░░░░░▐░░░░░░░░░░▐░░░░
░░░░░░░░░░▐░░████░░▐░░░░░
запускаем░░▐░░░░░░░▐░░░░░
░░░░Влада░░▐░░░░░░▐░░░░░░
░░░Макеева░░▐░░░░▐░░░░░░░
░░░░░░░░░░░░░▐▐▐▐░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
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
int up(int x, int y)
{
	return (x + y - 1) / y;
}
int notkill(int x, int y)
{
	if (x % y == 0) return (x / y) - 1;
	return x / y;
}
const int INF = (int)1e9 + 7;
int zhfs()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		int hd, ad, hk, ak, b, d;
		scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);
		int killSteps = INF;
		for (int i = 0; i <= 101; i++)
		{
			killSteps = min(killSteps, i + up(hk, ad + i * b));
		}
		int res = INF;
		for (int i = 0; i <= 101; i++)
		{
			int curh = hd, curd = ak;
			bool ok = true;
			int stepsDone = 0;
			int it = 0;
			while (stepsDone < i + killSteps - 1 && it <= 500)
			{
				it++;
				int god = curd;
				if (i == 0)
				{
				//	cerr << stepsDone << " " << curh << " " << curd << endl;
				}
				if (stepsDone < i)
				{
					god = max(0, curd - d);
				}
				if (curh - god <= 0)
				{
					curh = hd - curd;
					if (curh <= 0)
					{
						ok = false;
						break;
					}
					continue;
				}
				curh -= god;
				stepsDone++;
				curd = god;
			}
			if (ok && it < 500)
			{
				res = min(res, it + 1);
			}
		}
		printf("Case #%d: ", tt);
		if (res == INF)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", res);
		}
	}
}

