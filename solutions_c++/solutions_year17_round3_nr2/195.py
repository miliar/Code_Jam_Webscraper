#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MaxN = 1450;
const int MaxM = 730;

int T, N, M, AC, AJ, tim[MaxN];
int f[MaxN][MaxM][2];

void DP1()
{
	int i, j;
	for (i=0; i<=N; i++)
		for (j=0; j<=M; j++) f[i][j][0] = f[i][j][1] = 1<<30;
	f[0][0][0] = 0;
	for (i=1; i<=N; i++)
		for (j=0; j<=i; j++)
		{
			if (tim[i] != 2)
			{
				if (j > 0 && i != j) f[i][j][0] = min(f[i-1][j-1][0], f[i-1][j][1] + 1);
				else if (i == j) f[i][j][0] = f[i-1][j-1][0];
				else f[i][j][0] = f[i-1][j][1] + 1;
			}
			if (tim[i] != 1)
			{
				if (j > 0 && i != j) f[i][j][1] = min(f[i-1][j-1][0] + 1, f[i-1][j][1]);
				else if (i == j) f[i][j][1] = f[i-1][j-1][0] + 1;
				else f[i][j][1] = f[i-1][j][1];
			}
			//cout << i << ' ' << j << ' ' << f[i][j][0] << ' ' << f[i][j][1] << endl;
		}
}

void DP2()
{
	int i, j;
	for (i=0; i<=N; i++)
		for (j=0; j<=M; j++) f[i][j][0] = f[i][j][1] = 1<<30;
	f[0][0][1] = 0;
	for (i=1; i<=N; i++)
		for (j=0; j<=i; j++)
		{
			if (tim[i] != 2)
			{
				if (j > 0 && i != j) f[i][j][0] = min(f[i-1][j-1][0], f[i-1][j][1] + 1);
				else if (i == j) f[i][j][0] = f[i-1][j-1][0];
				else f[i][j][0] = f[i-1][j][1] + 1;
			}
			if (tim[i] != 1)
			{
				if (j > 0 && i != j) f[i][j][1] = min(f[i-1][j-1][0] + 1, f[i-1][j][1]);
				else if (i == j) f[i][j][1] = f[i-1][j-1][0] + 1;
				else f[i][j][1] = f[i-1][j][1];
			}
			//cout << i << ' ' << j << ' ' << f[i][j][0] << ' ' << f[i][j][1] << endl;
		}
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &T); N = 1440; M = 720;
	for (int id = 1; id <= T; id++)
	{
		scanf("%d%d", &AC, &AJ);
		for (int i=1; i<=N; i++)
			tim[i] = 0;
		for (int i=1; i<=AC; i++)
		{
			int l, r;
			scanf("%d%d", &l, &r);
			while (l < r) tim[l++] = 2;
		}
		for (int i=1; i<=AJ; i++)
		{
			int l, r;
			scanf("%d%d", &l, &r);
			while (l < r) tim[l++] = 1;
		}
		int ans;
		DP1();
		ans = min(f[N][M][0], f[N][M][1] + 1);
		DP2();
		ans = min(ans, min(f[N][M][1], f[N][M][0] + 1));
		printf("Case #%d: %d\n", id, ans);
	}
	return 0;
}
