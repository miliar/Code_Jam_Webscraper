// b-neigh.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

void swap(char & a, char & b)
{
	char tmp = a;
	a = b;
	b = tmp;
}

void check(char & a, char & b, char & c)
{
	if (a == 'R')
	{
		if (b == 'O' || b == 'V' || b == 'R')
		{
			swap(b, c);
		}
	}
	else if (a == 'O')
	{
		if (b == 'Y' || b == 'R' || b == 'O')
		{
			swap(b, c);
		}
	}
	else if (a == 'Y')
	{
		if (b == 'G' || b == 'O' || b == 'Y')
		{
			swap(b, c);
		}
	}
	else if (a == 'G')
	{
		if (b == 'B' || b == 'Y' || b == 'G')
		{
			swap(b, c);
		}
	}
	else if (a == 'B')
	{
		if (b == 'V' || b == 'G' || b == 'B')
		{
			swap(b, c);
		}
	}
	else if (a == 'V')
	{
		if (b == 'R' || b == 'B' || b == 'V')
		{
			swap(b, c);
		}
	}
}

bool isPossible(const int & u, const int & a, const int & b, const int & c)
{
	int sum = (a <= b ? a : b) + b + (c <= b ? c : b);
	if (sum == 0)
	{
		return true;
	}

	if ((u / sum) < 2)
	{
		return false;
	}

	return true;
}

void runCase()
{
	int numUnicorns, red, orange, yellow, green, blue, violet;
	cin >> numUnicorns >> red >> orange >> yellow >> green >> blue >> violet;

	if (!isPossible(numUnicorns, red, orange, yellow) ||
		!isPossible(numUnicorns, orange, yellow, green) ||
		!isPossible(numUnicorns, yellow, green, blue) ||
		!isPossible(numUnicorns, green, blue, violet) ||
		!isPossible(numUnicorns, blue, violet, red) ||
		!isPossible(numUnicorns, violet, red, orange))
	{
		cout << "IMPOSSIBLE";
		return;
	}
	else
	{
		char *stalls = new char[numUnicorns];

		for (int i = 0; i < numUnicorns;)
		{
			if (red > 0)
			{
				stalls[i++] = 'R';
				red--;
			}

			if (yellow > 0)
			{
				stalls[i++] = 'Y';
				yellow--;
			}

			if (violet > 0)
			{
				stalls[i++] = 'V';
				violet--;
			}

			if (green > 0)
			{
				stalls[i++] = 'G';
				green--;
			}

			if (orange > 0)
			{
				stalls[i++] = 'O';
				orange--;
			}

			if (blue > 0)
			{
				stalls[i++] = 'B';
				blue--;
			}
		}

		for (int j = 0; j < 1000; j++)
		{
			for (int i = 0; i < numUnicorns; i++)
			{
				
				if (i == numUnicorns - 2)
				{
					check(stalls[i], stalls[i + 1], stalls[0]);
				}
				else if (i == numUnicorns - 1) 
				{ 
					check(stalls[i], stalls[0], stalls[1]);
				}
				else
				{
					check(stalls[i], stalls[i + 1], stalls[i + 2]);
				}
			}
		}

		for (int i = 0; i < numUnicorns; i++)
		{
			cout << stalls[i];
		}

		delete [] stalls;
	}
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		runCase();
		cout << endl;
	}

	return 0;
}

