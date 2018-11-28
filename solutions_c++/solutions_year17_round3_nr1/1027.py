#define _USE_MATH_DEFINES
#include <stdio.h>
#include <bits/stdc++.h>
#define ull unsigned long long
#define ld long double
#define ll __int64
using namespace std;
const int N = 1500;
const int seconds = 24 * 60;
int main()
{
	int i, j, t;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		int n, k;
		ld ans = 0, tmpAns=0;
		scanf("%d %d", &n, &k);
		vector<pair<ld, ld>> x; // up, side
		for (auto j = 0; j < n; j++)
		{
			ld r, h;
			scanf("%lf %lf", &r, &h);
			ld up = r*r;
			ld side = 2*r*h;
			x.push_back({ up,side});
		}
		sort(x.begin(), x.end());
		for (auto idx = 0; idx < n; idx++)
		{
			tmpAns = x[idx].first + x[idx].second;
			vector<ld> y;
			for (auto id = 0; id < n; id++)
			{
				if(id!=idx)
					y.push_back(x[id].second);
			}
			sort(y.rbegin(), y.rend());
			for (auto id = 0; id < k - 1; id++)
				tmpAns += y[id];
			if (tmpAns > ans)
				ans = tmpAns;
		}
		ld doubleAns = M_PI*static_cast<ld>(ans);
		printf("Case #%d: %.10lf\n", i + 1,doubleAns);
	}
	return 0;
}