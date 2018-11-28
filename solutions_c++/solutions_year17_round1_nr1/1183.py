/*Alphabet Cake*/

#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	char grid[30][30];
	int C, i, j, k, R, t, T;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d %d", &R, &C);
		for (i = 0; i < R; i++)
			scanf("%s", grid[i]);
		for (i = 0; i < R; i++)
		{
			for (j = 0; j < C; j++)
			{
				if (grid[i][j] != '?')
				{
					for (k = i - 1; k >= 0; k--)
					{
						if (grid[k][j] != '?')
							break;
						grid[k][j] = grid[i][j];
					}
					for (k = i + 1; k < R; k++)
					{
						if (grid[k][j] != '?')
							break;
						grid[k][j] = grid[i][j];
					}
				}
			}
		}
		for (i = 0; i < R; i++)
		{
			for (j = 0; j < C; j++)
			{
				if (grid[i][j] != '?')
				{
					for (k = j - 1; k >= 0; k--)
					{
						if (grid[i][k] != '?')
							break;
						grid[i][k] = grid[i][j];
					}
					for (k = j + 1; k < C; k++)
					{
						if (grid[i][k] != '?')
							break;
						grid[i][k] = grid[i][j];
					}
				}
			}
		}
		printf("Case #%d:\n", t);
		for (i = 0; i < R; i++)
			puts(grid[i]);
	}
	return 0;
}