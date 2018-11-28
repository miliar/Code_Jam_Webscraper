#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
#include <functional>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int testCase = 1; testCase < numCases + 1; testCase++)
	{
		string numberString = "";
		int number[1005];
		cin >> numberString;
		int numberSize = numberString.size();
		for (int i = 0; i < numberSize; i++)
			number[i] = numberString[i] - '0';

		int numFlips = 0;
		int tp = 0;
		int ninePoint = numberSize;
		for (int i = numberSize - 1; i > 0; i--)
			if (number[i] < number[i - 1]) { ninePoint = i; number[i - 1]--; }
		for (int i = 0; i < numberSize; i++)
			if (i >= ninePoint) number[i] = 9;
		
		cout << "Case #" << testCase << ": ";
		bool noLeadingZeros = false;
		for (int i = 0; i < numberSize; i++)
		{
			if (number[i] != 0) noLeadingZeros = true;
			if (noLeadingZeros) cout << number[i];
		}
			
		cout << '\n';
	}
}

