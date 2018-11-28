
#include <stdio.h>
#include <string.h>

struct Problem
{
	char S[1001];
	int  K;
	void Load()
	{
		scanf("%s %d", &S, &K);
	}
};

struct Answer
{
	int a;
	void Print(int id)
	{
		if (a >= 0)
			printf("Case #%d: %d\n", id, a);
		else
			printf("Case #%d: IMPOSSIBLE\n", id);

	}
};

class Solver
{
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		char s[sizeof(p->S)];
		strcpy(s, p->S);
		a.a = 0;
		int i = 0;
		while (s[i] != '\0')
		{
			if (s[i] == '+')
				i++;
			else
			{
				a.a++;
				for (int j = 0; j < p->K; j++)
				{
					switch (s[i+j])
					{
					case '+':
						s[i + j] = '-';
						break;
					case '-':
						s[i + j] = '+';
						break;
					case '\0':
						a.a = -1;
						return a;
					}
				}
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

