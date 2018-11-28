#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int R, C;
char g[40][40];

void prt()
{
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
			printf("%c", g[i][j]);
		printf("\n");
	}
}
int main()
{
	/*freopen("1a17aL.in", "r", stdin);
	freopen("1a17aL.out", "w", stdout);*/
	int T, i, j;
	cin >> T;
	for (int cs = 1; cs <= T; cs++)
	{
		memset(g, 0, sizeof g);
		cin >> R >> C;
		for (i = 1; i <= R; i++)
			for (j = 1; j <= C; j++)
			{
				scanf(" %c", &g[i][j]);
				if (g[i][j] == '?')
					g[i][j] = 0;
			}
		
		for (i = 1; i <= R; i++)
			for (j = 1; j <= C; j++)
				if (g[i][j] == 0)
					g[i][j] = g[i][j - 1];
		
		for (i = 1; i <= R; i++)
			for (j = C; j >= 1; j--)
				if (g[i][j] == 0)
					g[i][j] = g[i][j + 1];
		
		for (i = 1; i <= R; i++)
			for (j = 1; j <= C; j++)
				if (g[i][j] == 0)
					g[i][j] = g[i - 1][j];
		
		for (i = R; i >= 1; i--)
			for (j = 1; j <= C; j++)
				if (g[i][j] == 0)
					g[i][j] = g[i + 1][j];
		
		
		printf("Case #%d:\n", cs);
		
		prt();
	}
	return 0;
}

