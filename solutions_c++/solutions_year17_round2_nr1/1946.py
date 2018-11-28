#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
#include <iomanip>

//https://code.google.com/codejam/contest/8294486/dashboard

typedef unsigned long long my_type;

struct Thorse
{
	my_type speed;
	my_type startPos;

	bool operator < (const Thorse& rhs) const
	{
		return startPos < rhs.startPos;
	}
};

struct CTest
{
	std::vector<Thorse> arrHorses;
	std::vector<long double> arrArivalTime;

	int numHorses;
	my_type DestDist;

	void Read()
	{
		std::cin >> DestDist;
		std::cin >> numHorses;

		arrHorses.resize(numHorses);
		for (auto& horse : arrHorses)
		{
			std::cin >> horse.startPos;
			std::cin >> horse.speed;
		}

		std::sort(arrHorses.begin(), arrHorses.end());

		arrArivalTime.resize(numHorses, 1.0);
	}



	long double MaxSpeed()
	{
		// max speed is the total distance divide by the arrival time of the first horse
		assert(numHorses > 0);
		{
			Thorse& tlast = arrHorses[numHorses - 1];
			arrArivalTime[numHorses - 1] = (DestDist - tlast.startPos) / (long double)tlast.speed;
		}
		

		for (int iHorse = numHorses - 2; iHorse >=0; --iHorse)
		{
			Thorse& Tcur = arrHorses[iHorse];
			arrArivalTime[iHorse] = (DestDist - Tcur.startPos) / (long double)Tcur.speed;
			if (arrArivalTime[iHorse] < arrArivalTime[iHorse + 1])
			{
				arrArivalTime[iHorse] = arrArivalTime[iHorse + 1];
			}
		}
		
		
		auto result = (long double)DestDist/ (long double)arrArivalTime[0];
		return result;
	}


	
};


int main()
{
	
	int nTests;
	std::cin >> nTests;

	std::setprecision(std::numeric_limits<long double>::digits10 + 1);
	for (int nCase =0 ; nCase < nTests; ++nCase)
	{				
		CTest curTest;
		curTest.Read();

		std::cout << "Case #" << nCase + 1 << ": " << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << curTest.MaxSpeed() << std::endl;
								
	}

	return 0;
}
