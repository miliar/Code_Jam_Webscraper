#include <stdio.h>
#include <math.h>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int map[27][27];

int 
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for (int qq = 1; qq < T + 1; qq++)
	{
		int h, w;
		scanf("%d%d", &h, &w);
		char temp;

		for (int i = 0; i < 26; i++)
			for (int j = 0; j < 26; j++)
				map[i][j] = 0;

		for (int i = 0; i < h; i++)
		{
			scanf("%c", &temp);
			for (int j = 0; j < w; j++)
			{
				char c;
				scanf("%c", &c);
				map[i][j] = c;
			}
		}

		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (map[i][j] != '?')
				{
					int you = map[i][j];
					for (int k = j; k < w; k++)
					{
						if (map[i][k] != '?' && map[i][k] != you)
							break;
						map[i][k] = you;
					}
					for (int k = j; k >= 0; k--)
					{
						if (map[i][k] != '?' && map[i][k] != you)
							break;
						map[i][k] = you;
					}
				}
			}
		}
		int before = -1;
		int start;
		int is_possible = 1;
		int size = 0;
		for (int i = 0; i < h - 1; i++)
		{
			before = -1;
			for (int j = 0; j < w + 1; j++)
			{
				if (map[i][j] != '?')
				{
					int you = map[i][j];
					if (before == -1)
					{
						start = j;
						before = you;
						is_possible = 1;
						size = 0;
					}

					if (before != you)
					{
						if (is_possible)
						{
							for (int k = start; k < start + size; k++)
							{
								map[i + 1][k] = before;
							}
						}
						start = j;
						before = you;
						is_possible = 1;
						size = 0;
					}

					if (map[i + 1][j] != '?')
						is_possible = 0;
					else
						size++;
				}
			}
		}
		before = -1;
		is_possible = 1;
		size = 0;
		for (int i = h - 1; i >= 0; i--)
		{
			before = -1;
			for (int j = w - 1; j >= -1; j--)
			{
				if (j == -1)
				{
					for (int k = start; k > start - size; k--)
					{
						map[i - 1][k] = before;
					}
					break;
				}
				if (map[i][j] != '?')
				{
					int you = map[i][j];
					if (before == -1)
					{
						start = j;
						before = you;
						is_possible = 1;
						size = 0;
					}

					if (before != you)
					{
						if (is_possible)
						{
							for (int k = start; k > start - size; k--)
							{
								map[i - 1][k] = before;
							}
						}
						start = j;
						before = you;
						is_possible = 1;
						size = 0;
					}

					if (map[i - 1][j] != '?')
						is_possible = 0;
					else
						size++;
				}
			}
		}
		printf("Case #%d:\n", qq);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				printf("%c", map[i][j]);
			}
			printf("\n");
		}
	}
	
	return 0;
}
/*
1
4 2
??
?A
??
B?
*/