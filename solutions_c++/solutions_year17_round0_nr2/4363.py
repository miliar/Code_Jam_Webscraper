#include "TidyNumbers.h"

#include <stdio.h>
#include <string>
#include <fstream>
#include <iostream>

bool decipher_input(std::string filename)
{
	std::ifstream infile(filename);

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
			std::string tidyNumber = "";
			infile.get(c);
			tidyNumber += c;

			bool nineTime = false;
			while ( infile.get(c) && c != '\n' )
			{
				if (nineTime)
				{
					tidyNumber += '9';
				}
				else
				{
					tidyNumber += c;

					int prevIndex = tidyNumber.length() - 2;

					bool borrowing = false;
					while (prevIndex >= 0 && (borrowing || tidyNumber[prevIndex] > tidyNumber[prevIndex + 1]))
					{
						borrowing = false;
						tidyNumber[prevIndex+1] = '9';
						if(tidyNumber[prevIndex] == '1' && prevIndex != 0)
						{
							tidyNumber[prevIndex] = '9';
							borrowing = true;
						}
						else
						{
							tidyNumber[prevIndex] = tidyNumber[prevIndex] - 1;
						}
						prevIndex -= 1;
						nineTime = true;
					}
				}
			}

			if(tidyNumber[0] == '0')
				tidyNumber.erase(0, 1);

			outfile << "Case #" << testCurrent  + 1 << ": ";
			outfile << tidyNumber;

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
	return decipher_input("in.in");
}


