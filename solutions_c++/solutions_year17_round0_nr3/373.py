
#include <stdio.h>


struct Problem
{
	int N;
	int K;
	void Load()
	{
		scanf("%d %d", &N, &K);
	}
};

struct Answer
{
	int min;
	int max;
	void Print(int id)
	{
		printf("Case #%d: %d %d\n", id, max, min);
	}
};

class Solver
{
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		//check (2^T-1) <K
		int T = 0;
		while (p->K > 2 * T + 1)
			T = 2 * T + 1;
		// there are 2 type of room, X and X+1;
		int X = (p->N - T) / (T + 1);
		int num_X_1 = (p->N - T) % (T + 1);
		int rest = p->K - T;
		if (rest <= num_X_1)
			X++;
		a.min = (X - 1) / 2;
		a.max = (X - 1) - a.min;
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

