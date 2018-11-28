// GimmeVisa.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdint.h>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <string>

typedef std::pair<int64_t, double> Horse;
typedef std::pair<std::vector<Horse>, int64_t> TestCase;
typedef std::vector<TestCase> TestCases;

std::unordered_map<char, int> InitialsCount;

void Solve(TestCase& testCase)
{
	auto& horses = testCase.first;
	std::sort(horses.begin(), horses.end(), [](Horse& a, Horse& b) { return a.first > b.first; });
	int64_t destinationMax = testCase.second;

	double maxSpeed = (double)horses.back().second;
	double lastTimeToReach = ((double)(destinationMax - horses.back().first)) / (double) horses.back().second;
	if (horses.back().second == 0)
	{
		lastTimeToReach = 1;
	}

	//int64_t prevPos = horses.back().first;
	
//	uint64_t pointOfIntersection = destinationMax;

	auto size = horses.size() - 1;

	for (int64_t i = (size); i >= 0; --i)
	{
		auto& horse = horses[i];
		double time = (destinationMax - horse.first) / horse.second;
		if (time > lastTimeToReach)
		{
			//maxSpeed = (double) horse.second;
			lastTimeToReach = time;
		}
		//else
		//{
		//	uint64_t distanceBetween = prevPos - horse.first;
		//	uint64_t speedDiff = horse.second - maxSpeed;
		//	double timeOfIntersection = distanceBetween / speedDiff;
		//	uint64_t pointOfIntersection = horse.first + (timeOfIntersection * horse.second);
		//	//if (pointOfIntersection > )

		//}
	}
	double speed = destinationMax / lastTimeToReach;
	static int caseNum = 1;
	printf("Case #%d: %.6lf\n", caseNum++, speed);
//	std::cout << "Case #" << caseNum++ << ": " << speed  << std::endl;
}

int main()
{
	using namespace std;
	int numberOfTestCases;
	cin >> numberOfTestCases;
	TestCases all;
	for (decltype(numberOfTestCases) i = 0; i < numberOfTestCases; ++i)
	{
		TestCase testCase;

		uint64_t destination = 0;
		cin >> testCase.second;
		
		uint64_t otherHorses = 0;
		cin >> otherHorses;

		for (uint64_t h = 0; h < otherHorses; h++)
		{
			Horse horse;
			
			cin >> horse.first;
			cin >> horse.second;

			testCase.first.push_back(horse);
		}

		all.push_back(testCase);
	}

	for (auto& testCase : all)
	{
		Solve(testCase);
	}

    return 0;
}

