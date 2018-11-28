#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1000 + 5

int Case, n, c, m, y, z, Pos[N][N], Sum[N][N], Cnt[N];

inline void Solve()
{
	for (int i = 1; i <= c; i ++)
	{
		for (int j = 1; j <= n; j ++)
			Pos[i][j] = 0;
		Cnt[i] = 0;
	}
	for (int i = 1, pos, id; i <= m; i ++)
	{
		scanf("%d%d", &pos, &id);
		Cnt[id] ++;
		Pos[id][pos] ++;
	}
	y = z = 0;
	for (int i = 1; i <= c; i ++)
		y = max(y, Cnt[i]);
	for (int i = 1; i <= n; i ++)
	{
		int sum = 0;
		for (int j = 1; j <= c; j ++)
		{
			Sum[j][i] = Sum[j][i - 1] + Pos[j][i];
			sum += Sum[j][i];
		}
		y = max(y, (sum + i - 1) / i);
	}
	for (int i = 1; i <= n; i ++)
	{
		int sum = 0;
		for (int j = 1; j <= c; j ++)
			sum += Pos[j][i];
		z += max(sum - y, 0);
	}
}

int main()
{
	scanf("%d", &Case);
	for (int Test = 1; Test <= Case; Test ++)
	{
		scanf("%d%d%d", &n, &c, &m);
		Solve();
		printf("Case #%d: %d %d\n", Test, y, z);
	}
	return 0;
}
