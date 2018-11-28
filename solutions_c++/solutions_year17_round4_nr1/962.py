
#include <stdio.h>

#define MAX_P  4

struct Problem
{
	int P;
	int count[MAX_P];
	void Load()
	{
		for (int i = 0; i < MAX_P; i++)
			count[i] = 0;
		int n;
		scanf("%d %d\n", &n, &P);
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			count[x%P]++;
		}
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
public:
	Answer solve(const Problem* _p)
	{
		Problem p = *_p;
		Answer a;
		// can divide
		a.a = p.count[0]; p.count[0] = 0;
		// pair 2
		for (int i = 1; i <= p.P/2; i++)
		{
			int ti = p.P - i;
			if (i == ti)
			{
				a.a += p.count[i] / 2;
				p.count[i] = p.count[i] % 2;
			}
			else
			{
				int x = p.count[i];
				if (x > p.count[ti])
					x = p.count[ti];
				a.a += x;
				p.count[i] -= x;
				p.count[ti] -= x;
			}
		}
		if (p.P == 4)
		{
			while (p.count[2] > 0)
			{
				if (p.count[1] >= 2)
				{
					p.count[2]--;
					p.count[1] -= 2;
					a.a++;
				}
				else if (p.count[3] >= 2)
				{
					p.count[2]--;
					p.count[3] -= 2;
					a.a++;
				}
				else
					break;
			}
		}
		for (int i = 1; i < p.P; i++)
		{
			a.a += p.count[i] / p.P;
			p.count[i] %= p.P;
		}
		for (int i = 1; i < p.P; i++)
		{
			if (p.count[i] > 0)
			{
				a.a++;
				break;
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

