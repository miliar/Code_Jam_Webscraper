// TidyNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>

using namespace std;

inline void subtractOne(string& sNum, int nIndex)
{
	if (sNum[nIndex] == '0')
	{
		sNum[nIndex] = '9';
		subtractOne(sNum, nIndex - 1);
	}
	else
	{
		--sNum[nIndex];
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		string sNum;
		cin >> sNum;

		int nDigits = sNum.length();

		// go backwards through the string from index N to 0
		// if str[N-1] > str[N], subtract 1 from str[N-1] and make all following digits 9

		for (int i = nDigits - 1; i > 0; --i)
		{
			if (sNum[i] < sNum[i - 1])
			{
				subtractOne(sNum, i - 1);
				for (int j = i; j < nDigits; ++j)
				{
					sNum[j] = '9';
				}
			}
		}

		// remove leading zeros - not efficient but should be fine
		while(sNum.find('0') == 0)
			sNum.erase(0, 1);


		cout << "Case #" << t << ": " << sNum << endl;
	}
    return 0;
}

