/*
ID: paradoxes
PROG: Bathroom Stalls
LANG: C++
*/

#include<iostream>
#include<fstream>

using namespace std;

int T;

long long int div2ceil(long long int a)
{
	if (a % 2 == 0)
		return a / 2;
	else
		return (a / 2) + 1;
}

void f(long long int S, long long int P, long long int& a, long long int& b)
{
	if (P == 1)
	{
		a = S / 2;
		b = (S - 1) / 2;

		return;
	}

	if (S % 2 == 1)
	{
		f(S / 2, div2ceil(P-1), a, b);
		return;
	}

	if (P % 2 == 0)
	{
		f(S + 1, P, a, b);
		return;
	}

	else
	{
		f(S - 1, P, a, b);
		return;
	}
}

int main()
{
	ifstream Input("stall.in");
	ofstream Output("stall.out");

	Input >> T;

	long long int a, b, S, P;

	for (int j = 1; j <= T; j++)
	{
		Input >> S >> P;

		f(S, P, a, b);

		Output << "Case #" << j << ": " << a << " " << b << endl;
	}

	return 0;
}