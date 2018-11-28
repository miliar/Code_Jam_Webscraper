/*
 * OversizedPancakeFlipper.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: mattias
 */

#include <iostream>
#include <string>
#include <vector>


void flip(std::vector<bool> &pancakes, int startIndex, int K)
{
	for (int i = 0; i < K; i++)
		pancakes[startIndex + i] = !pancakes[startIndex + i];
}

int main()
{
	int T;
	std::cin >> T;

	int K;
	std::string pancakesS;
	int flips = 0;
	std::vector<bool> pancakes;
	for (int caseNr = 0; caseNr < T; caseNr++)
	{
		flips = 0;
		std::cin >> pancakesS;
		pancakes.clear();
		pancakes.reserve(pancakesS.length());
		for (char c : pancakesS)
		{
			if (c == '+')
				pancakes.push_back(true);
			else
				pancakes.push_back(false);
		}
		std::cin >> K;

		bool impossible = false;
		for (size_t i = 0; i < pancakes.size(); i++)
		{
			if (pancakes[i])
				continue;
			if (i + K > pancakes.size())
			{
				std::cout << "Case #" << (caseNr+1) << ": IMPOSSIBLE" << std::endl;
				impossible = true;
				break;
			}
			flip(pancakes, i, K);
			flips++;
		}
		if (!impossible)
			std::cout << "Case #" << (caseNr+1) << ": " << flips << std::endl;

	}

	return 0;
}
