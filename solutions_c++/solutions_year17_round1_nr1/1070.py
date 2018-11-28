#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
int T;
int main()
{
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int R, C;
		char grid[30][30];
		scanf("%d %d", &R, &C);
		for(int r=0; r<R; r++)
		{
			scanf(" %s ", grid[r]);
		}
		for(int r=0; r<R; r++)
		{
			char prev = '?';
			for(int c=0; c<C; c++)
			{
				if(grid[r][c]!='?')
				{
					if(prev == '?')
					{
						for(int i=0; i<c; i++)
						{
							grid[r][i] = grid[r][c];
						}
					}
					prev = grid[r][c];
				}
				else
				{
					grid[r][c] = prev;
				}
			}
		}
		for(int c=0; c<C; c++)
		{
			char prev = '?';
			for(int r=0; r<R; r++)
			{
				if(grid[r][c]!='?')
				{
					if(prev == '?')
					{
						for(int i=0; i<r; i++)
						{
							grid[i][c] = grid[r][c];
						}
					}
					prev = grid[r][c];
				}
				else
				{
					grid[r][c] = prev;
				}
			}
		}
		printf("Case #%d:\n", t);
		for(int r=0; r<R; r++)
		{
			for(int c=0; c<C; c++)
			{
				printf("%c", grid[r][c]);
			}
			printf("\n");
		}
	}
}