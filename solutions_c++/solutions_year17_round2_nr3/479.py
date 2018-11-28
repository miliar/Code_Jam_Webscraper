#include <bits/stdc++.h>
using namespace std;

const int maxn = 105;

long long Dist[maxn][maxn];
double Time[maxn][maxn];
long long inf = 0x3f3f3f3f3f3f3f3f;
long long s[maxn], sp[maxn];

void sol(int cas)
{
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++) cin >> s[i] >> sp[i];
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
		{
			cin >> Dist[i][j];
			if (Dist[i][j] == -1) Dist[i][j] = inf;
		}
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (Dist[i][k] + Dist[k][j] <= Dist[i][j])
					Dist[i][j] = Dist[i][k] + Dist[k][j];
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (Dist[i][j] <= s[i])
				Time[i][j] = Dist[i][j] * 1. / sp[i];
			else
				Time[i][j] = 1e100;
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (Time[i][k] + Time[k][j] <= Time[i][j])
					Time[i][j] = Time[i][k] + Time[k][j];
	printf("Case #%d:", cas);
	for (int i = 1; i <= q; i++)
	{
		int u, v;
		cin >> u >> v;
		printf(" %.10f", Time[u][v]);
	}
	puts("");
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) sol(i);
	return 0;
}
