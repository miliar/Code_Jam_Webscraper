#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void doStuff(std::vector<std::string>& board, std::vector<std::vector<int> >& used, int nRows, int nCols)
{
	for (int r = 0; r < nRows; ++r)
	{
		for (int c = 0; c < nCols; ++c)
		{
			if (board[r][c] == '?' || used[r][c] == 1)
			{
				continue;
			}

			char cur = board[r][c];
			int l = c-1;
			int ri = c+1;
			int u = r-1;
			int d = r+1;

			while (ri < nCols)
			{
				if (board[r][ri] != '?')
				{
					ri--;
					break;
				}
				ri++;
			}

			while (l >= 0)
			{
				if (board[r][l] != '?')
				{
					l++;
					break;
				}
				l--;
			}

			if (l == -1)
			{
				l = 0;
			}
			if (ri == nCols)
			{
				ri = nCols-1;
			}

			bool done = false;
			while (u >= 0 && !done)
			{
				for (int i = l; i <= ri; ++i)
				{
					if (board[u][i] != '?')
					{
						u++;
						u++;
						done = true;
						break;
					}
				}
				u--;
			}

			done = false;
			while (d < nRows && !done)
			{
				for (int i = l; i <= ri; ++i)
				{
					if (board[d][i] != '?')
					{
						d--;
						d--;
						done = true;
						break;
					}
				}
				d++;
			}

			if (u == -1)
			{
				u = 0;
			}
			if (d == nRows)
			{
				d = nRows-1;
			}

			//std::cout << board[r][c] << ": " << l << ri << u << d << std::endl;

			for (int c2 = l; c2 <= ri; ++c2)
			{
				for (int r2 = u; r2 <= d; ++r2)
				{
						board[r2][c2] = cur;
						used[r2][c2] = 1;
				}
			}

		}
	}
}

int main(void)
{
	int nTests;
	std::cin >> nTests;
	for (int iTest = 1; iTest <= nTests; ++iTest)
	{
		std::cout << "Case #" << iTest << ": " << std::endl;

		int R, C;
		std::cin >> R >> C;

		std::vector<std::string> board;
		for (int iRow = 0; iRow < R; ++iRow)
		{
			std::string tmp;
			std::cin >> tmp;

			board.push_back(tmp);
		} 
		std::vector<int> zerosRow(C, 0);
		std::vector<std::vector<int> > used(R, zerosRow);

		doStuff(board, used, R, C);

		for (auto r : board)
		{
			std::cout << r << std::endl;
		}
	}
}