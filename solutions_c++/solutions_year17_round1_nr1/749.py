
#include <stdio.h>
#include <string.h>

#define MAX 25
struct Problem
{
	char c[MAX][MAX+1];
	int H, W;
	void Load()
	{
		scanf("%d %d\n", &H, &W);
		for (int y = 0; y < H; y++)
			scanf("%25s\n", &c[y]);
	}
};

struct Answer
{
	char c[MAX][MAX + 1];
	int H, W;
	void Print(int id)
	{
		printf("Case #%d: \n", id);
		for (int y = 0; y < H; y++)
			printf("%s\n",c[y]);
	}
};

class Solver
{
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		memcpy(a.c, p->c, sizeof(a.c));
		a.H = p->H;
		a.W = p->W;
		bool is_q_line[MAX];
		for (int y = 0; y < a.H; y++)
		{
			char t = '?';
			for (int x = 0; x < a.W; x++)
				if (a.c[y][x] == '?')
					a.c[y][x] = t;
				else
					t = a.c[y][x];
			is_q_line[y] = (t == '?');
			for (int x = a.W - 1; x >=0 ; x--)
				if (a.c[y][x] == '?')
					a.c[y][x] = t;
				else
					t = a.c[y][x];
		}
		for (int y = 1; y < a.H; y++)
		{
			if (is_q_line[y])
			{
				memcpy(a.c[y], a.c[y-1], sizeof(a.c[0]));
				is_q_line[y] = is_q_line[y - 1];
			}
		}
		for (int y = a.H-2; y >= 0; y--)
		{
			if (is_q_line[y])
			{
				memcpy(a.c[y], a.c[y + 1], sizeof(a.c[0]));
				is_q_line[y] = is_q_line[y + 1];
			}
		}
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

