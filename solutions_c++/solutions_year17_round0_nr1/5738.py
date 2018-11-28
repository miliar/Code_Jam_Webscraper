// a-pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

void flip(char &ch) {
	if (ch == '+') ch = '-';
	else ch = '+';
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		// get info
		string pancakes = "";
		int flipper = 0;
		cin >> pancakes >> flipper;
		
		bool possible = true;
		int flips = 0;

		// calculate
		int j = 0;
		for (j = 0; j < pancakes.size() - (flipper - 1); j++)
		{
			if (pancakes[j] == '-')
			{
				// flip
				for (int k = 0; k < flipper; k++)
				{
					flip(pancakes[j + k]);
				}

				flips++;
			}
		}

		for (j; j < pancakes.size(); j++)
		{
			if (pancakes[j] == '-')
			{
				possible = false;
				break;
			}
		}

		// output
		cout << "Case #" << i + 1 << ": ";

		if (!possible)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << flips;
		}

		cout << endl;
	}

    return 0;
}

