#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{

	fstream inputFile(argv[1], ios_base::in);
	fstream outputFile(argv[2], ios_base::out);
	int t;
	inputFile >> t;

	long long n;
	long long temp;
	int tidy = 0;
	int previousDigit = 9;
	for (int k = 1; k <= t; k++)
	{

		inputFile >> n;
		for (long long i = n; i >= 1; i--)
		{
			previousDigit = 9;
			tidy = 1;
			temp = i;
			while (temp > 0)
			{
				if (temp % 10 > previousDigit)
				{
					tidy = 0;
					break;
				}
				else
				{
					previousDigit = temp % 10;
					temp /= 10;
				}
			}
			if (tidy)
			{
				outputFile << "Case #" << k << ": " << i << endl;
				break;
			}
		}
		
	}

	return 0;
}

