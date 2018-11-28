#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 1500;

int main()
{
	int i, t, k;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		int n, q, e, s;
		int dist[105][105] = { 0 };
		scanf("%d %d", &n, &q);
		vector< pair<int, int>> x; // range, speed
		x.push_back({ -1, -1 }); // dummy
		vector<long double> y(N + 1, LDBL_MAX); // time
		y[1] = 0; // initial position
		for (auto j = 1; j <= n; j++)
		{
			scanf("%d %d", &e, &s);
			x.push_back({ e,s });
		}
		for (auto j = 1; j <= n; j++)
			for (auto m = 1; m <= n; m++)
				scanf("%d", &dist[j][m]);
		for (auto j = 1; j <= n; j++)
		{
			int curIdx = j;
			ull curDist = 0;
			while (1)
			{
				if (curIdx + 1 <= n)
				{
					curDist += dist[curIdx][curIdx + 1];
					if (curDist <= x[j].first)
					{
						if (y[curIdx + 1] > y[j] + (static_cast<long double>(curDist) / x[j].second))
							y[curIdx + 1] = y[j] + (static_cast<long double>(curDist) / x[j].second);
					}
					else
					{
						break;
					}
					curIdx++;
				}
				else
				{
					break;
				}
			}
		}
		for (auto j = 0; j < q; j++)
		{
			int u, v;
			scanf("%d %d", &u, &v);
			//double ans = 0.0;
			//printf(" %lf", ans);
		}
		//printf("\n");
		printf("Case #%d:", i + 1);
		printf(" %.15lf\n", y[n]);
	}
	return 0;
}
// s = v*t;