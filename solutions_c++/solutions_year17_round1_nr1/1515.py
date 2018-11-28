#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>

using namespace std;
#define ll long long

bool isemptycol(int i, vector<string>& grid)
{
	for (int j = 0; j < grid.size(); j++)
	{
		if (grid[j][i] != '?')
			return false;
	}
	return true;
}

void copycol(int i, int j, vector<string>& grid)
{
	for (int k = 0; k < grid.size(); k++)
	{
		grid[k][j] = grid[k][i];
	}

}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		int r, c;
		cin >> r >> c;
		vector<string> grid(r);
		for (int i = 0; i < r; i++)
			cin >> grid[i];
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (grid[i][j] != '?')
				{
					int k = i - 1;
					char temp = grid[i][j];
					while (k >= 0)
					{
						if (grid[k][j] != '?')
							temp = grid[k][j];
						else
							grid[k][j] = temp;
						k--;
					}

					k = i + 1;
					temp = grid[i][j];
					while (k < r)
					{
						if (grid[k][j] != '?')
							temp = grid[k][j];
						else
							grid[k][j] = temp;
						k++;
					}

				}
			}
		}

		for (int j = 0; j < c; j++)
		{
			if (!isemptycol(j, grid))
			{
				int k = j - 1;
				int temp = j;

				while (k >= 0)
				{
					if (isemptycol(k, grid))
						copycol(j, k, grid);
					k--;
				}

				k = j + 1;

				while (k < c)
				{
					if (isemptycol(k, grid))
						copycol(temp, k, grid);
					else
						temp = k;
					k++;
				}
			}

		}
		cout << "Case #" << cases << ":\n";

		for (int i = 0; i < r; i++)
			cout << grid[i] << "\n";
	}
	return 0;
}