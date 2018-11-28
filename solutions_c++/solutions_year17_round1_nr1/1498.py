#include <bits/stdc++.h>
using namespace std;

int t, cake[25][25], r, c, current;
char cha;

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 25; j++)
		{
			for (int h = 0; h < 25; h++)
			{
				cake[j][h] = 0;
			}
		}
		cin >> r >> c;
		for (int j = 0; j < r; j++)
		{
			for (int h = 0; h < c; h++)
			{
				cin >> cha;
				if (cha == '?')
				{
					cake[j][h] = 0;
				}
				else
				{
					cake[j][h] = int(cha);
				}
			}
		}
		for (int j = 0; j < r; j++)
		{
			current = 0;
			for (int h = 0; h < c; h++)
			{
				if (cake[j][h] == 0)
				{
					if (current != 0)
					{
						cake[j][h] = current;
					}
				}
				else current = cake[j][h];
			}
		}
		for (int j = 0; j < r; j++)
		{
			current = 0;
			for (int h = c-1; h >= 0; h--)
			{
				if (cake[j][h] == 0)
				{
					if (current != 0)
					{
						cake[j][h] = current;
					}
				}
				else current = cake[j][h];
			}
		}
		for (int j = 0; j < c; j++)
		{
			current = 0;
			for (int h = 0; h < r; h++)
			{
				if (cake[h][j] == 0)
				{
					if (current != 0)
					{
						cake[h][j] = current;
					}
				}
				else current = cake[h][j];
			}
		}
		for (int j = 0; j < c; j++)
		{
			current = 0;
			for (int h = r-1; h >= 0; h--)
			{
				if (cake[h][j] == 0)
				{
					if (current != 0)
					{
						cake[h][j] = current;
					}
				}
				else current = cake[h][j];
			}
		}
		cout << "Case #" << i+1 << ": " << endl;
		for (int j = 0; j < r; j++)
		{
			for (int h = 0; h < c; h++)
			{
				cout << char(cake[j][h]);
			}
			cout << endl;
		}
	}
}


























