#include "stdio.h"


int main()
{
	int t = 0;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++)
	{
		char map[26][26] = { 0 };
		int R, C;
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; i++)
		{
			scanf("%s", &map[i][0]);
		}
		for (int i = 0; i < C; i++)
		{
			for (int j = 1; j < R; j++)
			{
				if (map[j][i] == '?')
					map[j][i] = map[j-1][i];
			}
		}
		for (int i = 0; i < C; i++)
		{
			for (int j = R-2; j >= 0; j--)
			{
				if (map[j][i] == '?')
					map[j][i] = map[j+1][i];
			}
		}

		for (int i = 1; i < C; i++)
		{
			if (map[0][i] == '?')
			{
				for (int j = 0; j < R; j++)
				{
					map[j][i] = map[j][i - 1];
				}
			}
		}
		for (int i = C-2; i >=0; i--)
		{
			if (map[0][i] == '?')
			{
				for (int j = 0; j < R; j++)
				{
					map[j][i] = map[j][i+1];
				}
			}
		}

		printf("Case #%d: \n", tc +1);

		for (int i = 0; i < R; i++)
		{
			printf("%s\n", map[i]);
		}
	}
}