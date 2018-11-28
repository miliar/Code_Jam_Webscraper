// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include <iostream>
//#include "stdafx.h"
#include <vector>
#include <string>

#define ReturnIf(condition, ret) if(condition) return ret;
#define HAPPY '+'
#define BLANK '-'


typedef std::pair<std::string, int> TestCase;
typedef std::vector<TestCase> CaseVector;

void flip(char& c)
{
	c = c == HAPPY ? BLANK : HAPPY;
}

int SolveCase(TestCase t)
{
	auto flipSize = t.second;
	auto pancake = t.first;
	auto flipsPerformed = 0;

	for (int i = 0; i < pancake.length(); i++)
	{
		auto current = pancake[i];
		if (current == BLANK && (pancake.length() - i) >= flipSize)
		{
			flipsPerformed++;
			for (int j = 0; j < flipSize; j++)
			{
				auto atIndex = i + j;
				flip(pancake[atIndex]);
			}
		}
	}

	for (auto& c : pancake)
	{
		ReturnIf(c == BLANK, -1);
	}
	return flipsPerformed;
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	ReturnIf(testCases == 0, 0);

	CaseVector cases;

	while (testCases-- > 0)
	{
		std::string testCase;
		int flips = 0;

		std::cin >> testCase;
		std::cin >> flips;

		cases.push_back(std::make_pair(testCase, flips));
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

