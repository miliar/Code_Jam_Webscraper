#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

ifstream fin;
ofstream fout;

typedef vector<vector<bool> > vvb;

struct Grid {
	vvb plus;
	vvb diagonal;
	int gridSize;
};

void Init(Grid& gr)
{
	int n, m;
	fin >> n >> m;
	int size = n;
	gr.gridSize = size;
	gr.plus.resize(n);
	gr.diagonal.resize(n);
	for (int i = 0; i < n; i++)
	{
		gr.plus[i].resize(n);
		gr.diagonal[i].resize(n);
	}

	for (int i = 0; i < m; i++)
	{
		char symbol;
		int x, y;
		fin >> symbol >> x >> y;
		x--;
		y--;
		if ((symbol == '+') || (symbol == 'o'))
		{
			gr.plus[x][y] = true;
		}

		if ((symbol == 'x') || (symbol == 'o'))
		{
			gr.diagonal[x][y] = true;
		}
	}
}

void copyGrid(Grid& start, Grid& end)
{
	int size = start.gridSize;
	end.gridSize = size;
	end.diagonal.resize(size);
	end.plus.resize(size);
	for (int i = 0; i < size; i++)
	{
		end.diagonal[i].resize(size);
		end.plus[i].resize(size);
	}

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			end.diagonal[i][j] = start.diagonal[i][j];
			end.plus[i][j] = start.plus[i][j];
		}
	}

}

void SolveDiagonal(Grid& gr)
{
	int size = gr.gridSize;
	vector<bool> rows(size);
	vector<bool> cols(size);
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (gr.diagonal[i][j])
			{
				rows[i] = true;
				cols[j] = true;
			}
		}
	}

	vector<int> emptyRows(0);
	vector<int> emptyCols(0);
	for (int i = 0; i < size; i++)
	{
		if (!rows[i])
			emptyRows.push_back(i);
		if (!cols[i])
			emptyCols.push_back(i);
	}

	for (int i = 0; i < emptyRows.size(); i++)
	{
		gr.diagonal[emptyRows[i]][emptyCols[i]] = true;
	}
}

void PrintResult(Grid& start,Grid& end)
{
	int size = start.gridSize;
	int count = 0;
	int earn = 0;
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if ((start.diagonal[i][j] != end.diagonal[i][j]) ||
				(start.plus[i][j] != end.plus[i][j]))
			{
				count++;
			}

			if (end.diagonal[i][j])
			{
				earn++;
			}

			if (end.plus[i][j])
			{
				earn++;
			}
		}
	}

	fout << earn << " " << count << endl;
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if ((start.diagonal[i][j] == end.diagonal[i][j]) &&
				(start.plus[i][j] == end.plus[i][j]))
			{
				continue;
			}

			char symbol;
			if (end.diagonal[i][j] && end.plus[i][j])
			{
				symbol = 'o';
			}

			else if (end.diagonal[i][j])
			{
				symbol = 'x';
			}

			else
			{
				symbol = '+';
			}

			fout << symbol << " " << i + 1 << " " << j + 1 << endl;
		}
	}
}

void SolvePlus(Grid& gr)
{
	int size = gr.gridSize;
	for (int i = 0;i < size; i++)
	{
		gr.plus[0][i] = true;
	}

	if (size > 1)
	{
		for (int i = 1; i < size - 1; i++)
		{
			gr.plus[size - 1][i] = true;
		}
	}
}


int main()
{
	fin.open("D-small-attempt0.in");
	fout.open("output.txt");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << t;
		fout << "Case #" << t + 1 << ": ";
		Grid Start, End;
		Init(Start);
		copyGrid(Start,End);
		SolvePlus(End);
		SolveDiagonal(End);
		PrintResult(Start,End);
	}

	return 0;
}