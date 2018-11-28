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

vector < vector<int> > q;
int n, p;
int r[52];

int findi(int ind, int mul, int sta)
{
	while (sta < p)
	{
		if (0.9*r[ind] * mul <= q[ind][sta] && q[ind][sta] <= 1.1*r[ind] * mul)
			return sta;
		sta++;
	}
	return p;
}

int main() 
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		fin >> n >> p;

		for (int i = 0; i < n; i++)
			fin >> r[i];

		q.clear();
		for (int i = 0; i < n; i++)
		{
			vector <int> t;
			for (int j = 0; j < p; j++)
			{
				int te = 0;
				fin >> te;
				t.push_back(te);
			}
			q.push_back(t);
		}

		int num = 0;
		vector <int> ind;
		for (int i = 0; i < n; i++)
		{
			sort(q[i].begin(), q[i].end());
			ind.push_back(0);
		}

		bool done = false;
	    while (ind[0] < p)
	    {
				int indd = ind[0];
				if (q[0][indd] < 0.9*r[0])
				{
					ind[0]++;
					continue;
				}
				int rem = q[0][indd] % r[0];
				int div = (q[0][indd] - rem) / r[0];
				int low  = (10 * div) / 11 - 1;
				int high = (10 * div) / 9 + 2;
				low = max(1, low);
				bool found = false;
				int locind[52];

				for (int ratio = low; ratio <= high && !found; ratio++)
				{
					if (0.9*r[0] * ratio > q[0][indd] ||
						q[0][indd] > 1.1*r[0] * ratio)
						continue;

					bool imposs = false;
					for (int j = 1; j < n && !imposs; j++)
					{
						int lfi = findi(j, ratio, ind[j]);
						if (lfi >= p)
						{
							imposs = true;
							continue;
						}
						else
							locind[j] = lfi;
					}

					if (!imposs)
					{
						found = true;
						num++;
						for (int k = 1; k < n; k++)
						{
							ind[k] = locind[k]+1;
						}
					}
				}
				ind[0]++;
		}

        fout << "Case #" << tt + 1 << ": " << num << "\n";
	}

	return 0;
}

