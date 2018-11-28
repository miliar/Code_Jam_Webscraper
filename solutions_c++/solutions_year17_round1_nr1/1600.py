#include<fstream>

using namespace std;

#define R 25
#define C 25

char grid[R][C];

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		int r, c;

		in >> r >> c;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				in >> grid[i][j];
			}

		for (int i = 0; i < r; i++)
		{
			int first = -1;
			for (int j = 0; j < c; j++)
			{
				if (grid[i][j] != '?')
				{
					first = j;
					break;
				}
			}
			if (first != -1)
			{
				int j;
				for (j = 0; j < c && (grid[i][j] == '?' || grid[i][j] == grid[i][first]); j++)
				{
					grid[i][j] = grid[i][first];
				}

				while (j < c - 1)
				{
					if (grid[i][j + 1] == '?') grid[i][j + 1] = grid[i][j];
					j++;
				}
			}
		}

		int cur_row;
		for (cur_row = 0; cur_row < r && grid[cur_row][0] == '?'; cur_row++);

		for (int i = 0; i < cur_row; i++)
		{
			for (int j = 0; j < c; j++)
			{
				grid[i][j] = grid[cur_row][j];
			}
		}

		cur_row++;
		while (cur_row < r)
		{
			if (grid[cur_row][0] == '?')
				for (int j = 0; j < c; j++)
				{
					grid[cur_row][j] = grid[cur_row - 1][j];
				}
			cur_row++;
		}

		out << "Case #" << test_case + 1 << ":" << endl;

		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				out << grid[i][j];
			}
			out << endl;
		}
	}
}