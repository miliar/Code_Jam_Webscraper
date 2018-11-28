// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include <iostream>
//#include "stdafx.h"
#include <vector>
#include <string>

#define ReturnIf(condition, ret) if(condition) return ret;



typedef std::pair<int64_t, int64_t> TestCase;
typedef std::vector<TestCase> CaseVector;


TestCase SolveCase(TestCase startFrom)
{
	auto people = startFrom.second;
	auto max = startFrom.first + 1;
	auto min = 0;

	while (people-- > 0)
	{
		auto middle = (max + min) / 2;
		auto arePeopleEven = (people % 2) == 0;
		
		auto leftSide = (middle - min) - 1;
		auto rightSide = (max - middle) - 1;

		auto isLeftBigger = leftSide > rightSide;

		if (isLeftBigger)
		{
			if (!arePeopleEven)
			{
				max = middle;
			}
			else
			{
				min = middle;
			}
		}
		else
		{
			if (!arePeopleEven)
			{
				min = middle;

			}
			else
			{
				max = middle;
			}
		}

		auto addMissing = people%2;
		people /= 2;
		people += addMissing;

		if (people == 0)
		{
			return std::make_pair(leftSide,rightSide);
		}

	}
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	ReturnIf(testCases == 0, 0);

	CaseVector cases;

	while (testCases-- > 0)
	{
		int64_t one = 0;
		int64_t two = 0;

		std::cin >> one;
		std::cin >> two;

		cases.push_back(std::make_pair(one,two));
	}

	int whichCase = 1;
	for (auto& testCase : cases)
	{
		auto res = SolveCase(testCase);
		{
			if (res.first > res.second)
			{
				std::cout << "Case #" << whichCase << ": " << res.first << " " << res.second << std::endl;
			}
			else
			{
				std::cout << "Case #" << whichCase << ": " << res.second << " " << res.first << std::endl;
			}
		}
		whichCase++;
	}


    return 0;
}

