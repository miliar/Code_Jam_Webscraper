#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int T;
char cake[30][30];
bool processed[30][30];
int R, C;

void expand(int x, int y)
{
	if (processed[x][y] == true)
	{
		return;
	}
	processed[x][y] = true;
	char ch = cake[x][y];
	int startindex = -1, endIndex = -1;
	bool started = false;
	for (int i = 0; i < R; i++)
	{
		if (cake[i][y] == ch)
		{
			if (started == false)
			{
				started = true;
				startindex = i;
			}
		}
		else if (started == true)
		{
			endIndex = i - 1;
			break;
		}
	}
	if (endIndex == -1)
	{
		endIndex = R - 1;
	}

	for (int i = y + 1; i < C; i++)
	{
		bool nonJoker = false;
		for (int j = startindex; j <= endIndex; j++)
		{
			if (cake[j][i] != '?')
			{
				nonJoker = true;
				break;
			}
		}
		if (nonJoker)
		{
			break;
		}
		else
		{
			for (int j = startindex; j <= endIndex; j++)
			{
				cake[j][i] = ch;
				processed[j][i] = true;
			}
		}
	}
	for (int i = y - 1; i >= 0; i--)
	{
		bool nonJoker = false;
		for (int j = startindex; j <= endIndex; j++)
		{
			if (cake[j][i] != '?')
			{
				nonJoker = true;
				break;
			}
		}
		if (nonJoker)
		{
			break;
		}
		else
		{
			for (int j = startindex; j <= endIndex; j++)
			{
				cake[j][i] = ch;
				processed[j][i] = true;
			}
		}
	}






	startindex = -1, endIndex = -1;
	started = false;
	for (int i = 0; i < C; i++)
	{
		if (cake[x][i] == ch)
		{
			if (started == false)
			{
				started = true;
				startindex = i;
			}
		}
		else if (started == true)
		{
			endIndex = i - 1;
			break;
		}
	}
	if (endIndex == -1)
	{
		endIndex = C - 1;
	}

	for (int i = x + 1; i < R; i++)
	{
		bool nonJoker = false;
		for (int j = startindex; j <= endIndex; j++)
		{
			if (cake[i][j] != '?')
			{
				nonJoker = true;
				break;
			}
		}
		if (nonJoker)
		{
			break;
		}
		else
		{
			for (int j = startindex; j <= endIndex; j++)
			{
				cake[i][j] = ch;
				processed[i][j] = true;
			}
		}
	}

	for (int i = x - 1; i >= 0; i--)
	{
		bool nonJoker = false;
		for (int j = startindex; j <= endIndex; j++)
		{
			if (cake[i][j] != '?')
			{
				nonJoker = true;
				break;
			}
		}
		if (nonJoker)
		{
			break;
		}
		else
		{
			for (int j = startindex; j <= endIndex; j++)
			{
				cake[i][j] = ch;
				processed[i][j] = true;
			}
		}
	}

}

int main()
{
	FILE* file;
	freopen_s(&file, "input.txt", "r", stdin);
	FILE* file_2;
	freopen_s(&file_2, "output.txt", "w", stdout);
	scanf_s("%d", &T);
	for (int test_i = 0; test_i < T; test_i++)
	{
		for (int i = 0; i < 30; i++)
		{
			for (int j = 0; j < 30; j++)
			{
				processed[i][j] = false;
			}
		}
		scanf_s(" %d %d", &R, &C);
		for (int i = 0; i < R; i++)
		{
			scanf_s(" %s", cake[i], 30);
		}

		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (cake[i][j] != '?')
				{
					expand(i, j);
				}
			}
		}

		printf("Case #%d: \n", test_i + 1);
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				printf("%c", cake[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}