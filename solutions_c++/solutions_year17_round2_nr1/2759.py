// round1b.cpp : definisce il punto di ingresso dell'applicazione console.
//

#include "stdafx.h"

#include <iostream>
#include <iomanip>

#define ULL unsigned long long

int main()
{
	std::cout << "test\n";
	//std::cerr << "test\n";

	int testCases = 0;
	std::cin >> testCases;

	ULL roadLength = 0;
	ULL horsesCount = 0;
	for (int i = 0; i < testCases; ++i)
	{
		std::cin >> roadLength >> horsesCount;
		//std::cerr << "Road Length KM: " << roadLength << " Horses Count: " << horsesCount << "\n";

		ULL initialPosition = 0;
		ULL maxSpeed = 0;
		double slowestArrivalTimeHours = 0.0;
		for (int j = 0; j < horsesCount; ++j)
		{
			std::cin >> initialPosition >> maxSpeed;
			//std::cerr << "Horse #" << j << ": Positioned at KM " << initialPosition << ", Max Speed: " << maxSpeed << "km/h\n";

			ULL deltaKm = roadLength - initialPosition;
			ULL deltaMeters = deltaKm * 1000;
			double timeToArrivalHours = (double)deltaKm / (double)maxSpeed;

			if (timeToArrivalHours > slowestArrivalTimeHours)
			{
				slowestArrivalTimeHours = timeToArrivalHours;
			}
			int asd = 0;
		}

		double cruiseSpeed = roadLength / slowestArrivalTimeHours;

		std::cerr << "Case #" << (i + 1) << ": " << std::fixed << std::setw (6) << std::setprecision (6) << cruiseSpeed << "\n";
		int asd = 0;
	}

    return 0;
}

