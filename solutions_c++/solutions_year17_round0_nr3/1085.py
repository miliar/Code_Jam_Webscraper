// Bathroom Stalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <tuple>

std::tuple<unsigned long long, unsigned long long> getDistances(long long stalls, long long people)
{
	unsigned long long shortdistance;
	unsigned long long longdistance;
	if (stalls % 2 == 1)
	{
		shortdistance = longdistance = (stalls - 1) / 2;
	}
	else
	{
		shortdistance = stalls / 2 - 1;
		longdistance = stalls / 2;
	}
	if (people == 1)
	{
		return std::tie(shortdistance, longdistance);
	}
	else
	{
		if (people % 2 == 1)
		{
			return getDistances(shortdistance, people / 2);
		}
		else
		{
			return getDistances(longdistance, people / 2);
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	unsigned long long stalls;
	unsigned long long people;
	unsigned long long shortdistance;
	unsigned long long longdistance;
	for (int i = 1; i <= nootests; i++)
	{
		std::cin >> stalls >> people;
		std::tie(shortdistance, longdistance) = getDistances(stalls, people);
		std::cout << "Case #" << i << ": " << longdistance << " " << shortdistance << std::endl;
	}
return 0;
}