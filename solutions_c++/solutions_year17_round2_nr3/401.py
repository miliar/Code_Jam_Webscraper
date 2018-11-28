#include <cstdio>
const double eps = 1e-8;
const int maxn = 105;
int n, q, e[maxn], s[maxn];
double dist[maxn][maxn];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; i++)
			scanf("%d%d", &e[i], &s[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				scanf("%lf", &dist[i][j]);
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
				{
					if (dist[i][k] < -eps || dist[k][j] < -eps)
						continue;
					if (dist[i][j] < -eps || dist[i][j] > dist[i][k] + dist[k][j])
						dist[i][j] = dist[i][k] + dist[k][j];
				}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (dist[i][j] > e[i] + eps)
					dist[i][j] = -1;
				else
					dist[i][j] = dist[i][j] / s[i];
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
				{
					if (dist[i][k] < -eps || dist[k][j] < -eps)
						continue;
					if (dist[i][j] < -eps || dist[i][j] > dist[i][k] + dist[k][j])
						dist[i][j] = dist[i][k] + dist[k][j];
				}
		printf("Case #%d: ", tt);
		while (q--)
		{
			int u, v;
			scanf("%d%d", &u, &v);
			if (dist[u][v] > eps)
				printf("%.8f ", dist[u][v]);
			else
				printf("cnm ");
		}
		printf("\n");
	}
	return 0;
}
