// Cruise Control.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <unordered_set>
#include <iomanip>

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	int score;
	for (int i = 1; i <= nootests; i++)
	{
		int D, N;
		std::cin >> D >> N;
		double speed = std::numeric_limits<double>::max();
		for (int j = 0; j < N; j++)
		{
			int K, S;
			std::cin >> K >> S;
			if ((D - K) / (double)S >(D / speed)) speed = D / ((D - K) / (double)S);

		}
		std::cout << "Case #" << i << ": ";
		std::printf("%.6f", speed);
		//std::cout << std::fixed << std::setprecision(6) << "Case #" << i << ": " << speed << std::endl;
		std::cout << std::endl;
		
	}
	return 0;
}

