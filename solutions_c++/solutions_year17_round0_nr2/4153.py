// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include <iostream>
//#include "stdafx.h"
#include <vector>
#include <string>

#define ReturnIf(condition, ret) if(condition) return ret;



typedef int64_t TestCase;
typedef std::vector<TestCase> CaseVector;

int64_t optimize(TestCase number)
{
	int64_t copy = number;
	int64_t remove = 0;

	auto timesModified = 0;

	int64_t modifier = 10;
	auto last = number % 10;
	while (number != 0)
	{
		auto next = number % 10;
		if (next > last)
		{
			remove =  copy % (int64_t)pow(10, timesModified) + 1;
			next -= 1;
		}
		number /= modifier;
		timesModified++;
		last = next;
	}
	return copy - remove;
}

bool isTidy(TestCase number)
{
	auto modifier = 10;
	auto last = number%10;
	while (number != 0)
	{
		auto next = number%10;
		if (next > last) return false;
		number /= modifier;
		last = next;
	}

	return true;
}

int64_t SolveCase(TestCase startFrom)
{
	auto ret = startFrom;
	startFrom = optimize(startFrom);
	ReturnIf(isTidy(startFrom), startFrom);
	for (; startFrom >= 0; startFrom--)
	{
		ReturnIf(isTidy(startFrom), startFrom);
	//	std::cout << startFrom << std::endl;
	}
	return ret;
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	ReturnIf(testCases == 0, 0);

	CaseVector cases;

	while (testCases-- > 0)
	{
		int64_t largest = 0;

		std::cin >> largest;

		cases.push_back(largest);
	}

	int whichCase = 1;
	for (auto& testCase : cases)
	{
		auto res = SolveCase(testCase);
		if (res == -1)
		{
			std::cout << "Case #" << whichCase << ": IMPOSSIBLE" << std::endl;
		}
		else
		{
			std::cout << "Case #" << whichCase << ": " << res << std::endl;;
		}
		whichCase++;
	}


    return 0;
}

