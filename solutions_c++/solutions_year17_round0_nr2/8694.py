
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

unsigned long long lAns = 0;

void process(const char* pzValue, int iPos, int iLen, char cPrev, string sValue, bool bOverride)
{
	if (iPos >= iLen)
	{
		unsigned long long lVal = strtoull(sValue.c_str(), NULL, 10);
		if (lAns < lVal)
			lAns = lVal;

		return;
	}

	char cEndChar = pzValue[iPos];

	if (bOverride)
	{
		cEndChar = '9';
	}

	
	for (char i = cPrev; i <= cEndChar; ++i)
	{
		bool bTempOvrd  = bOverride;
		if (i < cEndChar)
		{
			bTempOvrd = true;
		}

		process(pzValue, iPos + 1, iLen, i, sValue + i, bTempOvrd);
	}
}

int main()
{
	int N;
	in >> N;

	for (int i = 1; i <= N; ++i)
	{
		unsigned long long lValue;
		in >> lValue;

		lAns = 0;

		char zValue[100];
		snprintf(zValue, 100, "%llu", lValue);
		int iValLen = strlen(zValue);

		process(zValue, 0, iValLen, '1', "", false);

		if (lAns == 0)
		{
			char zNewAns[100];
			for (int j = 0; j < iValLen - 1; ++j)
			{
				zNewAns[j] = '9';
			}
			zNewAns[iValLen - 1] = '\0';
			lAns = strtoull(zNewAns, NULL, 10);
		}

		out << "Case #" << i << ": " << lAns << endl;
	}

	return 0;
}

