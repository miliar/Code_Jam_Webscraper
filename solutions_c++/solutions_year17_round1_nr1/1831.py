// Google2017R1-A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>

using namespace std;


inline int max(int x, int y)
{
	int t = x;
	if (y > x)
		t = y;
	return y;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in", std::ios_base::in);
	output.open("A-large-output.txt");

	int T;
	input >> T;

	for (int g = 0; g < T; g++)
	{
		int r, c;
		input >> r >> c;
		vector<string> grid(r);
		vector<int> x;
		vector<int> y;
		vector<char> C;


		for (int i = 0; i < r; i++)
			input >> grid[i];
		for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (grid[i][j] != '?')
			{
				x.push_back(i);
				y.push_back(j);
				C.push_back(grid[i][j]);
			}
		}

		int m = C.size();
		for (int i = 0; i < r; i++)
		{
			for (int j = 1; j < c; j++)
			{
				if (grid[i][j] == '?')
					grid[i][j] = grid[i][j - 1];

			}
			for (int j = c - 2; j >= 0; j--)
			{
				if (grid[i][j] == '?')
					grid[i][j] = grid[i][j + 1];

			}
		}

		for (int j = 0; j < c; j++)
		{
			for (int i = 1; i < r; i++)
			{
				if (grid[i][j] == '?')
					grid[i][j] = grid[i - 1][j];

			}
			for (int i = r - 2; i >= 0; i--)
			{
				if (grid[i][j] == '?')
					grid[i][j] = grid[i+ 1][j];
			}
		}

		output << "Case #" << g + 1 << ":\n";
		for (int i = 0; i < r; i++)
			output << grid[i] <<"\n";
		
	}
	input.close();
	output.close();
	
	return 0;
}



