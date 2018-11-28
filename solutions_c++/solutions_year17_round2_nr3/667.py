#include <bits/stdc++.h>
using namespace std;

int e[105];
int s[105];
long long d[105][105];
double g[105][105];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		int n, q;
		scanf("%d %d", &n, &q);
		for (int i = 0; i < n; i++)
			scanf("%d %d", e + i, s + i);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &d[i][j]);
		for (int k = 0; k < n; k++)
		{
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
				{
					long long nd = -1;
					if (d[i][k] != -1 && d[k][j] != -1)
						nd = d[i][k] + d[k][j];
					if (d[i][j] == -1)
						d[i][j] = nd;
					else if (nd != -1)
						d[i][j] = min(d[i][j], nd);
				}
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				if (d[i][j] == -1)
					continue;
				g[i][j] = 1e15;
				if (d[i][j] <= e[i])
					g[i][j] = 1.0 * d[i][j] / s[i];
			}

		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
		
		printf("Case #%d:", z);
		for (int i = 0; i < q; i++)
		{
			int u, v;
			scanf("%d %d", &u, &v);
			u--;
			v--;
			printf(" %.9lf", g[u][v]);	
		}
		printf("\n");
		
	}
}