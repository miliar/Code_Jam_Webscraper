#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <map>

using namespace std;

void removeLeading0(std::string& number)
{
	int maxIndex = -1;
	int max = (int)number.size() - 1;

	for (int i = 0; i < max; ++i)
	{
		if (number[i] != '0')
			break;

		maxIndex = i;
	}

	if (maxIndex != -1)
	{
		int newHead = maxIndex + 1;

		std::rotate(number.begin(), number.begin() + newHead, number.end());
		number.resize(number.size() - newHead);
	}
}

bool isTidy(const std::string& number)
{
	if (number.size() == 1)
		return true;

	int max = (int)number.size() - 1;
	for (int i = 0; i < max; ++i)
	{
		if (number[i] > number[i + 1])
			return false;
	}

	return true;
}

void operation(std::string& res, int indice)
{
	for (int i = indice; i < (int)res.size(); ++i)
	{
		res[i] = '9';
	}

	--res[indice - 1];
}

std::string getLastTidy(const std::string& number)
{
	if (isTidy(number))
		return number;

	auto isValid = [&number](const std::string& numbFound)
	{
		if (numbFound.size() < number.size())
			return true;
		else if (numbFound.size() > number.size())
			return false;
		else
		{
			for (int i = 0; i < (int)number.size(); ++i)
			{
				if (numbFound[i] > number[i])
					return false;
			}
		}

		return true;
	};

	std::string res = number;
	int origin = (int)number.size() - 1;

	auto op = [&res](int indice)
	{
		operation(res, indice);
	};

	for (int i = origin; i > 0; --i)
	{
		if (res[i] < res[i - 1])
		{
			op(i);

			if (isTidy(res))
				return res;
		}
	}

	return res;
}

int main()
{
	ifstream inputFile("B-large.in");
	ofstream outputFile("output_2017.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": ";
		std::string number;

		inputFile >> number;

		std::string result = getLastTidy(number);
		removeLeading0(result);
	
		outputFile << result << endl;
	}

	return 0;
}
