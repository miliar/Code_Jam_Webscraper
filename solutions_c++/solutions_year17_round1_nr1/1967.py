#include <iostream>
#include <vector>
using namespace std;

int R, C;
char ary[30][30];

void fill_Down(int y, int x, char c)
{
	if (ary[y][x] == '?')
	{
		ary[y][x] = c;
		fill_Down(y + 1, x, c);
	}
	else return;
}
void fill_Up(int y, int x, char c)
{
	if (ary[y][x] == '?')
	{
		ary[y][x] = c;
		fill_Up(y - 1, x, c);
	}
	else return;
}
void process(int tc)
{
	cin >> R >> C;
	
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cin >> ary[i][j];
		}
	}
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			if (ary[i][j] != '?')
			{
				fill_Down(i + 1, j, ary[i][j]);
				fill_Up(i - 1, j, ary[i][j]);
			}
		}
	}

	for (int j = 1; j <= C; j++)
	{
		bool no_one = true;
		for (int i = 1; i <= R; i++)
		{
			if (ary[i][j] != '?') no_one = false;
		}

		if (no_one)
		{
			int cloneCol = j - 1;
			if (j == 1) cloneCol = j + 1;

			for (int i = 1; i <= R; i++) ary[i][j] = ary[i][cloneCol];
		}
	}

	for (int j = C; j >= 1; j--)
	{
		bool no_one = true;
		for (int i = 1; i <= R; i++)
		{
			if (ary[i][j] != '?') no_one = false;
		}

		if (no_one)
		{
			int cloneCol = j + 1;
			if (j == C) cloneCol = j - 1;

			for (int i = 1; i <= R; i++) ary[i][j] = ary[i][cloneCol];
		}
	}


	cout << "Case #" << tc << ":" << endl;
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cout << ary[i][j];
		}
		cout << endl;
	}
}

int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) process(i+1);
	return 0;
}

