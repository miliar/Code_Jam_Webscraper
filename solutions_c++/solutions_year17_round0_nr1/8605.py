
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
	int N;
	in >> N;

	for (int i = 1; i <= N; ++i)
	{
		string sAns = "IMPOSSIBLE";
		string sPanCakes;
		int iFlipSize;
		int iAns = 0;

		in >> sPanCakes >> iFlipSize;

		int iCakeCount = sPanCakes.size();
		int iIndex = 0;

		while (iIndex <= (iCakeCount - iFlipSize))
		{
			if (sPanCakes.at(iIndex) == '+')
			{
				++iIndex;
				continue;
			}

				
			for (int j = iIndex; j < iIndex + iFlipSize; ++j)
			{
				if (sPanCakes.at(j) == '+')
				{
					sPanCakes.replace(j, 1, "-");
				}
				else if (sPanCakes.at(j) == '-')
				{
					sPanCakes.replace(j, 1, "+");
				}
			}

			++iAns;
			++iIndex;
		}

		bool bSuccess = true;

		for (int j = iIndex - 1; j < iIndex - 1 + iFlipSize; ++j)
		{
			if (sPanCakes.at(j) != '+')
			{
				bSuccess = false;
			}
		}

		if (bSuccess)
		{
			sAns = std::to_string(iAns);
		}

		out << "Case #" << i << ": " << sAns << endl;
	}

	return 0;
}

