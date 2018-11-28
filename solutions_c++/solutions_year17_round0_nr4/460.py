#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cassert>
using namespace std;

class GridElement
{
private:
	char m_model;		// . + x o
	bool m_horiz, m_cross;
	bool m_modified;

public:
	GridElement()
	{
		m_model = '.';
		m_horiz = m_cross = false;
		m_modified = false;
	}
	char getModel() const
	{
		return m_model;
	}
	bool isModified() const
	{
		return m_modified;
	}
	void markHoriz()
	{
		m_horiz = true;
	}
	void markCross()
	{
		m_cross = true;
	}
	void initialise(char model)
	{
		m_model = model;
		m_modified = false;
	}
	bool isLegal(char model)
	{
		if (model == '+')
			return !m_cross;
		else if (model == 'x')
			return !m_horiz;

		return false;
	}
	bool insert(char model)
	{
		if (!isLegal(model))
			return false;

		if (m_model == '.')
			m_model = model;
		else
			m_model = 'o';

		m_modified = true;
		return true;
	}
};

class Grid
{
private:
	GridElement m_grid[105][105];
	int m_N;

public:
	Grid(int N)
	{
		m_N = N;
	}
	int getScore(char model)
	{
		if (model == '.')
			return 0;
		else if (model == '+' || model == 'x')
			return 1;
		else if (model == 'o')
			return 2;
		else
			return -1;
	}
	bool inBound(int row, int col)
	{
		return row >= 1 && row <= m_N && col >= 1 && col <= m_N;
	}
	void markHoriz(int row, int col)
	{
		for (int k = 1; k <= m_N; ++k)
		{
			m_grid[row][k].markHoriz();
			m_grid[k][col].markHoriz();
		}
	}
	void markCross(int row, int col)
	{
		for (int i = row, j = col; inBound(i, j); --i, --j)
			m_grid[i][j].markCross();
		for (int i = row, j = col; inBound(i, j); --i, ++j)
			m_grid[i][j].markCross();
		for (int i = row, j = col; inBound(i, j); ++i, --j)
			m_grid[i][j].markCross();
		for (int i = row, j = col; inBound(i, j); ++i, ++j)
			m_grid[i][j].markCross();
	}
	void mark(char model, int row, int col)
	{
		if (model == '+')
			markCross(row, col);
		else if (model == 'x')
			markHoriz(row, col);
		else if (model == 'o')
		{
			markCross(row, col);
			markHoriz(row, col);
		}
	}
	void initialise(char model, int row, int col)
	{
		GridElement &curElem = m_grid[row][col];
		
		curElem.initialise(model);
		mark(model, row, col);
	}
	void insert(char model, int row, int col)
	{
		GridElement &curElem = m_grid[row][col];

		if (curElem.insert(model))
			mark(model, row, col);
	}
	int totalScore()
	{
		int ret = 0;
		for (int i = 1; i <= m_N; ++i)
			for (int j = 1; j <= m_N; ++j)
				ret += getScore(m_grid[i][j].getModel());
		return ret;
	}
	int totalMod()
	{
		int ret = 0;
		for (int i = 1; i <= m_N; ++i)
			for (int j = 1; j <= m_N; ++j)
				if (m_grid[i][j].isModified())
					++ret;
		return ret;
	}
	void printResult()
	{
		printf("%d %d\n", totalScore(), totalMod());
		for (int i = 1; i <= m_N; ++i)
			for (int j = 1; j <= m_N; ++j)
			{
				GridElement &curElem = m_grid[i][j];
				if (curElem.isModified())
					printf("%c %d %d\n", curElem.getModel(), i, j);
			}
	}
};

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d: ", tcase);
		int N, M;
		cin >> N >> M;
		Grid grid(N);
		for (int i = 0; i < M; ++i)
		{
			char model;
			int row, col;
			cin >> model >> row >> col;
			grid.initialise(model, row, col);
		}
		for (int k = 1; k <= N; ++k)
		{
			grid.insert('+', 1, k);
			grid.insert('+', N, k);
			grid.insert('+', k, 1);
			grid.insert('+', k, N);
		}
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				grid.insert('x', i, j);
		grid.printResult();
	}

	return 0;
}
