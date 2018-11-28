#include <fstream>
#include <iostream>

using namespace std;

char grid[25][25];

int findKnown(int R, int Cno)
{
	int i;
	for(i = 0; i < R; i++)
	{
		if(grid[i][Cno] != '?')
			return i;
	}
	return -1;
}

void copyPreviousColumn(int R, int Cno)
{
	int i;
	for(i = 0; i < R; i++)
	{
		grid[i][Cno] = grid[i][Cno - 1];
	}
}

void solve(int R, int C)
{
	int firstI, firstJ;
	int i, j;
	for(j = 0; j < C; j++)
	{
		for(i = 0; i < R; i++)
		{
			if(grid[i][j] != '?')
				break;
		}
		if(i != R)
			break;
	}
	firstI = i;
	firstJ = j;
	for(i = 0; i <= firstI; i++)
	{
		for(j = 0; j <= firstJ; j++)
		{
			grid[i][j] = grid[firstI][firstJ];
		}
	}
	for(;i < R; i++)
	{
		if(grid[i][firstJ] != '?')
		{
			firstI = i;
		}
		for(j = 0; j <= firstJ; j++)
		{
			grid[i][j] = grid[firstI][firstJ];
		}
	}
	for(firstJ++; firstJ < C; firstJ++)
	{		
		firstI = findKnown(R, firstJ);
		if(firstI == -1)
		{
			copyPreviousColumn(R, firstJ);
		}
		else
		{
			for(i = 0;i < R; i++)
			{
				if(grid[i][firstJ] != '?')
				{
					firstI = i;
				}
				else
				{
					grid[i][firstJ] = grid[firstI][firstJ];
				}
			}
		}
	}
}

int main()
{
	ofstream cout("A-large.out", ofstream::out);
	ifstream cin("A-large.in", ifstream::in);
	int T, R, C;
	int x, i, j;
	cin >> T;
	for(x = 1; x <= T; x++)
	{
		cin >> R >> C;
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				cin >> grid[i][j];
			}
		}
		solve(R, C);
		cout << "Case #" << x << ":" << endl;
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				cout << grid[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}