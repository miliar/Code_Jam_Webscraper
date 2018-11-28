// D.cpp
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

void getT(int& T)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> T;
}

void getNM(int& N, int& M)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> N >> M;
}

using Grid = char[101][101];

void getCell(Grid& g)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	char c;
	int row;
	int col;
	ss >> c >> row >> col;
	g[row][col] = c;
}

void printGrid(const Grid& g, int size)
{
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (g[row][col] == 0)
				cout << '.';
			else if (g[row][col] == 1)
				cout << '.';
			else
				cout << g[row][col];
		}
		cout << endl;
	}
}

void transform(const Grid& in, Grid& out, char remain, int size)
{
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (in[row][col] == remain)
				out[row][col] = remain;
			else if (in[row][col] == 'o')
				out[row][col] = remain;
			else
				out[row][col] = 0;
		}
	}
}

bool placeableX(const Grid& g, int row, int col, int size)
{
	for (int c = 1; c <= size; ++c)
	{
		if (c != col && g[row][c] == 'x')
			return false;
	}
	for (int r = 1; r <= size; ++r)
	{
		if (r != row && g[r][col] == 'x')
			return false;
	}
	return true;
}

bool placeablePlus(const Grid& g, int row, int col, int size)
{
	int r, c;
	for (r = row + 1, c = col + 1; r <= size && c <= size; ++r, ++c)
	{
		if (g[r][c] == '+')
			return false;
	}
	for (r = row - 1, c = col - 1; r >= 1 && c >= 1; --r, --c)
	{
		if (g[r][c] == '+')
			return false;
	}
	for (r = row + 1, c = col - 1; r <= size && c >= 1; ++r, --c)
	{
		if (g[r][c] == '+')
			return false;
	}
	for (r = row - 1, c = col + 1; r >= 1 && c <= size; --r, ++c)
	{
		if (g[r][c] == '+')
			return false;
	}
	return true;
}

void fillX(Grid& g, int size)
{
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (placeableX(g, row, col, size))
				g[row][col] = 'x';
		}
	}
}

void setReserved(Grid& g, int row, int col, int size)
{
	int r, c;
	for (r = row + 1, c = col + 1; r <= size && c <= size; ++r, ++c)
	{
		if (g[r][c] == 0)
			g[r][c] = 1;
	}
	for (r = row - 1, c = col - 1; r >= 1 && c >= 1; --r, --c)
	{
		if (g[r][c] == 0)
			g[r][c] = 1;
	}
	for (r = row + 1, c = col - 1; r <= size && c >= 1; ++r, --c)
	{
		if (g[r][c] == 0)
			g[r][c] = 1;
	}
	for (r = row - 1, c = col + 1; r >= 1 && c <= size; --r, ++c)
	{
		if (g[r][c] == 0)
			g[r][c] = 1;
	}
}

void setReserved(Grid& g, int size)
{
	for (int r = 1; r <= size; ++r)
	{
		for (int c = 1; c <= size; ++c)
		{
			if (g[r][c] == '+')
			{
				setReserved(g, r, c, size);
			}
		}
	}
}

int countValue(Grid& g, int row, int col, int size)
{
	int count = 0;
	int r, c;
	for (r = row + 1, c = col + 1; r <= size && c <= size; ++r, ++c)
	{
		if (g[r][c] == 0)
			++count;
	}
	for (r = row - 1, c = col - 1; r >= 1 && c >= 1; --r, --c)
	{
		if (g[r][c] == 0)
			++count;
	}
	for (r = row + 1, c = col - 1; r <= size && c >= 1; ++r, --c)
	{
		if (g[r][c] == 0)
			++count;
	}
	for (r = row - 1, c = col + 1; r >= 1 && c <= size; --r, ++c)
	{
		if (g[r][c] == 0)
			++count;
	}
	return count;
}

bool select(Grid& g, int& row, int& col, int size)
{
	bool selectPossible = false;
	int minValue = 2 * size;
	int minRow, minCol;

	for (int r = 1; r <= size; ++r)
	{
		for (int c = 1; c <= size; ++c)
		{
			if (g[r][c] == 0)
			{
				selectPossible = true;
				int value = countValue(g, r, c, size);
				if (value < minValue)
				{
					minValue = value;
					minRow = r;
					minCol = c;
				}				
			}
		}
	}

	if (selectPossible)
	{
		row = minRow;
		col = minCol;
	}
	return selectPossible;
}

void fillPlus(Grid& g, int size)
{
	setReserved(g, size);
	int row, col;
	while (select(g, row, col, size))
	{
		g[row][col] = '+';
		setReserved(g, row, col, size);
	}
}

void merge(const Grid& x, const Grid& plus, Grid& out, int size)
{
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (x[row][col] == 'x' && plus[row][col] == '+')
				out[row][col] = 'o';
			else if (x[row][col] == 'x')
				out[row][col] = 'x';
			else if (plus[row][col] == '+')
				out[row][col] = '+';
		}
	}
}

void solve(Grid& in, Grid& out, int size)
{
	Grid x{};
	transform(in, x, 'x', size);
	fillX(x, size);

	//cout << "FILLED X" << endl;
	//printGrid(x, size);

	Grid plus{};
	transform(in, plus, '+', size);
	fillPlus(plus, size);

	//cout << "FILLED +" << endl;
	//printGrid(plus, size);

	merge(x, plus, out, size);

	//cout << "MERGED +" << endl;
	//printGrid(out, size);
}

int calcScore(const Grid& g, int size)
{
	int score = 0;
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (g[row][col] == '+')
				score += 1;
			else if (g[row][col] == 'x')
				score += 1;
			else if (g[row][col] == 'o')
				score += 2;
		}
	}
	return score;
}

int countAdded(const Grid& in, const Grid& out, int size)
{
	int count = 0;
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (in[row][col] != out[row][col])
			{
				++count;
			}
		}
	}
	return count;
}
void printAdded(const Grid& in, const Grid& out, int size)
{
	for (int row = 1; row <= size; ++row)
	{
		for (int col = 1; col <= size; ++col)
		{
			if (in[row][col] != out[row][col])
			{
				cout << out[row][col] << " " << row << " " << col << endl;
			}
		}
	}
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	getT(T);

	for (int t = 1; t <= T; ++t)
	{
		int N;
		int M;
		getNM(N, M);

		Grid in{};
		for (int i = 1; i <= M; ++i)
		{
			getCell(in);
		}

		//cout << "INPUT GRID " << endl;;
		//printGrid(in, N);

		int score = 0;
		int added = 0;
 
		Grid out{};
		solve(in, out, N);

		score = calcScore(out, N);
		added = countAdded(in, out, N);
		cout << "Case #" << t << ": " << score << " " << added << endl;
		printAdded(in, out, N);

	}

    return 0;
}

