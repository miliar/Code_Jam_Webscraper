// codejam.cpp : definisce il punto di ingresso dell'applicazione console.
// < tidy_small-1.in 2> tidy_small-1.out

#include "stdafx.h"

#include <iostream>

bool checkTidy (char *i_szNumber, int caseNumber)
{
	int length = strlen (i_szNumber);
	if (length == 0)
	{
		return false;
	}

	bool traceFlag = false;
	if (caseNumber == -1)//if (strcmp (i_szNumber, "1000") == 0)
	{
		traceFlag = true;
		int asd = 0;
	}

	int lastIndex = strlen (i_szNumber) - 1;

	char prevDigit = i_szNumber[lastIndex];
	for (int i = lastIndex - 1; i >= 0; --i)
	{
		if (i_szNumber[i] > prevDigit)
		{
			if (traceFlag)
			{
				std::cout << (i + 1) << "th digit not tidy [" << i_szNumber << "]\n";
			}

			bool removeOneDigit = false;
			if (i_szNumber[i] == '1')
			{
				removeOneDigit = true;
			}

			i_szNumber[i] = i_szNumber[i] - 1;

			for (int j = i + 1; j <= lastIndex; ++j)
			{
				if (i == 0 && removeOneDigit == true)
				{
					i_szNumber[j - 1] = '9';
				}
				else
				{
					i_szNumber[j] = '9';
				}
			}

			if (i == 0 && removeOneDigit == true)
			{
				i_szNumber[lastIndex] = '\0';
			}

			if (traceFlag)
			{
				std::cout << "Changed the number to " << i_szNumber << "\n";
			}
			return false;
		}

		prevDigit = i_szNumber[i];
	}

	return true;
}

int main ()
{
	int testCases = 0;
	std::cin >> testCases;

	for (int i = 0; i < testCases; ++i)
	{
		unsigned long long upperLimit = 0;
		std::cin >> upperLimit;

		// Print to string
		char szString[64];

		sprintf (szString, "%llu", upperLimit);

		while (checkTidy (szString, i) == false)
		{
			//--upperLimit;
			//sprintf (szString, "%llu", upperLimit);
		}

		std::cerr << "Case #" << (i + 1) << ": " << szString << "\n";
		//std::cout << "Case #" << (i + 1) << ": " << szString << "\n";

		//int asd = 0;
	}

	return 0;
}