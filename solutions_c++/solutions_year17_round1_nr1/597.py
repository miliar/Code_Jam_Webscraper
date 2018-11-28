#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

const LL MOD = 1000000007LL;

char grid[33][33];

int main()
{
	int T, R, C;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++)
			scanf("%s", grid[i]);

		for (int c = 0; c < C; c++)
		{
			char pc = '?';
			for (int r = 0; r < R; r++)
			{
				if (grid[r][c] == '?')
					grid[r][c] = pc;
				pc = grid[r][c];
			}
			pc = '?';
			for (int r = R - 1; r >= 0; r--)
			{
				if (grid[r][c] == '?')
					grid[r][c] = pc;
				pc = grid[r][c];
			}
		}

		for (int r = 0; r < R; r++)
		{
			char pc = '?';
			for (int c = 0; c < C; c++)
			{
				if (grid[r][c] == '?')
					grid[r][c] = pc;
				pc = grid[r][c];
			}
			pc = '?';
			for (int c = C - 1; c >= 0; c--)
			{
				if (grid[r][c] == '?')
					grid[r][c] = pc;
				pc = grid[r][c];
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < R; i++)
			printf("%s\n", grid[i]);
	}

	return 0;
}