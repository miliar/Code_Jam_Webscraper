
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstring>
#include <iomanip>

using namespace std;

ifstream in("fracdec.in");
ofstream out("fracdec.out");


int main()
{
	int T;
	in >> T;

	for (int i = 1; i <= T; ++i)
	{
		unsigned long long lN;
		unsigned long long lK;
		in >> lN >> lK;

		map<unsigned long long, int> mapValues;
		mapValues[lN]++;

		unsigned long long lMin = 0;
		unsigned long long lMax = 1;

		while (lK > 0)
		{
			auto ite = mapValues.rbegin();
			if (ite == mapValues.rend())
			{
				lMin = 0;
				lMax = 0;
				break;
			}

			lN = ite->first;

			if (ite->second <= 1)
			{
				mapValues.erase(lN);
			}
			else
			{
				mapValues[lN]--;
			}
			

			lMin = (lN - 1) / 2;
			lMax = (lN - 1) % 2 + lMin;

			mapValues[lMin]++;
			mapValues[lMax]++;

			--lK;
		}

		out << "Case #" << i << ": " << lMax << " " << lMin << endl;
	}

	return 0;
}

