#include<cstdio>
#define N 110

int T, n, q, E[N], S[N], Map[N][N], a, b, Can[N][N];
double ans, f[N][N];

void Doit()
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
		{
			f[i][j] = -1;
			Can[i][j] = 0;
		}
	for (int i = 1; i <= n; i++)
	{
		Can[i][i] = 1;
		int x = E[i];
		for (int j = i + 1; j <= n; j++)
		{
			x -= Map[j - 1][j];
			if (x >= 0) Can[i][j] = 1;
		}
	}
	f[1][1] = 0;
	for (int i = 2; i <= n; i++)
	{
		for (int j = 1; j < i; j++) if (Can[j][i] && f[i - 1][j] != -1 && (f[i][i] == -1 || f[i][i] > f[i - 1][j] + 1.0 * Map[i - 1][i] / S[j])) f[i][i] = f[i - 1][j] + 1.0 * Map[i - 1][i] / S[j];
		for (int j = 1; j < i; j++) if (Can[j][i] && f[i - 1][j] != -1) f[i][j] = f[i - 1][j] + 1.0 * Map[i - 1][i] / S[j];
	}
	ans = -1;
	for (int i = 1; i <= n; i++) if (f[n][i] != -1 && (ans == -1 || ans > f[n][i])) ans = f[n][i];
}

int main()
{
//	freopen("C.in", "r", stdin);
//	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; i++) scanf("%d%d", E + i, S + i);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) scanf("%d", &Map[i][j]);
		for (int i = 1; i <= q; i++)
		{
			scanf("%d%d", &a, &b);
			Doit();
		}
		printf("Case #%d: %lf\n", I, ans);
	}
	return 0;
}
