#include <stdio.h>
#include <iostream>
using namespace std;


const int MAX_SIZE = 26;
char ch[MAX_SIZE][MAX_SIZE];
int R, C;
void extend(int ii, int jj)
{
	for (int i = ii - 1; i >= 0; i--)
	{
		if (ch[i][jj] == '?') ch[i][jj] = ch[ii][jj];
		else break;
	}
	for (int i = ii + 1; i < R; i++)
	{
		if (ch[i][jj] == '?') ch[i][jj] = ch[ii][jj];
		else break;
	}
}

void A()
{
	int T;
	scanf("%d", &T);
	for (int cnt = 0; cnt < T; cnt++)
	{
		scanf("%d %d\n", &R, &C);
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
				scanf("%c", &ch[i][j]);
			scanf("\n");
		}
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (ch[i][j] != '?')
				{
					extend(i, j);
				}
			}
		}
		// check left most;
		int l_m = -1;
		for (int j = 0; j < C; j++)
		{
			if (ch[0][j] == '?') continue;
			else
			{
				l_m = j;
				break;
			}
		}
		if (l_m != 0)
		{
			for (int j = 0; j < l_m; j++)
			{
				for (int i = 0; i < R; i++)
				{
					ch[i][j] = ch[i][l_m];
				}
			}
		}
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (ch[i][j] == '?')
				{
					ch[i][j] = ch[i][j - 1];
				}
			}
		}
		printf("Case #%d:\n", cnt + 1);
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				printf("%c", ch[i][j]);
			}
			printf("\n");
		}
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	A();
	return 0;
}