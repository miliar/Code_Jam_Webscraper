// Tidy Numbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

std::string lowerNumberToEndingNines(std::string number, int i)
{
	if (i == 0 && number[i] == *"1")
	{
		std::string newNumber;
		for (int j = 0; j < number.length() - 1; j++)
		{
			newNumber.append("9");
		}
		return newNumber;
	}
	else
	{
		number[i] -= 1;
		i++;
		while (i < number.length())
		{
			number[i] = *"9";
			i++;
		}
		return number;
	}
}

std::string getTidyNumber(std::string number)
{
	for (int i = 0; i < number.length() - 1; i++)
	{
		if (number[i] > number[i + 1])
		{
			return getTidyNumber(lowerNumberToEndingNines(number, i));
		}
	}
	return number;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	std::string number;
	for (int i = 1; i <= nootests; i++)
	{
		std::cin >> number;

		std::cout << "Case #" << i << ": " << getTidyNumber(number) << std::endl;
	}
	return 0;
}

