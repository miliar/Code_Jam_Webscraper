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

long long le[65];
long long mu[65];

int main() 
{
	le[0] = 0;
	long long mul = 1;
	for (long long i = 1; i < 65; i++)
	{
		mu[i] = mul;
		le[i] = le[i - 1] + mul;
		mul = 2 * mul;
	}

	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		long long n, k;
		fin >> n >> k;
		int i = 0;
		while (le[i] < k)
			i++;

		long long fr = n - le[i - 1];
		long long rem = fr%mu[i];
		long long qu = (fr - rem) / mu[i];
		long long remk = k - le[i - 1];
		long long inter = qu;
		if (remk <= rem)
			inter++;

		long long ls, rs;
		if (inter % 2 == 1)
		{
			ls = (inter - 1) / 2;
			rs = ls;
		}
		else
		{
			ls = (inter - 2) / 2;
			rs = ls + 1;
		}

        fout << "Case #" << tt + 1 << ": " << rs << " " << ls  << "\n";
	}

	return 0;
}

