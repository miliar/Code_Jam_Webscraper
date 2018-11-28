// 2017_Qualification_B_TidyNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <cstdint>

std::ifstream input("B-large.in");
std::ofstream output("B-results-large.txt");

std::int64_t solve()
{
	std::int64_t N; 
	std::string strN;
	input >> N;

	strN = std::to_string(N);
	std::int64_t change = 1;
	for (int i = strN.size() - 1; i > 0; i--)
	{
		int diff = 10;
		for (int j = 0; j < i; j++)
		{
			int temp = static_cast<int>(strN[j+1]) - static_cast<int>(strN[j]);
			if (temp < diff)
				diff = temp;
		}

		if (diff < 0)
			N -= change*(static_cast<int>(strN[i])-48 + 1);
		strN = std::to_string(N);
		change *= 10;
	}

	return N;
}

int main()
{
	int T;
	input >> T;

	for (int cas = 1; cas <= T; cas++)
	{
		std::int64_t sol = solve();
		std::cout << "Case #" << cas << ": " << sol << "\n";
		output << "Case #" << cas << ": " << sol << "\n";
	}
}

