// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>
#include <cmath>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, /*k, l, p, q,*/ Ncases;

	cin >> Ncases;

	for (i = 1; i <= Ncases; i++)
	{
		__int64 lastNum;
		bool done = false;
		char numStr[20];
		memset(numStr, 0x00, 20);

		cin >> lastNum;
		if (lastNum < 10)
		{
			cout << "Case #" << i << ": " << lastNum << endl;
			continue;
		}

		// Greater than 10
		_i64toa(lastNum, numStr, 10);
		short lent = strlen(numStr) - 1;
		short currDig = lent;
		j = 0;
		while (currDig>0)
		{
			if (numStr[currDig] < numStr[currDig - 1])
			{
				short tmpDig = currDig;
				currDig = lent;
				numStr[currDig--] = '9';
				while (currDig>0 && (numStr[currDig] == '0' || currDig >= tmpDig))
					numStr[currDig--] = '9';
				numStr[currDig]--;
			}
			else
				currDig--;
		}

		lastNum = atoll(numStr);
		cout << "Case #" << i << ": " << lastNum << endl;
	}

	return 0;
}

