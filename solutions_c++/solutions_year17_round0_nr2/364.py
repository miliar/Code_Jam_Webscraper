
#include <stdio.h>
#include <string.h>


struct Problem
{
	char s[20]; 
	void Load()
	{
		scanf("%s", &s);
	}
};

struct Answer
{
	char s[20];
	void Print(int id)
	{
		printf("Case #%d: %s\n", id, s);
	}
};

class Solver
{
public:
	Answer solve(const Problem* p)
	{
		Answer a;
		char s[20];
		strcpy(s, p->s);
		int i;
		while (1)
		{
			// exit check
			for (i = 1; s[i] != '\0'; i++)
			{
				if (s[i - 1] > s[i])
					break;
			}
			if (s[i] == '\0')
			{// exit
				for (i = 0; s[i] == '0'; i++)
					/* do nothing */;
				strcpy(a.s, s + i);
				return a;
			}

			for (i = 1; s[i] != '\0'; i++)
			{
				if (s[i - 1] > s[i])
				{
					s[i - 1]--;
					for (; s[i] != '\0'; i++)
						s[i] = '9';
					break;
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

