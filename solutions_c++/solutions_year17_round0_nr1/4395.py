#include "Pancake.h"
#include <stdio.h>
#include <string>
#include <fstream>
#include <iostream>

int GetFlipCount(std::string pancakes, int flipWidth)
{
	int flipCount = 0;
	for (size_t pancakeIndex = 0; pancakeIndex < pancakes.length() + 1 - flipWidth; pancakeIndex++)
	{
		if (pancakes[pancakeIndex] == '-')
		{
			for (size_t flipIndex = pancakeIndex; flipIndex < pancakeIndex + flipWidth; flipIndex++)
			{
				if (pancakes[flipIndex] == '-')
				{
					pancakes[flipIndex] = '+';
				}
				else
				{
					pancakes[flipIndex] = '-';
				}
			}
			flipCount++;
		}
	}

	if(pancakes.find_first_of('-') != std::string::npos)
		return -1;

	return flipCount;
}

bool decipher_input()
{
	std::ifstream infile("in.in");

	if (infile.is_open())
	{
		size_t testCount = 0;
		char c = 0;
		while ( infile.get(c) && c != '\n' )
		{
			testCount *= 10;
			testCount += c - '0';
		}

		std::ofstream outfile;
		outfile.open ("out.txt");

		for ( size_t testCurrent = 0; testCurrent < testCount; testCurrent++ )
		{
			std::string pancakes = "";
			while ( infile.get(c) && c != ' ' )
			{
				pancakes += c;
			}

			int flipWidth = 0;
			while ( infile.get(c) && c != '\n' )
			{
				flipWidth *= 10;
				flipWidth += c - '0';
			}

			int flipCount = GetFlipCount(pancakes, flipWidth);

			outfile << "Case #" << testCurrent  + 1 << ": ";
			if (flipCount > -1)
			{
				outfile << flipCount;
			}
			else
			{
				outfile << "IMPOSSIBLE";
			}

			if (testCurrent + 1 < testCount)
				outfile << "\n";
		}

		infile.close();
		outfile.close();

		return true;
	}
	return false;
}

int main()
{
	return decipher_input();
}
