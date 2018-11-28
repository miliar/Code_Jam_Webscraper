#include "stdafx.h"
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>

#include <math.h>

using namespace std;

ofstream fout("OUT111.txt");
ifstream fin("INP111.txt");


int main() 
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		string s;
		fin >> s;
		int k;
		fin >> k;

		int res = 0;
		int numf = 0;
		queue <int> q;
		int pos = 0;
		bool poss = true;
		while (poss && pos < s.size())
		{
			if ((s[pos] == '-' && numf == 0) || (s[pos] == '+' && numf == 1))
			{
				if (pos + k > s.size())
					poss = false;
				else
				{
					q.push(pos + k - 1);
					numf = 1 - numf;
					res++;
				}
			}

			pos++;
			if (!q.empty())
			{
				if (q.front() < pos)
				{
					q.pop();
					numf = 1 - numf;
				}
			}
		}

		if (poss)
		    fout << "Case #" << tt + 1 << ": " << res << "\n";
		else
			fout << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << "\n";
	}

	return 0;
}

