#include <set>
#include <numeric>
#include <memory>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <map>
#include <iterator>
#include <string>
#include <iostream>
#include <math.h>

#include <fstream>
//#include "inf_int.h"
using inf_int = int;
using namespace std;

string make(int n)
{
	string s;

	for (int i = 0; i < n; i++)
	{
		s += '-';
	}

	return s;
}

string makeLonger(int n)
{
	string s;

	for (int i = 0; i < n + 1; i++)
	{
		if (i == 0 || i == n)
		{
			s += '-';
		}
		else
		{
			s += '+';
		}
	}

	return s;
}

int main()
{
	ios::sync_with_stdio(false);
	ifstream in{ "input.txt" , ios::in };
	ofstream out{ "output.txt", ios::out };

	int testCase;
	in >> testCase;

	for (int i = 0; i < testCase; i++)
	{
		int p, r;
		in >> r >> p;
		inf_int people{ p }, stall{ r };
		set<inf_int> stalled;

		stalled.insert(1);
		stalled.insert(stall + 2);

		auto finalIter = --stalled.end();
		inf_int finalDest = 0;
		inf_int currentDist = -1;
		auto savedIter = stalled.begin(), prevSaved = stalled.begin();

		while (people-- != 0)
		{
			currentDist = -1;
			for (auto iter = stalled.begin(); iter != finalIter; )
			{
				auto prevIter = iter++;
				inf_int dist = abs(*iter - *prevIter);

				if (dist > currentDist)
				{
					currentDist = dist;
					finalDest = *prevIter + (currentDist / 2);
					savedIter = iter;
					prevSaved = prevIter;
				}

			}

			stalled.insert(finalDest);
		}
		int x = *savedIter - finalDest - 1, y = finalDest - *prevSaved - 1;
		if (x < y)
		{
			swap(x, y);
		}

		cout << i << endl;
		out << "Case #" << (i + 1) << ": " << x << " " << y << endl;
	}

	return 0;
}
