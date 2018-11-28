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
		int r, c;
		fin >> r >> c;
		vector <string> cak;
		for (int i = 0; i < r; i++)
		{
			string te;
			fin >> te;
			cak.push_back(te);
		}
		int left = 0;
		int right = 0;
		while (left < c && right < c)
		{
			right = left;
			bool found = false;
			while (!found && right < c)
			{
				for (int i = 0; i < r && !found; i++)
				{
					if (cak[i][right] != '?')
						found++;
				}
				if (!found)
					right++;
			}
			if (found)
			{
				vector <int> indx;
				indx.push_back(-1);
				for (int i = 0; i < r; i++)
				{
					if (cak[i][right] != '?')
					indx.push_back(i);
				}
				for (int i = 1; i < indx.size(); i++)
				{
					for (int x = indx[i - 1] + 1; x <= indx[i]; x++)
					{
						for (int y = left; y <= right; y++)
							cak[x][y] = cak[indx[i]][right];
					}
				}
				int nn = indx.size();
				for (int x = indx[nn-1] + 1; x < r; x++)
				{
					for (int y = left; y <= right; y++)
						cak[x][y] = cak[indx[nn-1]][right];
				}
			}
			else
			{
				for (int x = 0; x < r; x++)
				{
					for (int y = left; y < c; y++)
					{
						cak[x][y] = cak[x][left-1];
					}
				}
			}
			left = right+1;
		}

        fout << "Case #" << tt + 1 << ": " << "\n";
		for (int i = 0; i < r; i++)
			fout << cak[i] << "\n";
	}

	return 0;
}

