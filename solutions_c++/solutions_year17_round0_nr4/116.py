#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int score(char c)
{
	switch (c)
	{
	case 'o':
		return 2;
	case '+':
	case 'x':
		return 1;
	case '.':
		return 0;
	}

	return -1;
}

struct Command
{
	Command(char c_, int x_, int y_) : c(c_), x(x_), y(y_) {}

	void print()
	{
		printf("%c %d %d\n", c, x + 1, y + 1);
	}

	char c;
	int x;
	int y;
};

struct Input
{
	bool isPlusable(int x, int y)
	{
		//대각선에 이미 x 아닌게 있는지 확인 - 있으면 못 놓음(rule 2 위배)
		for (int nx = 0, ny = y - x; nx < N && ny < N; nx++, ny++)
		{
			if (ny < 0)
				continue;

			if (nx == x && ny == y)
				continue;

			if (board[nx][ny] != 'x' && board[nx][ny] != '.')
				return false;
		}

		for (int nx = 0, ny = x + y; nx < N && ny >= 0; nx++, ny--)
		{
			if (ny >= N)
				continue;

			if (nx == x && ny == y)
				continue;

			if (board[nx][ny] != 'x' && board[nx][ny] != '.')
				return false;
		}

		return true;
	}

	bool isXable(int x, int y)
	{
		//가로, 세로 줄에 이미 + 아닌게 있는지 확인. 있으면 못 놓음(rule 1 위배)
		for (int nx = 0; nx < N; nx++)
		{
			if (nx == x)
				continue;

			if (board[nx][y] != '+' && board[nx][y] != '.')
				return false;
		}

		for (int ny = 0; ny < N; ny++)
		{
			if (ny == y)
				continue;

			if (board[x][ny] != '+' && board[x][ny] != '.')
				return false;
		}

		return true;
	}

	static Input standard()
	{
		Input input;
		int M;
		scanf("%d %d", &input.N, &M);

		for (int x = 0; x < input.N; x++)
		{
			for (int y = 0; y < input.N; y++)
			{
				input.board[x][y] = '.';
			}
		}

		for (int i = 0; i < M; i++)
		{
			char c[5];
			int x, y;
			scanf("%s %d %d", c, &x, &y);

			input.board[x - 1][y - 1] = c[0];
		}

		return input;
	}

	static Input test()
	{
		Input input;

		input.N = rand() % 10 + 1;

		for (int x = 0; x < input.N; x++)
		{
			for (int y = 0; y < input.N; y++)
			{
				bool plusable = input.isPlusable(x, y);
				bool xable = input.isXable(x, y);

				if (plusable && xable)
				{
					switch (rand() % 3)
					{
					case 0:
						input.board[x][y] = '.';
						break;
					case 1:
						input.board[x][y] = '+';
						break;
					case 2:
						input.board[x][y] = 'x';
						break;
					}
				}
				else if (plusable && rand() % 2)
				{
					input.board[x][y] = '+';
				}
				else if (xable && rand() % 2)
				{
					input.board[x][y] = 'x';
				}
				else
				{
					input.board[x][y] = '.';
				}
			}
		}
		
		return input;
	}

	int N;
	char board[101][101];
};

struct Blank
{
	Blank(int x_, int y_, int num_) : x(x_), y(y_), num(num_) {}

	int x, y, num;
};

void solve()
{
	Input input = Input::standard();

	int totalScore = 0;
	std::vector<Command> commands;

	for (int x = 0; x < input.N; x++)
	{
		for (int y = 0; y < input.N; y++)
		{
			bool xable = input.isXable(x, y);
			
			if (xable && input.board[x][y] == '.')
			{
				//x놓기
				//어차피 한 줄당 하나 - 놓을 수 있는 위치는 거의 정해짐.
				input.board[x][y] = 'x';
				commands.emplace_back('x', x, y);
			}
		}
	}

	std::vector<Blank> blanks;

	//대각선 단위로 순회하면서, 대각선에 걸치는 빈칸 숫자 기록.
	for (int x = 0; x < input.N; x++)
	{
		for (int y = 0; y < input.N; y++)
		{
			if (input.board[x][y] != '.')
				continue;

			if (!input.isPlusable(x, y))
				continue;

			int num = 0;

			for (int nx = 0, ny = y - x; nx < input.N && ny < input.N; nx++, ny++)
			{
				if (ny < 0)
					continue;

				if (nx == x && ny == y)
					continue;

				if (input.board[nx][ny] == '.')
					num++;
			}

			for (int nx = 0, ny = x + y; nx < input.N && ny >= 0; nx++, ny--)
			{
				if (ny >= input.N)
					continue;

				if (nx == x && ny == y)
					continue;

				if (input.board[nx][ny] == '.')
					num++;
			}

			blanks.emplace_back(x, y, num);
		}
	}

	std::sort(blanks.begin(), blanks.end(), [](const auto& a, const auto& b) { return a.num < b.num; });

	for (auto& b : blanks)
	{
		if (!input.isPlusable(b.x, b.y))
			continue;

		input.board[b.x][b.y] = '+';
		commands.emplace_back('+', b.x, b.y);
	}

	for (int x = 0; x < input.N; x++)
	{
		for (int y = 0; y < input.N; y++)
		{
			bool plusable = input.isPlusable(x, y);
			bool xable = input.isXable(x, y);

			if (plusable && xable && input.board[x][y] != 'o')
			{
				input.board[x][y] = 'o';
				for (int i = 0; i < commands.size();)
				{
					if (commands[i].x == x && commands[i].y == y)
					{
						commands.erase(commands.begin() + i);
					}
					else
					{
						i++;
					}
				}
				commands.emplace_back('o', x, y);
			}

			totalScore += score(input.board[x][y]);
		}
	}

	printf("%d %d\n", totalScore, commands.size());

	for (auto& c : commands)
	{
		c.print();
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}