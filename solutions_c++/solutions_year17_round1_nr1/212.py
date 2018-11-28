#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int R, C;
char G[30][30];

void Solve()
{
	int i, j;
	scanf("%d%d", &R, &C);
	for (i = 0; i < R; ++i)
	{
		scanf("%s", G[i]);
	}

	for (i = 0; i < R; ++i)
	{
		for (j = 1; j < C; ++j)
		{
			if (G[i][j] == '?')
				G[i][j] = G[i][j-1];
		}
		for (j = C - 2; j >= 0; --j)
		{
			if (G[i][j] == '?')
				G[i][j] = G[i][j + 1];
		}
	}

	for (j = 0; j < C; ++j)
	{
		for (i = 1; i < R; ++i)
		{
			if (G[i][j] == '?')
				G[i][j] = G[i - 1][j];
		}
		for (i = R - 2; i >= 0; --i)
		{
			if (G[i][j] == '?')
				G[i][j] = G[i + 1][j];
		}
	}

	for (i = 0; i < R; ++i)
	{
		puts(G[i]);
	}
}

int main()
{
	int i, t;
	scanf("%d", &t);
	for (i = 0; i < t; ++i)
	{
		printf("Case #%d:\n", i + 1);
		Solve();
	}
	return 0;
}
