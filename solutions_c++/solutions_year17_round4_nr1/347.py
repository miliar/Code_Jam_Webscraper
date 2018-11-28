#include <cstdio>
#include <algorithm>
using namespace std;
#define N 100 + 5
#define INF 593119681

int Case, n, p, ans, A[N], T[5], Dp[N][N][N][3], _Dp[N][N][N][N][4];

inline void Solve_2()
{
	int cnt = 0;
	for (int i = 1; i <= n; i ++)
	{
		if (A[i] & 1) cnt ++;
		else ans ++;
	}
	ans += cnt + 1 >> 1;
}

inline void Solve_3()
{
	T[0] = T[1] = T[2] = 0;
	for (int i = 1; i <= n; i ++)
		T[A[i] % 3] ++;
	for (int i = 0; i <= T[0]; i ++)
		for (int j = 0; j <= T[1]; j ++)
			for (int k = 0; k <= T[2]; k ++)
				for (int ret = 0; ret < 3; ret ++)
					Dp[i][j][k][ret] = -INF;
	Dp[0][0][0][0] = 0;
	for (int i = 0; i <= T[0]; i ++)
		for (int j = 0; j <= T[1]; j ++)
			for (int k = 0; k <= T[2]; k ++)
				for (int ret = 0; ret < 3; ret ++)
				{
					if (Dp[i][j][k][ret] < 0) continue ;
					if (i < T[0])
						Dp[i + 1][j][k][ret] = max(Dp[i + 1][j][k][ret], Dp[i][j][k][ret] + (ret == 0));
					if (j < T[1])
						Dp[i][j + 1][k][(ret + 1) % 3] = max(Dp[i][j + 1][k][(ret + 1) % 3], Dp[i][j][k][ret] + (ret == 0));
					if (k < T[2])
						Dp[i][j][k + 1][(ret + 2) % 3] = max(Dp[i][j][k + 1][(ret + 2) % 3], Dp[i][j][k][ret] + (ret == 0));
				}
	ans = Dp[T[0]][T[1]][T[2]][(T[1] + 2 * T[2]) % 3];
}

inline void Solve_4()
{
	T[0] = T[1] = T[2] = T[3] = 0;
	for (int i = 1; i <= n; i ++)
		T[A[i] & 3] ++;
	for (int i = 0; i <= T[0]; i ++)
		for (int j = 0; j <= T[1]; j ++)
			for (int k = 0; k <= T[2]; k ++)
				for (int l = 0; l <= T[3]; l ++)
					for (int ret = 0; ret < 4; ret ++)
						_Dp[i][j][k][l][ret] = -INF;
	_Dp[0][0][0][0][0] = 0;
	for (int i = 0; i <= T[0]; i ++)
		for (int j = 0; j <= T[1]; j ++)
			for (int k = 0; k <= T[2]; k ++)
				for (int l = 0; l <= T[3]; l ++)
					for (int ret = 0; ret < 4; ret ++)
					{
						if (_Dp[i][j][k][l][ret] < 0) continue ;
						if (i < T[0])
							_Dp[i + 1][j][k][l][ret] = max(_Dp[i + 1][j][k][l][ret], _Dp[i][j][k][l][ret] + (ret == 0));
						if (j < T[1])
							_Dp[i][j + 1][k][l][(ret + 1) & 3] = max(_Dp[i][j + 1][k][l][(ret + 1) & 3], _Dp[i][j][k][l][ret] + (ret == 0));
						if (k < T[2])
							_Dp[i][j][k + 1][l][(ret + 2) & 3] = max(_Dp[i][j][k + 1][l][(ret + 2) & 3], _Dp[i][j][k][l][ret] + (ret == 0));
						if (l < T[3])
							_Dp[i][j][k][l + 1][(ret + 3) & 3] = max(_Dp[i][j][k][l + 1][(ret + 3) & 3], _Dp[i][j][k][l][ret] + (ret == 0));	
					}
	ans = _Dp[T[0]][T[1]][T[2]][T[3]][(T[1] + 2 * T[2] + 3 * T[3]) & 3];
}

int main()
{
	scanf("%d", &Case);
	for (int Test = 1; Test <= Case; Test ++)
	{
		scanf("%d%d", &n, &p);
		for (int i = 1; i <= n; i ++)
			scanf("%d", A + i);
		ans = 0;
		if (p == 2) Solve_2();
		else if (p == 3) Solve_3();
		else if (p == 4) Solve_4();
		printf("Case #%d: %d\n", Test, ans);
	}
	return 0;
}
