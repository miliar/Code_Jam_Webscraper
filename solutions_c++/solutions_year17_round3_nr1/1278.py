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

double pi = 3.141592653589793238462643;

int main()
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		int n, k;
		fin >> n >> k;
		vector <double> rad;
		vector <vector<double> > sidear;
		for (int i = 0; i < n; i++)
		{
			double r, h;
			fin >> r >> h;
			rad.push_back(r);
			double si = 2*pi*r*h;
			vector <double> te;
			te.push_back(si);
			te.push_back(r);
			sidear.push_back(te);
		}


		sort(sidear.begin(), sidear.end());
		reverse(sidear.begin(), sidear.end());

		double bes = 0;
		for (int i = 0; i < sidear.size(); i++)
		{
			int curnum = 1;
			double currad = sidear[i][1];
			double curarea = pi*currad*currad + sidear[i][0];
			for (int j = 0; j < sidear.size() && curnum < k; j++)
			{
				if (i != j)
				{
					if (sidear[j][1] <= currad)
					{
						curnum++;
						curarea += sidear[j][0];
					}
				}
			}
			if (curnum == k)
			{
				bes = max(bes, curarea);
			}
		}

		fout.precision(60);
		fout << "Case #" << tt + 1 << ": " << bes << "\n";
	}

	return 0;
}

