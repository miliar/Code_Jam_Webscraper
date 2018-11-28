/*
 * TidyNumbers.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: mattias
 */

#include <cmath>
#include <iostream>

int main()
{
	int T;
	std::cin >> T;
	long long number;
	long long origNumber;
	for (int caseNr = 0; caseNr < T; caseNr++)
	{
		std::cin >> number;
		origNumber = number;
		int prevDigit = 10;
		int currentDigit;
		for (int i = 0; i <= std::floor(std::log10(origNumber)); i++)
		{
			currentDigit = (number / (long long)(std::pow(10,i))) % 10;
			if (currentDigit <= prevDigit)
			{
				prevDigit = currentDigit;
				continue;
			}
			prevDigit = currentDigit - 1;
			number = ((number / (long long)std::pow(10,i)) - 1)*(long long)std::pow(10,i) + (long long)std::pow(10,i) - 1;
		}
		std::cout << "Case #" << (caseNr + 1) << ": " << number << std::endl;
	}
	return 0;
}
