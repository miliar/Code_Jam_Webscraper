#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <vector>


int main()
{
#ifdef TEST
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int t = 0; t < numOfTestcases; ++t)
	{
		std::cout << "Case #" << (t + 1) << ":" << std::endl;

		int rows, columns;
		std::cin >> rows >> columns;

		std::vector<std::vector<char>> board(rows, std::vector<char>(columns, '?'));

		for (int i = 0; i < rows; ++i)
		{
			for (int j = 0; j < columns; ++j)
			{
				char c;
				std::cin >> c;
				board[i][j] = c;
			}
		}

		for (int i = 0; i < rows; ++i)
		{
			bool found = false;
			char lastChar = '?';
			for (int j = 0; j < columns; ++j)
			{
				if (board[i][j] != '?')
				{
					lastChar = board[i][j];
					found = true;
				}
				else
				{
					board[i][j] = lastChar;
				}
			}

			if (found)
			{
				lastChar = '?';
				for (int j = 0; j < columns; ++j)
				{
					if (board[i][columns - j - 1] != '?')
					{
						lastChar = board[i][columns - j - 1];
					}
					else
					{
						board[i][columns - j - 1] = lastChar;
					}
				}
			}
			else
			{
				if (i > 0)
				{
					for (int j = 0; j < columns; ++j)
					{
						board[i][j] = board[i - 1][j];
					}
				}
			}
		}

		for (int i = 0; i < rows; ++i)
		{
			bool found = false;
			for (int j = 0; j < columns; ++j)
			{
				if (board[rows - i - 1][j] != '?')
				{
					found = true;
				}
			}

			if (!found)
			{
				for (int j = 0; j < columns; ++j)
				{
					board[rows - i - 1][j] = board[rows - i][j];
				}
			}
		}

		for (int i = 0; i < rows; ++i)
		{
			for (int j = 0; j < columns; ++j)
			{
				std::cout << board[i][j];
			}
			std::cout << std::endl;
		}
	}
}