
#include <stdio.h>
#include <string.h>

const int MAX_SIZE = 100;
struct Problem
{
	char board[MAX_SIZE][MAX_SIZE+2];
	int  size;
	void Load()
	{
		int n;
		memset(board, ' ', sizeof(board));
		scanf("%d %d\n", &size, &n);
		for (int i = 0; i < n; i++)
		{
			int r, c;
			char p;
			scanf("%c %d %d\n", &p, &r, &c);
			board[r-1][c-1] = p;
		}
		//debug
		for (int i = 0; i < size; i++)
		{
			board[i][size] = '\n';
			board[i][size+1] = '\0';
		}
	}
	//debug print
	void DebugPrint()
	{
		for (int i = 0; i < size; i++)
			printf("%s",board[i]);
	}
};

struct Answer
{
	struct
	{
		int r;
		int c;
		char p;
	}results[MAX_SIZE*MAX_SIZE];
	int score;
	int len;
	void Print(int id)
	{
		printf("Case #%d: %d %d\n", id, score, len);
		for (int i = 0; i < len; i++)
			printf("%c %d %d\n", results[i].p, results[i].r, results[i].c);
	}
};

class Solver
{
	void solveHV(Problem& state)
	{
		bool check_x[MAX_SIZE];
		bool check_y[MAX_SIZE];
		for (int i = 0; i < MAX_SIZE; i++)
		{
			check_x[i] = true;
			check_y[i] = true;
		}
		int x, y;
		for (x = 0; x < state.size; x++)
		{
			for (y = 0; y < state.size; y++)
			{
				if ((state.board[y][x] == 'o')
					|| (state.board[y][x] == 'x'))
				{
					check_x[x] = false;
					check_y[y] = false;
				}
			}
		}
		y = 0;
		for (x = 0; x < state.size; x++)
		{
			if (check_x[x])
			{
				while ((y<state.size) &&!check_y[y]) y++;
				if (y < state.size)
				{
					check_x[x] = false;
					check_y[y] = false;
					if ((state.board[y][x] == '+') || (state.board[y][x] == 'o'))
						state.board[y][x] = 'o';
					else
						state.board[y][x] = 'x';
				}
			}
		}
	}
	void solveDiag(Problem& state)
	{
		bool check_p_diag[MAX_SIZE * 2 - 1];
		bool check_n_diag[MAX_SIZE * 2 - 1]; // idx =  y - x + state.size - 1
		for (int i = 0; i < MAX_SIZE* 2 -1; i++)
		{
			check_p_diag[i] = true;
			check_n_diag[i] = true;
		}
		int x, y;
		for (x = 0; x < state.size; x++)
		{
			for (y = 0; y < state.size; y++)
			{
				if ((state.board[y][x] == 'o')
					|| (state.board[y][x] == '+'))
				{
					check_p_diag[x + y] = false;
					check_n_diag[y - x + state.size - 1] = false;
				}
			}
		}
		for (int abs_n = state.size - 1; abs_n >= 0; abs_n--)
		{
			for (y = abs_n, x = 0; y < state.size; x++,y++)
			{
				if (check_p_diag[x + y] && check_n_diag[y - x + state.size - 1])
				{
					check_p_diag[x + y] = false;
					check_n_diag[y - x + state.size - 1] = false;
					if ((state.board[y][x] == 'x') || (state.board[y][x] == 'o'))
						state.board[y][x] = 'o';
					else
						state.board[y][x] = '+';
					break;
				}
			}
			for (y = 0, x = abs_n; x < state.size; x++, y++)
			{
				if (check_p_diag[x + y] && check_n_diag[y - x + state.size - 1])
				{
					check_p_diag[x + y] = false;
					check_n_diag[y - x + state.size - 1] = false;
					if ((state.board[y][x] == 'x') || (state.board[y][x] == 'o'))
						state.board[y][x] = 'o';
					else
						state.board[y][x] = '+';
					break;
				}
			}
		}
	}
	Answer CalcAns(const Problem* start, const Problem* end)
	{
		Answer rv;
		rv.score = 0;
		rv.len = 0;
		int x, y;
		for (x = 0; x < start->size; x++)
		{
			for (y = 0; y < start->size; y++)
			{
				if (start->board[y][x] != end->board[y][x])
				{
					rv.results[rv.len].r = y + 1;
					rv.results[rv.len].c = x + 1;
					rv.results[rv.len].p = end->board[y][x];
					rv.len++;
				}
				switch (end->board[y][x])
				{
				case 'o':
					rv.score += 2;
					break;
				case 'x':
				case '+':
					rv.score++;
					break;
				}
			}
		}
		return rv;
	}
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		Problem current = *p;
//		current.DebugPrint();
		solveHV(current);
//		current.DebugPrint();
		solveDiag(current);
//		current.DebugPrint();
		a = CalcAns(p, &current);
		return a;
	}
};


int main(int argc, char* argv[])
{

	int num;
	scanf("%d", &num);

	for (int i = 1; i < num + 1; i++)
	{
		Solver solver;
		Problem p;
		Answer a;
		p.Load();
		a = solver.solve(&p);
		a.Print(i);
	}

	return 0;
}

