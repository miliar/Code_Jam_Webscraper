#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		double u;
		scanf("%lf", &u);
		vector<double> p(n);
		for (int i = 0; i < n; i++)
			scanf("%lf", &p[i]);

		sort(p.begin(), p.end());
		p.push_back(1);
		while (u > 0)
		{
			int i;
			for (i = 1; i <= n && p[i] == p[i - 1]; i++);
			if (i > n)
				break;

			double needed = i * (p[i] - p[0]), add;
			if (needed <= u)
				add = p[i] - p[0];
			else
				add = u / i;
			u -= add * i;

			for (int j = 0; j < i; j++)
				p[j] += add;
		}

		double ans = 1;
		for (int i = 0; i < n; i++)
			ans *= p[i];
		printf("Case #%d: %.6lf\n", _case + 1, ans);
	}

	return 0;
}