#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <climits>

using namespace std;

int main(int argc, char* argv[])
{

	fstream inputFile(argv[1], ios_base::in);
	fstream outputFile(argv[2], ios_base::out);
	int t;
	inputFile >> t;

	int k, minFlips, counter;
	string s;
	for (int i = 1; i <= t; i++)
	{
		inputFile >> s >> k;
		minFlips = 0;
		counter = 0;
		//cout << s << " " << k << endl;
		for (int j = 0; j < static_cast<int>(s.size()) - k + 1; j++)
		{
			if ('-' == s[j])
			{
				minFlips++;
				for (int m = 0; m < k; m++)
				{
					if ('-' == s[j + m])
					{
						s[j + m] = '+';
					}
					else
					{
						s[j + m] = '-';
					}
				}
			}
		}

		for (int j = 0; j < static_cast<int>(s.size()); j++)
		{
			if ('+' == s[j])
			{
				counter++;
			}
		}

		if (counter == static_cast<int>(s.size()))
		{
			outputFile << "Case #" << i << ": " << minFlips << endl;
		}
		else
		{
			outputFile << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}

