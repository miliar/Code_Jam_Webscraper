#include <stdio.h>
#include <string>
#include <fstream>
#include <iostream>

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
			unsigned long long stallCount = 0;
			unsigned long long peopleCount = 0;
			infile >> stallCount;
			infile >> peopleCount;

			unsigned long long stallMost=stallCount;
			unsigned long long stallMore=0;


			unsigned long long stallMostCount=1;
			unsigned long long stallMoreCount=0;
			unsigned long long stallLessCount=0;
			unsigned long long stallLeastCount=0;

			bool mostLast = true;
			for (unsigned long long person=0; person < peopleCount; person++)
			{
				if(stallMostCount > 0)
				{
					stallMostCount--;
					if (stallMost%2 == 0)
					{
						stallLessCount++;
						stallLeastCount++;
					}
					else
					{
						stallLessCount+=2;
					}
				}
				else if (stallMoreCount > 0)
				{
					mostLast = false;
					stallMoreCount--;
					if (stallMore%2 == 0)
					{
						stallLessCount++;
						stallLeastCount++;
					}
					else
					{
						stallLeastCount+=2;
					}
				}
				else
				{
					mostLast = true;
					stallMost = stallMost/2;
					stallMore = stallMost - 1;
					stallMostCount = stallLessCount;
					stallMoreCount = stallLeastCount;

					stallLessCount = 0;
					stallLeastCount = 0;

					stallMostCount--;
					if (stallMost%2 == 0)
					{
						stallLessCount++;
						stallLeastCount++;
					}
					else
					{
						stallLessCount+=2;
					}
				}
			}

			outfile << "Case #" << testCurrent  + 1 << ": ";
			if(mostLast)
			{
				if (stallMost%2 == 0)
				{
					outfile << stallMost/2 << " " << (stallMost/2) - 1;
				}
				else
				{
					outfile << stallMost/2 << " " << stallMost/2;
				}
			}
			else
			{
				if (stallMore%2 == 0)
				{
					outfile << stallMore/2 << " " << (stallMore/2) - 1;
				}
				else
				{
					outfile << stallMore/2 << " " << stallMore/2;
				}
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
