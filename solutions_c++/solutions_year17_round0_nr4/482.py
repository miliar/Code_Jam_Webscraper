#include <cstdio>
#include <algorithm>
using namespace std;
#define N 100 + 5

int Case, n, m, sum, cnt;
char s[9];
bool Row[N], Col[N], Dia[N << 1], _Dia[N << 1], Flag[2][N][N], _Flag[2][N][N];

int main()
{
	scanf("%d", &Case);
	for (int T = 1; T <= Case; T ++)
	{
		printf("Case #%d: ", T);
		scanf("%d%d", &n, &m);
		sum = cnt = 0;
		for (int i = 1; i <= n; i ++)
			Row[i] = Col[i] = 0;
		for (int i = 1; i <= n * 2; i ++)
			Dia[i] = _Dia[i] = 0;
		for (int i = 1, x, y; i <= m; i ++)
		{
			scanf("%s%d%d", s, &x, &y);
			Flag[0][x][y] |= (s[0] != '+');
			_Flag[0][x][y] = Flag[0][x][y];
			Row[x] |= (s[0] != '+'), Col[y] |= (s[0] != '+');
			Flag[1][x][y] |= (s[0] != 'x');
			_Flag[1][x][y] = Flag[1][x][y];
			Dia[x + y] |= (s[0] != 'x'), _Dia[x + n - y] |= (s[0] != 'x');
			sum += 1 + (s[0] == 'o');
		}
		for (int i = 1, last = 0; i <= n; i ++)
		{
			if (Row[i]) continue ;
			for (last ++; Col[last]; last ++) ;
			Flag[0][i][last] = 1, sum ++;
		}
		for (int i = 1; i <= n; i ++)
		{
			if (!Dia[1 + i] && !_Dia[1 + n - i]) Flag[1][1][i] = 1, sum ++;
			if (i > 1 && i < n && !Dia[n + i] && !_Dia[n + n - i]) Flag[1][n][i] = 1, sum ++;
		}
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= n; j ++)
				if (Flag[0][i][j] != _Flag[0][i][j] || Flag[1][i][j] != _Flag[1][i][j]) cnt ++;
		printf("%d %d\n", sum, cnt);
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= n; j ++)
			{
				if (Flag[0][i][j] == _Flag[0][i][j] && Flag[1][i][j] == _Flag[1][i][j]) goto end;
				if (Flag[0][i][j] && Flag[1][i][j]) printf("o %d %d\n", i, j);
				else if (Flag[0][i][j]) printf("x %d %d\n", i, j);
				else if (Flag[1][i][j]) printf("+ %d %d\n", i, j);
				end :;
				Flag[0][i][j] = Flag[1][i][j] = _Flag[0][i][j] = _Flag[1][i][j] = 0;
			}
	}
	return 0;
}
