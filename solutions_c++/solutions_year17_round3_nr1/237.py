#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const double pi = 3.141592653589;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		vector<pair<long long, long long>> cakes;
		for (int i = 0; i < n; i++)
		{
			int x, y;
			scanf("%d %d", &x, &y);
			cakes.push_back(make_pair(-x, y));
		}

		sort(cakes.begin(), cakes.end());
		vector<vector<double>> f(k, vector<double>(n));
		for (int i = 0; i < n; i++)
			f[0][i] = pi * cakes[i].first * cakes[i].first - 2 * pi * cakes[i].first * cakes[i].second;

		for (int i = 1; i < k; i++)
		{
			double mx = 0;
			for (int j = 0; j < n; j++)
			{
				f[i][j] = mx - 2 * pi * cakes[j].first * cakes[j].second;
				mx = max(mx, f[i - 1][j]);
			}
		}

		double ans = 0;
		for (int i = 0; i < n; i++)
			ans = max(ans, f[k - 1][i]);
		printf("Case #%d: %.9lf\n", _case + 1, ans);
	}

	return 0;
}