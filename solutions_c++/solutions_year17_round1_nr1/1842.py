#include<cstdio>
#include<iostream>
using namespace std;
const int MAX_R = 30;
const int MAX_C = 30;

char a[MAX_R][MAX_C];
char ans[MAX_R][MAX_C];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				cin >> a[i][j];
				ans[i][j] = ' ';
			}

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (a[i][j] != '?' && ans[i][j] == ' ')
				{
					char sim = a[i][j];
					int x = i;
					int y = j;
					int lt_y = y - 1, rt_y = y + 1;
					while (lt_y >= 0)
					{
						if (a[i][lt_y] == '?' && ans[i][lt_y] == ' ')
							lt_y--;
						else
							break;
					}
					lt_y++;
					while (rt_y < c)
					{
						if (a[i][rt_y] == '?' && ans[i][rt_y] == ' ')
							rt_y++;
						else
							break;
					}
					rt_y--;

					int up_x = x - 1, down_x = x + 1;
					while (up_x >= 0)
					{
						int f = 1;
						for (int w = lt_y; w <= rt_y; w++)
							if (!(a[up_x][w] == '?' && ans[up_x][w] == ' '))
							{
								f = 0;
								break;
							}
						if (f)
							up_x--;
						else
							break;
					}
					up_x++;
					while (down_x < r)
					{
						int f = 1;
						for (int w = lt_y; w <= rt_y; w++)
							if (!(a[down_x][w] == '?' && ans[down_x][w] == ' '))
							{
								f = 0;
								break;
							}
						if (f)
							down_x++;
						else
							break;
					}
					down_x--;

					for (int z1 = up_x; z1 <= down_x; z1++)
						for (int z2 = lt_y; z2 <= rt_y; z2++)
							ans[z1][z2] = sim;
				}
		cout << "Case #" << (q + 1) << ":\n";

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (ans[i][j] == ' ')
				{
					int f = 0;
					for (int x = j - 1; x >= 0; x--)
						if (ans[i][x] != ' ')
						{
							ans[i][j] = ans[i][x];
							f = 1;
							break;
						}
					if (f == 0)
					{
						for (int x = j + 1; x < c; x++)
							if (ans[i][x] != ' ')
							{
								ans[i][j] = ans[i][x];
								break;
							}
					}
				}

		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
				cout << ans[i][j];
			cout << "\n";
		}
	}
	return 0;
}