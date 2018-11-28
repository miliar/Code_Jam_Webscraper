
#include <stdio.h>
#include <string.h>
#include <algorithm>

#define RMAX 50
#define QMAX 50

struct Problem
{
	int N;
	int P;
	int R[RMAX];
	int Q[RMAX][QMAX];
	void Load()
	{
		scanf("%d %d\n", &N, &P);
		for (int i = 0; i < N; i++)
			scanf("%d", &R[i]);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);
		for (int i = 0; i < N; i++)
			std::sort(Q[i], Q[i] + P);
	}
};

struct Answer
{
	int a;
	void Print(int id)
	{
		printf("Case #%d: %d\n", id, a);
	}
};

class Solver
{
	int idx[RMAX];
	bool findPackage(const Problem* p)
	{
		int min_i = 0;
		int n_min, n_max;
		while (1)
		{
			n_min = (p->Q[0][idx[0]] * 10 + p->R[0] * 11 - 1) / (p->R[0] * 11);
			n_max = (p->Q[0][idx[0]] * 10) / (p->R[0] * 9);
			for (int i = 0; i < p->N; i++)
			{
				if (idx[i] == p->P)
					return false;
				float t = p->Q[i][idx[i]] / (float)p->R[i];
				int t_min = (p->Q[i][idx[i]] * 10 + p->R[i] * 11 - 1) / (p->R[i] * 11);
				int t_max = (p->Q[i][idx[i]] * 10) / (p->R[i] * 9);
				if (t_min > n_min)
					n_min = t_min;
				if (t_max < n_max)
				{
					n_max = t_max;
					min_i = i;
				}
			}
			if (n_max < n_min)
				idx[min_i] ++;
			else
			{
				for (int i = 0; i < p->N; i++)
					idx[i]++;
				break;
			}
		}
		return true;
	}
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		a.a = 0;
		memset(idx, 0, sizeof(idx));
		while (findPackage(p))
			a.a++;
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

