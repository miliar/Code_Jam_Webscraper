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

int co(char c)
{
	return c - '0';
}

char oneL(char c)
{
	return c - 1;
}

int main() 
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
	    string s;
	    fin >> s;

		int pos = 1;
		int n = s.size();
		bool incr = true;
		while (pos < n && incr)
		{
			if (co(s[pos]) < co(s[pos - 1]))
				incr = false;
			pos++;
		}

		bool removeFirst = false;
		pos--;
		if (!incr)
		{
			for (int i = pos; i < n; i++)
				s[i] = '9';

			pos--;
			bool carry = true;
			while (carry)
			{
				if (pos == 0)
				{
					if (s[0] == '1')
						removeFirst = true;
					else
						s[0] = oneL(s[0]);

					carry = false;
				}
				else
				{
					s[pos] = oneL(s[pos]);
					if (co(s[pos]) >= co(s[pos - 1]))
						carry = false;
					else
					{
						s[pos] = '9';
						pos--;
					}
				}
			}
		}

			if (!removeFirst)
               fout << "Case #" << tt + 1 << ": " << s << "\n";
			else
			   fout << "Case #" << tt + 1 << ": " << s.substr(1) << "\n";
	}

	return 0;
}

