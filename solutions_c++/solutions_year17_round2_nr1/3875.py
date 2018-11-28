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
#include <unordered_set>
#include <unordered_map>

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
		double d; int n;
		fin >> d >> n;
		vector <double> tim;
		for (int i = 0; i < n; i++)
		{
			double k, s;
			fin >> k >> s;
			tim.push_back( (d-k)/s);
		}

		sort(tim.begin(), tim.end());
		double res = d / tim[n - 1];

		fout.precision(30);
        fout << "Case #" << tt + 1 << ": " << res << "\n";
	}

	return 0;
}

