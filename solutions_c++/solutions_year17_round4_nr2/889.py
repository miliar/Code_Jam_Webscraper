
#include <stdio.h>
#include <vector>
#include <algorithm>

struct Problem
{
	int N;
	int C;
	int M;
	typedef std::vector<int> Ticket;
	std::vector<Ticket> customer;
	std::vector<int> count_seat;

	int debug[2][2];
	void Load()
	{
		memset(debug, 0, sizeof(debug));

		scanf("%d %d %d\n", &N, &C, &M);
		customer.resize(C);
		for (int i = 0; i < M; i++)
		{
			int s, c;
			scanf("%d %d\n",&s, &c);
			customer[c-1].push_back(s);
			if (count_seat.size() < s)
				count_seat.resize(s);
			count_seat[s-1]++;

			if (c <= 2)
				debug[c - 1][(s == 1) ? 0 : 1] ++;
		}
	}
};

struct Answer
{
	int ride;
	int promote;
	void Print(int id)
	{
		printf("Case #%d: %d %d\n", id, ride, promote);
	}
};

class Solver
{
public:
	Answer solve(const Problem* p)
	{
		int c0 = p->debug[0][0] + p->debug[0][1];
		int c1 = p->debug[1][0] + p->debug[1][1];
		int s0 = p->debug[0][0] + p->debug[1][0];

		Answer a;
		a.ride = c0;
		if (a.ride < c1)
			a.ride = c1;
		if (a.ride < s0)
			a.ride = s0;
		a.promote = 0;
		for (auto i = p->count_seat.begin(); i != p->count_seat.end(); i++)
		{
			if (*i > a.ride)
				a.promote += *i - a.ride;
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

