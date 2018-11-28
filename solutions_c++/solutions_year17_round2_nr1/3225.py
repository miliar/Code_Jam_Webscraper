// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>

int main()
{
	int testCount;

	std::cin >> testCount;

	for (int i = 1; i <= testCount; i++) {
		int D;
		int N;

		std::cin >> D >> N;

		double maxTime = 0;

		for (int j = 0; j < N; j++) {
			int startPoint;
			int speed;
			double time;

			std::cin >> startPoint >> speed;
			time = (double)(D - startPoint) / speed;

			if (time > maxTime) {
				maxTime = time;
			}
		}

		double ans = D / maxTime;

		std::cout << "Case #" << i << ": "
			<< std::fixed << std::setprecision(6) << ans << std::endl;
	}

	return 0;
}
