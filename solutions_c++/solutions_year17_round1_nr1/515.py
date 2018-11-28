// Google Code Jam 2017, Round 1A - problem A
// "???"
// Andras Eles, Veszprem, Hungary, 2017.04.13.

#include <iostream>
using namespace std;

typedef unsigned long int uint;

class Matrix
{
public:
	uint R;
	uint C;
	char* m;
public:
	Matrix (void)
	{
		cin >> R >> C;
		m = new char [R * C];
		for (uint r=0;r<R;r++)
		{
			for (uint c=0;c<C;c++)
			{
				cin >> at(r,c);
			}
		}
	}
	~Matrix (void)
	{
		delete [] m;
	}
	char& at (uint r, uint c)
	{
		return m[r * C + c];
	}
	void print (void)
	{
		cout << endl;
		for (uint r=0;r<R;r++)
		{
			for (uint c=0;c<C;c++)
			{
				cout << at(r,c);
			}
			cout << endl;
		}
	}
	void solve (void)
	{
		solve(0,R,0,C);
	}
	void solve (uint rb, uint re, uint cb, uint ce)
	{
		bool was = false;
		uint fr = 0, fc = 0; char f;
		uint lr = 0, lc = 0;
		for (uint r=rb;r<re;r++)
		{
			for (uint c=cb;c<ce;c++)
			{
				if (at(r,c) != '?')
				{
					if (!was)
					{
						was = true;
						f = at(r,c);
						fr = r;
						fc = c;
					}
					lr = r;
					lc = c;
				}
			}
		}
		if (fr == lr && fc == lc)
		{
			for (uint r=rb;r<re;r++)
			{
				for (uint c=cb;c<ce;c++)
				{
					at(r,c) = f;
				}
			}
			return;
		}
		if (fr < lr)
		{
			solve(rb,lr,cb,ce);
			solve(lr,re,cb,ce);
		}
		else
		{
			solve(rb,re,cb,lc);
			solve(rb,re,lc,ce);
		}
	}
};

void solveProblem (void)
{
	Matrix M;
	M.solve();
	M.print();
}

int main (int argc, char** argv)
{
	int T;
	cin >> T;
	for (int t=1;t<=T;t++)
	{
		cout << "Case #" << t << ": " << flush;
		solveProblem();
	}
	return 0;
}
