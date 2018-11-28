#include <cstdio>
#include <algorithm>
using namespace std;
#define N 1440 + 5
#define INF 593119681

int Case, n, m, T = 1440, Min, Flag[N], Dp[N][N][2][2];

int main()
{
	scanf("%d", &Case);
	for (int Test = 1; Test <= Case; Test ++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= T; i ++) Flag[i] = 0;
		for (int i = 1, l, r; i <= n; i ++)
		{
			scanf("%d%d", &l, &r);
			for (l ++; l <= r; l ++) Flag[l] = 1;
		}
		for (int i = 1, l, r; i <= m; i ++)
		{
			scanf("%d%d", &l, &r);
			for (l ++; l <= r; l ++) Flag[l] = 2;
		}
		for (int i = 0; i <= T; i ++)
			for (int j = 0; j <= T; j ++)
				for (int k = 0; k < 2; k ++)
					for (int l = 0; l < 2; l ++)
						Dp[i][j][k][l] = INF;
		if (Flag[1] != 1) Dp[1][0][0][0] = 0;
		if (Flag[1] != 2) Dp[0][1][1][1] = 0;
		for (int t = 2; t <= T; t ++)
			for (int i = max(0, t - 720); i <= t && i <= 720; i ++)
				for (int last = 0; last < 2; last ++)
				{
					if (Flag[t] == last + 1) continue ;
					int _i = i, _j = t - i;
					if (last == 0) _i --; else _j --;
					if (_i < 0 || _j < 0) continue ;
					for (int start = 0; start < 2; start ++)
						for (int _last = 0; _last < 2; _last ++)
							Dp[i][t - i][last][start] = min(Dp[i][t - i][last][start], Dp[_i][_j][_last][start] + (last != _last));
				}
		Min = min(min(Dp[720][720][0][0], Dp[720][720][1][1]), min(Dp[720][720][0][1], Dp[720][720][1][0]) + 1);
		printf("Case #%d: %d\n", Test, Min);
	}
	return 0;
}
