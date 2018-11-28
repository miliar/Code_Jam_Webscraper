#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int d, n;
		scanf("%d %d", &d, &n);
		vector<pair<int, double>> horses;
		for (int i = 0; i < n; i++)
		{
			int k, s;
			scanf("%d %d", &k, &s);
			horses.push_back(make_pair(k, s));
		}

		sort(horses.begin(), horses.end());

		int now = 0;
		for (int i = now + 1; i < n; i++)
			if (horses[i].second < horses[now].second)
			{
				double t = (horses[i].first - horses[now].first) / (horses[now].second - horses[1].second);
				double k = horses[now].first + horses[now].second * t;
				if (k <= d)
					now = i;
			}

		double ans = d * horses[now].second / (d - horses[now].first);
		printf("Case #%d: %.6lf\n", _case + 1, ans);
	}

	return 0;
}