#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int n, q;
		scanf("%d %d", &n, &q);
		vector<int> e(n);
		vector<double> s(n);
		for (int i = 0; i < n; i++)
			scanf("%d %lf", &e[i], &s[i]);
		vector<vector<int>> d(n, vector<int>(n));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &d[i][j]);

		printf("Case #%d: ", _case + 1);
		for (int i = 0; i < q; i++)
		{
			int u, v;
			scanf("%d %d", &u, &v);
			u--; v--;

			vector<double> f(n, 1e12);
			f[u] = 0;
			for (int i = 0; i < n; i++)
			{
				long long sum = 0;
				for (int j = i + 1; j < n; j++)
				{
					sum += d[j - 1][j];
					if (sum > e[i])
						break;

					f[j] = min(f[j], f[i] + sum / s[i]);
				}
			}

			if (i)
				printf(" ");
			printf("%lf\n", f[v]);
		}
	}

	return 0;
}