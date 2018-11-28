#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isAlpha(char c){
	return ('A' <= c && c <= 'Z');
}


int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		int r, c;
		cin >> r >> c;
		vector<string> grid;
		for (int i = 0; i < r; ++i)
		{
			string row;
			cin >> row;
			grid.push_back(row);
		}

		// one
		for (int i = 0; i < r; ++i)
		{
			char init = '!';
			for (int j = 0; j < c; ++j)
			{
				if(isAlpha(grid[i][j]))
					init = grid[i][j];
				if(isAlpha(init) && grid[i][j] == '?')
					grid[i][j] = init;
			}
		}


		// two
		for (int i = 0; i < r; ++i)
		{
			char init = '!';
			for (int j = c-1; j >= 0; --j)
			{
				if(isAlpha(grid[i][j]))
					init = grid[i][j];
				if(isAlpha(init) && grid[i][j] == '?')
					grid[i][j] = init;
			}
		}

		// three
		for (int j = 0; j < c; ++j)
		{
			for (int i = 1; i < r; ++i)
			{
				if(grid[i][j] == '?')
					grid[i][j] = grid[i-1][j];
			}
		}


		// four
		for (int j = 0; j < c; ++j)
		{
			for (int i = r-2; i >= 0; --i)
			{
				if(grid[i][j] == '?')
					grid[i][j] = grid[i+1][j];
			}
		}


		cout << "Case #" << test+1 << ":" << endl;
		for (int i = 0; i < r; ++i)
			cout << grid[i] << endl;

	}
	return 0;
}